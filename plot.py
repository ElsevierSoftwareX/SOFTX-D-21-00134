# -*- coding: utf-8 -*-
"""
XXX We need a proper description here XXX
Functions for pickle editing
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import geopandas
import filter


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
            d = {'Order': ['NoneGiven'], 'TotalQuantity':[db.TotalQuantity.sum()]}
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
    SecondOrder : TYPE, optional
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


def plot_PollutantVolume(db, FirstOrder=None, SecondOrder=None, stacked=False):
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

    Returns
    -------
    Plot

    """
    data = get_PollutantVolume(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder)
    if SecondOrder is None:
        data.plot(x=FirstOrder, y='TotalQuantity', kind='bar')
    else:
        if stacked is True:
            data.plot.bar(x=FirstOrder, stacked=True)
        else:
            data.plot.bar(x=FirstOrder)


def plot_PollutantVolumeChange(db, FirstOrder=None, SecondOrder=None, stacked=False):
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

    Returns
    -------
    Plot

    """
    data = get_PollutantVolumeChange(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder)
    if SecondOrder is None:
        data.plot(x=FirstOrder, y='TotalQuantityChange', kind='bar')
    else:
        if stacked is True:
            data.plot.bar(x=FirstOrder, stacked=True)
        else:
            data.plot.bar(x=FirstOrder)


def plot_PollutantVolume_rel(db, FirstOrder=None, SecondOrder=None, stacked=False, norm=None):
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

    Returns
    -------
    Plot

    """
    data = get_PollutantVolume_rel(db, FirstOrder=FirstOrder, SecondOrder=SecondOrder, norm=norm)
    if SecondOrder is None:
        data.plot(x=FirstOrder, y='TotalQuantity', kind='bar')
    else:
        if stacked is True:
            data.plot.bar(x=FirstOrder, stacked=True)
        else:
            data.plot.bar(x=FirstOrder)


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
    gdff = geopandas.GeoDataFrame(columns=gdf.columns)
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


def map_PollutantSource(db, mb, category=None, markersize=0):
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

    Returns
    -------
    Plot with pollutant sources on map.

    """
#color selecting is bad.
#Calling gdfp, gdfd requires 2 times performing the function, perhaps better way.
    ax = mb.plot(zorder=1)
    colorlist = ['r', 'y', 'g', 'c', 'm', 'b']
    borders = get_mb_borders(mb)
    if category is None:
        gdf = geopandas.GeoDataFrame(db, geometry=geopandas.points_from_xy(db.Long, db.Lat)).reset_index(drop=True)
        gdfp = excludeData_NotInBorders(borders=borders, gdf=gdf)[0]
        gdfd = excludeData_NotInBorders(borders=borders, gdf=gdf)[1] 
        gdfp = add_markersize(gdfp, maxmarker=markersize)
        ax = gdfp.plot(ax=ax, color='r', zorder=1, markersize=gdfp['markersize'])
    else:
        for items in db[category].unique():
            if not colorlist:
                print('Running out of color')
                break
            color = colorlist[0]
            colorlist.remove(color)
            itemdata = db[db[category] == items].reset_index()
#            itemdata = filter.f_db(db, category=items)
            gdf = geopandas.GeoDataFrame(itemdata, geometry=geopandas.points_from_xy(itemdata.Long, itemdata.Lat))
            gdfp = excludeData_NotInBorders(borders=borders, gdf=gdf)[0]
            gdfd = excludeData_NotInBorders(borders=borders, gdf=gdf)[1]
            gdfp = add_markersize(gdfp, maxmarker=markersize)
            ax = gdfp.plot(ax=ax, color=color, zorder=1, markersize=gdfp['markersize'])
    if gdfd.empty == False:
        print('Some data points are out of borders')
    else:
        print('All data points are within rectangular borders')
    return(gdfp,gdfd)
    
    