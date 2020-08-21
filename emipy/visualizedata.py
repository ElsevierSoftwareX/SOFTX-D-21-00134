# -*- coding: utf-8 -*-
"""
This module contains all functions to visualize the data set.
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import processdata


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
        The change of TotalQuantity  to the previous data entry

    """
    data = get_PollutantVolume(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder)
    if SecondOrder is None:
        data = data.rename(columns={'TotalQuantity': 'TotalQuantityChange'})
    for items in data.columns:
        if items != FirstOrder:
            data[items] = data[items].diff()
    return data


def plot_PollutantVolume(db, FirstOrder=None, SecondOrder=None, stacked=False, *args, **kwargs):
    """

    Plots the filtered data set. The first order is the x-axis, the second order is a differentiation of the y-values.

    Parameters
    ----------
    db : DataFrame
        DESCRIPTION.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is None.
    SecondOrder : String, optional
        Name of column, the data are sorted in the second order.. The default is None.
    stacked : Boolean, optional
        Stacks the bars for second order. The default is False.
    *args : TYPE
        Geopandas.plot() input variables.
    **kwargs : TYPE
        Geopandas.plot() input variables.

    Returns
    -------
    Plot

    """
    data = get_PollutantVolume(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder)
    if SecondOrder is None:
        ax = data.plot(x=FirstOrder, y='TotalQuantity', kind='bar', *args, **kwargs)
    else:
        if stacked is True:
            ax = data.plot.bar(x=FirstOrder, stacked=True, *args, **kwargs)
        else:
            ax = data.plot.bar(x=FirstOrder, *args, **kwargs)
    return(ax)

def plot_PollutantVolumeChange(db, FirstOrder=None, SecondOrder=None, stacked=False, *args, **kwargs):
    """
    Plots the volume change of the data set. The first order is the x-axis, the second order is a differentiation of the y-values.

    Parameters
    ----------
    db : DataFrame
        DESCRIPTION.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is None.
    SecondOrder : String, optional
        Name of column, the data are sorted in the second order.. The default is None.
    stacked : Boolean, optional
        Stacks the bars for second order. The default is False.
    *args : TYPE
        Geopandas.plot() input variables.
    **kwargs : TYPE
        Geopandas.plot() input variables.

    Returns
    -------
    Plot

    """
    data = get_PollutantVolumeChange(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder)
    if SecondOrder is None:
        ax = data.plot(x=FirstOrder, y='TotalQuantityChange', kind='bar', *args, **kwargs)
    else:
        if stacked is True:
            ax = data.plot.bar(x=FirstOrder, stacked=True, *args, **kwargs)
        else:
            ax = data.plot.bar(x=FirstOrder, *args, **kwargs)
    return(ax)


def plot_PollutantVolume_rel(db, FirstOrder=None, SecondOrder=None, stacked=False, norm=None, *args, **kwargs):
    """
    Plots the normed pollutant volume of the data set, The first order is the x-axis, the second order is a differentiation of the y-values.

    Parameters
    ----------
    db : DataFrame
        DESCRIPTION.
    FirstOrder : String, optional
        Name of column, the data are sorted in the first order. The default is None.
    SecondOrder : String, optional
        Name of column, the data are sorted in the second order.. The default is None.
    stacked : Boolean, optional
        Stacks the bars for second order. The default is False.
    norm : variable, optional
        specific first order value, the data is normed to. The default is None. For None it searches the overall maximum.
    *args : TYPE
        Geopandas.plot() input variables.
    **kwargs : TYPE
        Geopandas.plot() input variables.

    Returns
    -------
    Plot

    """
    data = get_PollutantVolume_rel(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder, norm=norm)
    if SecondOrder is None:
        data.plot(x=FirstOrder, y='TotalQuantity', kind='bar', *args, **kwargs)
    else:
        if stacked is True:
            data.plot.bar(x=FirstOrder, stacked=True, *args, **kwargs)
        else:
            data.plot.bar(x=FirstOrder, *args, **kwargs)


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

def excludeData_NotInBorders(borders,gdf):
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
    [1] GeoDataFrame with data inside the borders. [2] GeoDataFrame with data outside the borders.

    """
    gdft = gdf
    gdff = gpd.GeoDataFrame(columns=gdf.columns)
    gdff['geometry'] = ""
    for i in range(len(gdf)):
        if (gdf.geometry.iloc[i].x < borders[0]) or (gdf.geometry.iloc[i].x > borders[2]) or (gdf.geometry.iloc[i].y < borders[1]) or (gdf.geometry.iloc[i].y > borders[3]):
            gdff = gdff.append(gdf.iloc[i])
            gdft = gdft.drop([i], axis=0)
    return(gdft, gdff)


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


def map_PollutantSource(db, mb, category=None, markersize=0, *args, **kwargs):
    """
    maps pollutant sources given by db on map given by mb.

    Parameters
    ----------
    db : DataFrame
        Data table on pollutant sources.
    mb : DataFrame
        geo data table.
    category : String
        The column name of db, which gets new colors for every unique entry.
    markersize : Int
        maximal size of the largest marker.
    *args : TYPE
        Geopandas.plot() input variables.
    **kwargs : TYPE
        Geopandas.plot() input variables.

    Returns
    -------
    ax : Axes
        Plot with pollutant sources on map.
    gdfp : GeoDataFrame
        GeoDataFrame with all sources that are within geo borders and therefore plotted.
    gdfd : GeoDataFrame
        GeoDataFrame with all sources that are outside geo borders and there fore

    """
# color selecting is bad.
# Calling gdfp, gdfd requires 2 times performing the function, perhaps better way.
    ax = mb.plot(zorder=1, *args, **kwargs)
    colorlist = ['r', 'y', 'g', 'c', 'm', 'b']
    borders = get_mb_borders(mb)
    if category is None:
        gdf = gpd.GeoDataFrame(db, geometry=gpd.points_from_xy(db.Long, db.Lat)).reset_index(drop=True)
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
            gdf = gpd.GeoDataFrame(itemdata, geometry=gpd.points_from_xy(itemdata.Long, itemdata.Lat))
            gdfp = excludeData_NotInBorders(borders=borders, gdf=gdf)[0]
            gdfd = excludeData_NotInBorders(borders=borders, gdf=gdf)[1]
            gdfp = add_markersize(gdfp, maxmarker=markersize)
            ax = gdfp.plot(color=color, zorder=1, markersize=gdfp['markersize'], *args, **kwargs)
    if gdfd.empty is False:
        print('Some data points are out of borders')
    else:
        print('All data points are within rectangular borders')
    return(ax, gdfp, gdfd)


def map_PollutantRegions(db, mb, *args, **kwargs):
    """
    Visualizes the pollutant emission of regions with a color map. The classification of regions is selected with the choice of mb.

    Parameters
    ----------
    db : DataFrame
        Pollution data that are plotted.
    mb : TYPE
        Map data for plotting. The region selection corresponds to the selection of mb.
    *args : TYPE
        Geopandas.plot() input variables.
    **kwargs : TYPE
        Geopandas.plot() input variables.

    Returns
    -------
    ax : Axes
        Axes with colormap of the pollution emission.

    """
    db01 = get_PollutantVolume(db, FirstOrder='NUTSRegionGeoCode')
    db01 = db01.rename(columns={'NUTSRegionGeoCode': 'NUTS_ID'})
    db02 = pd.merge(mb, db01, how='left', on=['NUTS_ID'])
    ax = db02.plot(column='TotalQuantity', *args, **kwargs)
    return(ax)
