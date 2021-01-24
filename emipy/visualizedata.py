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
                data = pd.merge(data, itemdata, on=[FirstOrder])
                data = data.rename(columns={'TotalQuantity': items})
    return data


def get_PollutantVolume_rel(db, FirstOrder=None, SecondOrder=None, norm=None):
    """
    Normes the volume values to the absolut max value or max value of first order value which is called with norm.

    Parameters
    ----------
    db : DataFrame
        input data table.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is None.
    SecondOrder : String, optional
        Name of column, the data are sorted in the second order. The default is None.
    norm : variable, optional
        specific first order value, which should be normed to. The default is None.

    Returns
    -------
    data : DataFrame
        Data table sorted to the announced paramters. The values are normed to some specific max value.

    """
    data = get_PollutantVolume(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder)
    if norm is None:
        maxvalue = data.iloc[:, 1:].to_numpy().max()
    else:
        maxvalue = data[data[FirstOrder] == norm].to_numpy().max()
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
        Name of column, the data are sorted in the second order.. The default is None.

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


def get_ImpurityVolume(db, Target, FirstOrder='FacilityReportID', ReleaseMediumName='Air', absolute=False, FacilityFocus=True, Impurity=None):
    """
    Creates a table with the impurities of the target pollutant, sorted by the FirstOrder parameter. Putting the absolute parameter to True, gives absolute values instead of relative.

    Parameters
    ----------
    db : DataFrame
        Data to look for impurities.
    Target : String
        Pollutant name of the pollutant, which is not seen as impurity.
    FirstOrder : String, optional
        Order to sort the impurities by. E.g. NACERegionGeoCode, FacilityReportID, NACEMainEconomicActivityCode. The default is 'FacilityReportID'.
    ReleaseMediumName : String, optional
        The release medium name in which the target is emitted and in which can be impurities. The default is 'Air'.
    absolute : Boolean, optional
        If this parameter is set on False, this function returns the impurity relative to the target pollutant emission. If it is set on True, the absolute emission value is returned. The default is False.
    FacilityFocus : Boolean, optional
        If this parameter is true, only the impurities in the facilities in which the target is emittet is taken in to consideration. If it is false, all data are taken into consideration. The default is True.
    Impurity : String, optional
        With this parameter, you can specify the impurity pollutant you want to return. Otherwise, all present impurities are shown. The default is None.

    Returns
    -------
    d2 : DataFrame
        Data table with the rows beeing the different present order values, and in the columns their respective emission of the target pollutant and the absolute emission of the impurities.
    d3 : DataFrame
        Data table with the rows beeing the different present order values, and in the columns their respective emission of the target pollutant and the relative emission of the impurities.

    """
    db = db[db.ReleaseMediumName == ReleaseMediumName]
    d1 = db[db.PollutantName == Target]
    d2 = get_PollutantVolume(d1, FirstOrder=FirstOrder)
    d3 = get_PollutantVolume(d1, FirstOrder=FirstOrder)
    if FacilityFocus == True:
        ff = get_PollutantVolume(d1, FirstOrder='FacilityReportID').FacilityReportID.unique()
        db = db[db.FacilityReportID.isin(ff)]
    for items in np.delete(db.PollutantName.unique(), np.argwhere(db.PollutantName.unique() == Target)):
        item = db[db.PollutantName == items].groupby([FirstOrder]).TotalQuantity.sum().reset_index()
        item = item[[FirstOrder, 'TotalQuantity']].rename(columns={'TotalQuantity': items})
        d2 = d2.merge(item, how='left', on=FirstOrder)
        d3[items] = d2.loc[:, items] / d2.loc[:, 'TotalQuantity']

    if Impurity != None:
        d2 = d2[[FirstOrder, 'TotalQuantity', Impurity]]
        d3 = d3[[FirstOrder, 'TotalQuantity', Impurity]]
    if absolute == True:
        return d2
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


