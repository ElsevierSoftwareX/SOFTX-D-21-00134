# -*- coding: utf-8 -*-
"""
This module contains all functions to visualize the data set.
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import configparser
import sys


def get_PollutantVolume(db, FirstOrder=None, SecondOrder=None):
    """
    Sorts the input data table, to the named order parameters, which are all possible column names.

    Parameters
    ----------
    db : DataFrame
        input data table.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is None.
    SecondOrder : TYPE, optional
        Name of column, the data are sorted in the second order. The default is None.

    Returns
    -------
    data : DataFrame
        Data table, sorted to the announced order parameters.

    """
    if SecondOrder is None:
        if FirstOrder is None:
            d = {'Order': ['NoneGiven'], 'TotalQuantity': [db.TotalQuantity.sum()]}
            data = pd.DataFrame(data=d)
        else:
            data = db.groupby([FirstOrder]).sum().reset_index()
            data = data[[FirstOrder, 'TotalQuantity']]
    else:
        timer = 0
        for items in db[SecondOrder].unique():
            if timer == 0:
                timer = 1
                data = db[db[SecondOrder] == items].groupby([FirstOrder]).TotalQuantity.sum().reset_index()
                data = data.rename(columns={'TotalQuantity': items})
            else:
                itemdata = db[db[SecondOrder] == items].groupby([FirstOrder]).TotalQuantity.sum().reset_index()
                data = pd.merge(data, itemdata, on=[FirstOrder], how='outer')
                data = data.rename(columns={'TotalQuantity': items})
    return data


def get_PollutantVolumeRel(db, FirstOrder=None, SecondOrder=None, normtop=None, normtov=None):
    """
    Normalises the volume values to one specific value. This value is either the present max value of the returned data table or is specifed by normtop(osition) or normtov(alue).

    Parameters
    ----------
    db : DataFrame
        input data table.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is None.
    SecondOrder : String, optional
        Name of column, the data are sorted in the second order. The default is None.
    normtop : list, optional
        With this parameter you can choose a entry of your data table, that the entries should be normalised too. The first item of the list has to be one value of the FirstOrder. If SecondOrder is called, the second value has to be a value of the SecondOrder. The default is None.
    normtov : float, optional
        With this parameter you can define a value, that the PollutantVolume entries are normalised to. The default is None
    Returns
    -------
    data : DataFrame
        Data table sorted to the announced parameters. The values are normed to one specific max value. If normtop and normtov are both unequal None, no normalization is applied, since there is no concrete value, that can be normed to.

    """
    data = get_PollutantVolume(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder)

    if (normtop is not None) and (normtov is not None):
        print('Multiple normto values given. Decide for either normtoposition or normtovalue. No normalisation applied!')
        return data

    if (normtop is None) and (normtov is None):
        maxvalue = np.nanmax(data.iloc[:, 1:].to_numpy())
    elif normtop is not None:
        if FirstOrder is None:
            maxvalue = data.iloc[0, 1]
        elif SecondOrder is None:
            maxvalue = data[data[FirstOrder] == normtop[0]].reset_index().loc[0, 'TotalQuantity']
        else:
            maxvalue = data[data[FirstOrder] == normtop[0]].reset_index().loc[0, normtop[1]]
    elif normtov is not None:
        maxvalue = normtov

    if pd.isnull(maxvalue):
        print('The determined maxvalue is of type Nan. Therefore, the normalization does not' +
              ' work and a DataFrame with NAN is returned.')

    data.iloc[:, 1:] = data.iloc[:, 1:] / maxvalue
    return data


def get_PollutantVolumeChange(db, FirstOrder=None, SecondOrder=None):
    """
    Derives the pollutant volume change to the previous year.

    Parameters
    ----------
    db : DataFrame
        the filtered input DataFrame.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is None.
    SecondOrder : String, optional
        Name of column, the data are sorted in the second order. The default is None.

    Returns
    -------
    data : DataFrame
        The change of TotalQuantity to the previous data entry

    """
    data = get_PollutantVolume(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder)
    if SecondOrder is None:
        data = data.rename(columns={'TotalQuantity': 'TotalQuantityChange'})
    for items in data.columns:
        if items != FirstOrder:
            data[items] = data[items].diff()
    data = data.iloc[1:]
    return data


def get_ImpurityVolume(db, target, FirstOrder='FacilityReportID', ReleaseMediumName='Air', absolute=False, FacilityFocus=True, impurity=None, statistics=False):
    """
    Creates a table with the impurities of the target pollutant, sorted by the FirstOrder parameter. Putting the absolute parameter to True, gives absolute values instead of relative.

    Parameters
    ----------
    db : DataFrame
        Data to look for impurities.
    target : String
        Pollutant name of the pollutant, which is not seen as impurity.
    FirstOrder : String, optional
        Order to sort the impurities by. E.g. NACERegionGeoCode, FacilityReportID, NACEMainEconomicActivityCode. The default is 'FacilityReportID'.
    ReleaseMediumName : String, optional
        The release medium name in which the target is emitted and in which can be impurities. The default is 'Air'.
    absolute : Boolean, optional
        If this parameter is set on False, this function returns the impurity relative to the target pollutant emission. If it is set on True, the absolute emission value is returned. The default is False.
    FacilityFocus : Boolean, optional
        If this parameter is true, only the impurities in the facilities in which the target is emittet is taken in to consideration. If it is false, all data are taken into consideration. The default is True.
    impurity : String, optional
        With this parameter, you can specify the impurity pollutant you want to return. Otherwise, all present impurities are shown. The default is None.
    statistics : Boolean, optional
        If this argument is True, the statistics (determined by .describe()) of the output DataFrame are returned, instead of the usual impurity table. The default is False.

    Returns
    -------
    d2 : DataFrame
        Data table with the rows beeing the different present order values, and in the columns their respective emission of the target pollutant and the absolute emission of the impurities.
    d3 : DataFrame
        Data table with the rows beeing the different present order values, and in the columns their respective emission of the target pollutant and the relative emission of the impurities.

    """
    db = db[db.ReleaseMediumName == ReleaseMediumName]
    d1 = db[db.PollutantName == target]
    d2 = get_PollutantVolume(d1, FirstOrder=FirstOrder)
    d3 = get_PollutantVolume(d1, FirstOrder=FirstOrder)
    if FacilityFocus == True:
        ff = get_PollutantVolume(d1, FirstOrder='FacilityReportID').FacilityReportID.unique()
        db = db[db.FacilityReportID.isin(ff)]
    for items in np.delete(db.PollutantName.unique(), np.argwhere(db.PollutantName.unique() == target)):
        item = db[db.PollutantName == items].groupby([FirstOrder]).TotalQuantity.sum().reset_index()
        item = item[[FirstOrder, 'TotalQuantity']].rename(columns={'TotalQuantity': items})
        d2 = d2.merge(item, how='left', on=FirstOrder)
        d3[items] = d2.loc[:, items] / d2.loc[:, 'TotalQuantity']

    if impurity != None:
        d2 = d2[[FirstOrder, 'TotalQuantity', impurity]]
        d3 = d3[[FirstOrder, 'TotalQuantity', impurity]]
    
    if absolute:
        if statistics:
            return d2.describe()
        else:
            return d2
    else:
        if statistics:
            return d3.describe()
        else:
            return d3


def plot_PollutantVolume(db, FirstOrder=None, SecondOrder=None, stacked=False, *args, **kwargs):
    """

    Plots the filtered data set. The first order is the x-axis, the second order is a differentiation of the y-values.

    Parameters
    ----------
    db : DataFrame
        The data to be plotted.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is None.
    SecondOrder : String, optional
        Name of column, the data are sorted in the second order. The default is None.
    stacked : Boolean, optional
        Stacks the bars for second order. The default is False.
    *args : TYPE
        pandas.plot() input variables.
    **kwargs : TYPE
        pandas.plot() input variables.

    Returns
    -------
    ax : Axes
        Plot of the data in db, sorted by FirstOrder and SecondOrder if given.

    """
    data = get_PollutantVolume(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder)
    if SecondOrder is None:
        ax = data.plot(x=FirstOrder, y='TotalQuantity', kind='bar', *args, **kwargs)
    else:
        if stacked is True:
            ax = data.plot.bar(x=FirstOrder, stacked=True, *args, **kwargs)
        else:
            ax = data.plot.bar(x=FirstOrder, *args, **kwargs)
    return ax


def plot_PollutantVolumeRel(db, FirstOrder=None, SecondOrder=None, normtop=None, normtov=None, stacked=False, *args, **kwargs):
    """
    Plots the normed pollutant volume of the data set, The first order is the x-axis, the second order is a differentiation of the y-values.

    Parameters
    ----------
    db : DataFrame
        The data to be plotted.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is None.
    SecondOrder : String, optional
        Name of column, the data are sorted in the second order.. The default is None.
    normtop : list, optional
        With this parameter you can choose a entry of your data table, that the entries should be normalised too. The first item of the list has to be one value of the FirstOrder. If SecondOrder is called, the second value has to be a value of the SecondOrder. The default is None.
    normtov : float, optional
        With this parameter you can define a value, that the PollutantVolume entries are normalised to. The default is None.
    stacked : Boolean, optional
        Stacks the bars for second order. The default is False.
    *args : TYPE
        pandas.plot() input variables.
    **kwargs : TYPE
        pandas.plot() input variables.

    Returns
    -------
    ax : Axes
        Plot of the data in db, sorted by FirstOrder and SecondOrder if given.

    """
    data = get_PollutantVolumeRel(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder, normtop=normtop, normtov=normtov)
    if SecondOrder is None:
        ax = data.plot(x=FirstOrder, y='TotalQuantity', kind='bar', *args, **kwargs)
    else:
        if stacked is True:
            ax = data.plot.bar(x=FirstOrder, stacked=True, *args, **kwargs)
        else:
            ax = data.plot.bar(x=FirstOrder, *args, **kwargs)
    return ax


def plot_PollutantVolumeChange(db, FirstOrder=None, SecondOrder=None, stacked=False, *args, **kwargs):
    """
    Plots the volume change of the data set. The first order is the x-axis, the second order is a differentiation of the y-values.

    Parameters
    ----------
    db : DataFrame
        The data to be plotted.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is None.
    SecondOrder : String, optional
        Name of column, the data are sorted in the second order.. The default is None.
    stacked : Boolean, optional
        Stacks the bars for second order. The default is False.
    *args : TYPE
        pandas.plot() input variables.
    **kwargs : TYPE
        pandas.plot() input variables.

    Returns
    -------
    ax : Axes
        Plot of the data in db, sorted by FirstOrder and SecondOrder if given.

    """
    data = get_PollutantVolumeChange(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder)
    if SecondOrder is None:
        ax = data.plot(x=FirstOrder, y='TotalQuantityChange', kind='bar', *args, **kwargs)
    else:
        if stacked is True:
            ax = data.plot.bar(x=FirstOrder, stacked=True, *args, **kwargs)
        else:
            ax = data.plot.bar(x=FirstOrder, *args, **kwargs)
    return ax


def plot_ImpurityVolume(db, target, impurity, FirstOrder='FacilityReportID', ReleaseMediumName='Air', absolute=False, FacilityFocus=True, statistics=False, PlotNA=True, *args, **kwargs):
    """
    Plots the impurities for the different FirstOrder values or the statistics of the entries.

    Parameters
    ----------
    db : DataFrame
        The data to be plotted.
    target : String
        The target pollutant which is impured.
    impurity : String
        The impurity which is to be analyzed.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is 'FacilityReportID'.
    ReleaseMediumName : TYPE, optional
        The release medium name in which the target is emitted and in which can be impurities. The default is 'Air'.
    absolute : Boolean, optional
        If this parameter is set on False, this function returns the impurity relative to the target pollutant emission. If it is set on True, the absolute emission value is returned. The default is False.
    FacilityFocus : Boolean, optional
        If this parameter is true, only the impurities in the facilities in which the target is emittet is taken in to consideration. If it is false, all data are taken into consideration. The default is True.
    statistics : Boolean, optional
        If this parameter is True, the statistics of the data are plotted. If it is False, the actual values are plotted. The default is False.
    PlotNA : Boolean, optional
        This argument is a option for discarding the na values if plotting the impurities. The default is True.
    *args : TYPE
        pandas.plot() input variables.
    **kwargs : TYPE
        pandas.plot() input variables.

    Returns
    -------
    ax : Axes
        Plot of the impurities in db, or the statistics of these impurities.

    """
    data = get_ImpurityVolume(db=db, target=target, FirstOrder=FirstOrder, ReleaseMediumName=ReleaseMediumName, impurity=impurity, absolute=absolute, FacilityFocus=FacilityFocus, statistics=statistics)

    if statistics is True:
        ax = data.drop('count').plot(kind='bar', y=impurity, *args, **kwargs)
    else:
        if PlotNA:
            ax = data.drop('TotalQuantity', axis=1).plot(x=FirstOrder, y=impurity, kind='bar', *args, **kwargs)
        else:
            ax = data.drop('TotalQuantity', axis=1).dropna().plot(x=FirstOrder, y=impurity, kind='bar', *args, **kwargs)

    return ax


def get_mb_borders(mb):
    """
    Generates a list with the borders of the objects of a GeoDataFrame.

    Parameters
    ----------
    mb : GeoDataFrame
        Table of geo objects which over all borders are wanted.

    Returns
    -------
    borders : List
        The x,y min/max values.

    """
    foo = mb.bounds
    borders = (foo.minx.min(), foo.miny.min(), foo.maxx.max(), foo.maxy.max())
    return list(borders)


def exclude_DataOutsideBorders(borders, gdf):
    """
    seperates data, that are inside and outside given borders

    Parameters
    ----------
    borders : list
        x,y min/max.
    gdf : GeoDataFrame
        GeoDataFrame that is to process.

    Returns
    -------
    gdft : DataFrame
        GeoDataFrame with data inside the borders.
    gdff : DataFrame
        GeoDataFrame with data outside the borders.

    """
    gdft = gdf
    gdff = gpd.GeoDataFrame(columns=gdf.columns)
    gdff['geometry'] = ""
    for i in range(len(gdf)):
        if (gdf.geometry.iloc[i].x < borders[0]) or (gdf.geometry.iloc[i].x > borders[2]) or (gdf.geometry.iloc[i].y < borders[1]) or (gdf.geometry.iloc[i].y > borders[3]):
            gdff = gdff.append(gdf.iloc[i])
            gdft = gdft.drop([i], axis=0)
    return gdft, gdff


def add_MarkerSize(gdf, MaxMarker):
    """
    adds column MarkerSize to GeoDataFrame. If MaxMarker=0, all markers have size 1. Else, they are normalized to max value and multiplied by value of MaxMarker.

    Parameters
    ----------
    gdf : GeoDataFrame
        GeoDataFrame, which gets additional column.
    MaxMarker : Int
        defines the marker size of the biggest marker. If 0, all markers have same size.

    Returns
    -------
    gdf : GeoDataFrame
        GeoDataFrame with added column 'MarkerSize'.

    """
    gdf['MarkerSize'] = ""
    markernorm = gdf.TotalQuantity.max()
    if MaxMarker == 0:
        gdf['MarkerSize'] = 1
    else:
        gdf['MarkerSize'] = gdf['TotalQuantity'] / markernorm * MaxMarker
    return gdf


def create_GDFWithRightProj(dfgdf, OutProj=None):
    """
    Converts DataFrame into GeoDataFrame and changes the projection if new projection is given as input.

    Parameters
    ----------
    dfgdf : DataFrame/GeoDataFrame
        Data that is about to be converted into a GeoDataFrame and experience a projection change if wanted.
    OutProj : String, optional
        Target projection of the geometry of the data. The default is None.

    Returns
    -------
    gdf : GeoDataFrame
        Data stored as GeoDataFrame and with eventually changed geometry CRS.

    """
    if isinstance(dfgdf, pd.DataFrame):
        gdf = gpd.GeoDataFrame(dfgdf, geometry=gpd.points_from_xy(dfgdf.Long, dfgdf.Lat), crs='EPSG:4326').reset_index(drop=True)
    elif isinstance(dfgdf, gpd.GeoDataFrame):
        if dfgdf.crs is None:
            gdf = gpd.GeoDataFrame(dfgdf, geometry=gpd.points_from_xy(dfgdf.Long, dfgdf.Lat), crs='EPSG:4326').reset_index(drop=True)
    if OutProj != None:
        gdf = change_proj(gdf, OutProj=OutProj)
    return(gdf)


def change_proj(gdf, OutProj=None):
    """
    Changes The projection of the input GeoDataFrame to the projection defined with OutProj. If no CRS is given for the geometry, the function tries to recover information from gdf.

    Parameters
    ----------
    gdf : GeoDataFrame
        Data that CRS is to be changed.
    OutProj : Datatype, optional
        Code for target output projection. See http://pyproj4.github.io/pyproj/stable/api/crs/crs.html#pyproj.crs.CRS.from_user_input for input possibilities. The default is None.

    Returns
    -------
    gdf : GeoDataFrame
        Data with new projection in the geometry.

    """
    if OutProj is None:
        sys.exit('InputError: For the change of projection is a target projection required.')

    if gdf.crs is None:
        if 'Long' not in gdf.columns or 'Lat' not in gdf.columns:
            sys.exit('InputError: No information about projection of geometry.' +
                     ' Define CRS or give coordinates as Long and Lat!')
        gdf = gpd.GeoDataFrame(gdf, geometry=gpd.points_from_xy(gdf.Long, gdf.Lat), crs='EPSG:4326').reset_index(drop=True)
    gdf = gdf.to_crs(crs=OutProj)

    return gdf


def map_PollutantSource(db, mb, category=None, MarkerSize=0, OutProj=None,
                        ReturnMarker=0, *args, **kwargs):
    """
    maps pollutant sources given by db on map given by mb.

    Parameters
    ----------
    db : DataFrame/GeoDataFrame
        Data table on pollutant sources.
    mb : DataFrame
        geo data table.
    category : String
        The column name of db, which gets new colors for every unique entry.
    MarkerSize : Int
        maximal size of the largest marker.
    OutProj : DataType
        Code for targeted output projection. See http://pyproj4.github.io/pyproj/stable/api/crs/crs.html#pyproj.crs.CRS.from_user_input for input possibilities. The default is None.
    ReturnMarker : Int
        If put on 1, the function returns a DataFrame with all data that are plotted. If put on 2, the function returns a DataFrame with all data  that are not plotted, because their coordinates are outside the geo borders.
    *args : TYPE
        Geopandas.plot() input arguments.
    **kwargs : TYPE
        Geopandas.plot() input arguments.

    Returns
    -------
    ax : Axes
        Plot with pollutant sources on map.
    gdfp : GeoDataFrame
        GeoDataFrame with all sources that are within geo borders and therefore plotted.
    gdfd : GeoDataFrame
        GeoDataFrame with all sources that are outside geo borders and therefore dropped.

    """
    # color selecting is bad.
    # Calling gdfp, gdfd requires 2 times performing the function, perhaps better way.
    ax = mb.plot(zorder=1, *args, **kwargs)
    colorlist = ['r', 'y', 'g', 'c', 'm', 'b']
    borders = get_mb_borders(mb)
    if category is None:
        gdf = create_GDFWithRightProj(db, OutProj=OutProj)
        gdfp = exclude_DataOutsideBorders(borders=borders, gdf=gdf)[0]
        gdfd = exclude_DataOutsideBorders(borders=borders, gdf=gdf)[1]
        gdfp = add_MarkerSize(gdfp, MaxMarker=MarkerSize)
        ax = gdfp.plot(color='r', zorder=1, markersize=gdfp['MarkerSize'], *args, **kwargs)

    else:
        for items in db[category].unique():
            if not colorlist:
                print('Running out of color')
                break
            color = colorlist[0]
            colorlist.remove(color)
            itemdata = db[db[category] == items].reset_index()
            gdf = create_GDFWithRightProj(itemdata, OutProj=OutProj)
            gdfp = exclude_DataOutsideBorders(borders=borders, gdf=gdf)[0]
            gdfd = exclude_DataOutsideBorders(borders=borders, gdf=gdf)[1]
            gdfp = add_MarkerSize(gdfp, MaxMarker=MarkerSize)
            ax = gdfp.plot(color=color, zorder=1, markersize=gdfp['MarkerSize'], *args, **kwargs)

    if gdfd.empty is False:
        print('Some data points are out of borders')
    else:
        print('All data points are within rectangular borders')

    if ReturnMarker == 0:
        return ax

    elif ReturnMarker == 1:
        return gdfp

    else:
        return gdfd


def map_PollutantRegions(db, mb, ReturnMarker=0, *args, **kwargs):
    """
    Visualizes the pollutant emission of regions with a color map. The classification of regions is selected with the choice of mb. If ReturnMarker is put on 1, the function returns a DataFrame with the plotted data. If ReturnMarker is put on 2, the function returns the DataFrame with Data that have no complementary NUTSID in the mapdata.

    Parameters
    ----------
    db : DataFrame
        Pollution data that are plotted.
    mb : TYPE
        Map data for plotting. The region selection corresponds to the selection of mb.
    ReturnMarker : int
        If it has the value 0, the function returns the plot. If put on 1, the function returns a DataFrame with all data that are plotted. If put on 2, the function returns a DataFrame with all data that are not plotted, because their NUTS_ID is not present in the mapdata.
    *args : TYPE
        Geopandas.plot() input arguments.
    **kwargs : TYPE
        Geopandas.plot() input arguments.

    Returns
    -------
    ax : Axes
        Axes with colormap of the pollution emission.
    dbp : DataFrame
        Data that are plotted
    dbna : DataFrame
        Data that are not plotted, because the NUTS_ID is not present in the mapdata.

    """

    NUTSlvl = mb.LEVL_CODE.unique()
    if len(NUTSlvl) != 1:
        print('There are multiple NUTS-Levels present in the map data input.' +
              'This function can not seperate the data in the required way. No Output!')
        return None
    NUTSlvl = NUTSlvl[0]

    dbpremerge = pd.DataFrame(columns=['NUTS_ID', 'TotalQuantity'])
    if NUTSlvl <= 2:
        db01 = get_PollutantVolume(db, FirstOrder='NUTSRegionGeoCode')
        for item in mb.NUTS_ID.unique():
            itemdata = db01[db01.NUTSRegionGeoCode.str.startswith(item)]
            itemvalue = itemdata.TotalQuantity.sum()
            dbpremerge = dbpremerge.append({'NUTS_ID': item, 'TotalQuantity': itemvalue}, ignore_index=True)
    elif NUTSlvl == 3:
        print('The NUTS-Level of the map data is to high.' +
              ' The geospatial resolution of the emission data is not high' +
              ' enough to differentiate on level 3 regions. Use NUTS-LVL smaller or equal to 2.')
        return None

    db02 = pd.merge(mb, dbpremerge, how='left', on=['NUTS_ID'])
    ax = db02.plot(column='TotalQuantity', *args, **kwargs)

    presentNUTS_IDs = tuple(mb.NUTS_ID.tolist())
    dbp = db01[db01.NUTSRegionGeoCode.str.startswith(presentNUTS_IDs)]
    dbna = db01[~db01.NUTSRegionGeoCode.str.startswith(presentNUTS_IDs)]

    if ReturnMarker == 0:
        return ax

    elif ReturnMarker == 1:
        return dbp

    else:
        return dbna


def export_fig(fig, path=None, filename=None, **kwargs):
    """
    Exports the choosen figure to a given path or to the export folder of the project if no path is given.

    Parameters
    ----------
    fig : figure
        The figure that is to export.
    path : String, optional
        Path under which the file is stored. The filename has to be included. The default is None.
    filename : String, optional
        Filename under which the figure is stored in the Export folder of the project. The default is None.
    **kwargs : TYPE
        Matplotlib.savefig() input arguments.

    Returns
    -------
    None.

    """
    if path is None and filename is None:
        print('A filename is required.')
        return None

    elif path is None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 'configuration', 'configuration.ini'))
        path = config['PATH']['path']
        path = os.path.join(os.path.join(path, 'ExportData'), filename)
    elif path is not None and filename is None:
        path = os.path.join(path, filename)

    if path.endswith(r'{}'.format(os.sep)):
        print('The file name or path must end with a file type extension')
        return None

    fig.savefig(path, **kwargs)

    return None