def plot_PollutantVolume_rel(db, FirstOrder=None, SecondOrder=None, stacked=False, norm=None, *args, **kwargs):
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
    stacked : Boolean, optional
        Stacks the bars for second order. The default is False.
    norm : variable, optional
        specific first order value, the data is normed to. The default is None. For None it searches the overall maximum.
    *args : TYPE
        pandas.plot() input variables.
    **kwargs : TYPE
        pandas.plot() input variables.

    Returns
    -------
    ax : Axes
        Plot of the data in db, sorted by FirstOrder and SecondOrder if given.

    """
    data = get_PollutantVolume_rel(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder, norm=norm)
    if SecondOrder is None:
        ax = data.plot(x=FirstOrder, y='TotalQuantity', kind='bar', *args, **kwargs)
    else:
        if stacked is True:
            ax = data.plot.bar(x=FirstOrder, stacked=True, *args, **kwargs)
        else:
            ax = data.plot.bar(x=FirstOrder, *args, **kwargs)
    return ax


def plot_ImpurityVolume(db, Target, Impurity, FirstOrder='FacilityReportID', ReleaseMediumName='Air', Statistics=True, *args, **kwargs):
    """
    Plots the impurities for the different FirstOrder values or the statistics of the entries.

    Parameters
    ----------
    db : DataFrame
        The data to be plotted.
    Target : String
        The target pollutant which is impured.
    Impurity : String
        The impurity which is to be analyzed.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is 'FacilityReportID'.
    ReleaseMediumName : TYPE, optional
        The release medium name in which the target is emitted and in which can be impurities. The default is 'Air'.
    Statistics : Boolean, optional
        If this parameter is True, the statistics of the data are plotted. If it is False, the actual values are plotted. The default is True.
    *args : TYPE
        pandas.plot() input variables.
    **kwargs : TYPE
        pandas.plot() input variables.

    Returns
    -------
    ax : Axes
        Plot of the impurities in db, or the statistics of these impurities.

    """
    if Statistics is True:
        data = get_ImpurityVolume(db=db, Target=Target, FirstOrder=FirstOrder, ReleaseMediumName=ReleaseMediumName, Impurity=Impurity).describe()
        ax = data.drop('count').plot(kind='bar', y=Impurity, *args, **kwargs)
    else:
        data = get_ImpurityVolume(db=db, Target=Target, FirstOrder=FirstOrder, ReleaseMediumName=ReleaseMediumName, Impurity=Impurity)
        ax = data.drop('TotalQuantity', axis=1).plot(x=FirstOrder, y=Impurity, kind='bar', *args, **kwargs)
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


def excludeData_NotInBorders(borders, gdf):
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


def add_markersize(gdf, maxmarker):
    """
    adds column markersize to GeoDataFrame. If maxmarker=0, all markers have size 1. Else, they are normalized to max value and multiplied by value of maxmarker.

    Parameters
    ----------
    gdf : GeoDataFrame
        GeoDataFrame, which gets additional column.
    maxmarker : Int
        defines the markersize of the biggest marker. If 0, all markers have same size.

    Returns
    -------
    gdf : GeoDataFrame
        GeoDataFrame with added column 'markersize'.

    """
    gdf['markersize'] = ""
    markernorm = gdf.TotalQuantity.max()
    if maxmarker == 0:
        gdf['markersize'] = 1
    else:
        gdf['markersize'] = gdf['TotalQuantity'] / markernorm * maxmarker
    return gdf


def CreateGDFWithRightProj(dfgdf, outproj=None):
    """
    Converts DataFrame into GeoDataFrame and changes the projection if new projection is given as input.

    Parameters
    ----------
    dfgdf : DataFrame/GeoDataFrame
        Data that is about to be converted into a GeoDataFrame and experience a projection change if wanted.
    outproj : String, optional
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
    if outproj != None:
        gdf = changeproj(gdf, outproj=outproj)
    return(gdf)


def changeproj(gdf, outproj=None):
    """
    Changes The projection of the input GeoDataFrame to the projection defined with outproj. If no CRS is given for the geometry, the function tries to recover information from gdf.

    Parameters
    ----------
    gdf : GeoDataFrame
        Data that CRS is to be changed.
    outproj : Datatype, optional
        Code for target output projection. See http://pyproj4.github.io/pyproj/stable/api/crs/crs.html#pyproj.crs.CRS.from_user_input for input possibilities. The default is None.

    Returns
    -------
    gdf : GeoDataFrame
        Data with new projection in the geometry.

    """
    if outproj == None:
        sys.exit('InputError: For the change of projection is a target projection required.')
    if gdf.crs == None:
        if ('Long' not in gdf.columns or 'Lat' not in gdf.columns):
            sys.exit('InputError: No information about projection of geometry. Define CRS or give coordinates as Long and Lat!')
        gdf = gpd.GeoDataFrame(gdf, geometry=gpd.points_from_xy(gdf.Long, gdf.Lat), crs='EPSG:4326').reset_index(drop=True)
    gdf = gdf.to_crs(crs=outproj)
    return(gdf)


def map_PollutantSource(db, mb, category=None, markersize=0, outproj=None, ReturnMarker=0, *args, **kwargs):
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
    markersize : Int
        maximal size of the largest marker.
    outproj : DataType
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
        gdf = CreateGDFWithRightProj(db, outproj=outproj)
        gdfp = excludeData_NotInBorders(borders=borders, gdf=gdf)[0]
        gdfd = excludeData_NotInBorders(borders=borders, gdf=gdf)[1]
        gdfp = add_markersize(gdfp, maxmarker=markersize)
        ax = gdfp.plot(color='r', zorder=1, markersize=gdfp['markersize'], *args, **kwargs)
    else:
        for items in db[category].unique():
            if not colorlist:
                print('Running out of color')
                break
            color = colorlist[0]
            colorlist.remove(color)
            itemdata = db[db[category] == items].reset_index()
#            itemdata = filter.f_db(db, category=items)
            gdf = CreateGDFWithRightProj(itemdata, outproj=outproj)
            gdfp = excludeData_NotInBorders(borders=borders, gdf=gdf)[0]
            gdfd = excludeData_NotInBorders(borders=borders, gdf=gdf)[1]
            gdfp = add_markersize(gdfp, maxmarker=markersize)
            ax = gdfp.plot(color=color, zorder=1, markersize=gdfp['markersize'], *args, **kwargs)
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
        print('There are multiple NUTS-Levels present in the map data input. This function can not seperate the data in the required way. No Output!')
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
        print('The NUTS-Level of the map data is to high. The geospatial resolution of the emission data is not high enough to differentiate on level 3 regions. Use NUTS-LVL smaller or equal to 2.')
        return None
    db02 = pd.merge(mb, dbpremerge, how='left', on=['NUTS_ID'])
    ax = db02.plot(column='TotalQuantity', *args, **kwargs)

    presentNUTS_IDs = tuple(mb.NUTS_ID.tolist())
    dbp = db01[db01.NUTSRegionGeoCode.str.startswith(presentNUTS_IDs)]
    dbna = db01[~db01.NUTSRegionGeoCode.str.startswith(presentNUTS_IDs)]

    if ReturnMarker == 0:
        return(ax)
    elif ReturnMarker == 1:
        return(dbp)
    else:
        return(dbna)


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
    if (path == None and filename == None):
        print('A filename is required.')
        return None
    elif path == None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
        path = config['PATH']['path']
        path = os.path.join(os.path.join(path, 'ExportData'), filename)
    elif (path != None and filename != None):
        path = os.path.join(path, filename)

    if path.endswith(r'\\') == True:
        print('The file name or path must end with a file type extension')
        return None

    fig.savefig(path, **kwargs)
    return None
