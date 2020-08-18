# -*- coding: utf-8 -*-
"""
Testing area.
Maybe template for init file.
"""


import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import filter
import plot
import rawdata
import time
import csv


timeline = []
timeline.append(time.time())

"""
setup area initiation:
"""

path = 'C:\\Witthaut\\Daten\\test2'
#rawdata.download_PollutionData(path=path)
#rawdata.download_MapFiles(path=path)
#rawdata.download_postalcode_NUTS_transition(path=path)
#rawdata.pickle_rawdata(path=path, force_rerun = True)
#rawdata.merge_frompickle(path=path, force_rerun = True)
timeline.append(time.time())
"""
setup area data tables:
"""


path = 'C:\\Witthaut\\Daten\\test2'
db = filter.read_db(path)
#db = filter.f_db(db, ExclaveExclude=True)[0]
timeline.append(time.time())

Countrylist = ['Germany']
Pollutantlist = ['Carbon dioxide (CO2)']
#Pollutantlist = ['Methane (CH4)', 'Carbon dioxide (CO2)']
ReportingYear = [2017]
# NUTSRegionGeoCode = ['DE92']
data = filter.f_db(db, CountryName=Countrylist, PollutantName=Pollutantlist, ReportingYear=ReportingYear)[0]

timeline.append(time.time())
"""
setup area map table loading:
"""
NUTS_LVL = '3'
Resolution = '01M'
datatype = 'shp'
projection = '4326'
spatialtype = 'RG'
m_year = '2021'


"""
loading map table:
"""
mb = filter.read_mb(path=path, Resolution=Resolution, spatialtype=spatialtype, NUTS_LVL=NUTS_LVL, m_year=m_year, projection=projection)
mb = filter.f_mb(mb, ExclaveExclude=True)

CNTR_CODE = ['DE']
NUTS_ID = ['DE92']
mapdata = filter.f_mb(mb, CNTR_CODE=CNTR_CODE)

timeline.append(time.time())

"""
testing functions area:
"""



























""" Take a look at NUTS3 assignment
gdf = gpd.GeoDataFrame(db, geometry=gpd.points_from_xy(db.Long, db.Lat)).reset_index(drop=True).set_crs('EPSG:4326')

timeline.append(time.time())

gdf1 = gpd.sjoin(gdf, mb, how='left')

timeline.append(time.time())

gdf1 = gdf1.drop(['index_right', 'FID', 'LEVL_CODE', 'CNTR_CODE', 'NAME_LATN', 'NUTS_NAME', 'MOUNT_TYPE', 'URBN_TYPE', 'COAST_TYPE', 'FID'], axis=1)

timeline.append(time.time())

test1 = gdf1[gdf1.NUTS_ID.isna()]
test2 = gdf1[gdf1.NUTS_ID.notna()]
test3 = test2[test2.NUTS_ID == test2['NUTS3']]
test4 = test2[test2.NUTS_ID != test2['NUTS3']]
test5 = gdf1[gdf1.NUTS3.notna()]
test6 = gdf1[gdf1.NUTS3.isna()]
test7 = test4[test4.NUTS3.notna()]

"""


"""testing map_pollutantregions
#fig1, fig1_axes = plt.subplots(1,1)
#fig1_axes[0,0] = plot.map_PollutantRegions(data, mapdata, ax=fig1_axes[0,0])
#plt.show

fig2 = plt.figure()
ax1 = fig2.add_subplot(1, 1, 1)
ax1 = plot.map_PollutantRegions(data, mapdata, ax=ax1, legend=True, missing_kwds={'color': 'lightgrey'})
plt.show
"""




"""plotting the bars
fig1, fig1_axes = plt.subplots(2, 2)
fig1_axes[0,0] = plot.plot_PollutantVolume(data, FirstOrder='ReportingYear', ax=fig1_axes[0,0])
fig1_axes[1,0] = plot.plot_PollutantVolume_rel(data, FirstOrder='ReportingYear', ax=fig1_axes[1,0])
fig1_axes[0,1] = plot.plot_PollutantVolumeChange(data, FirstOrder='ReportingYear', ax=fig1_axes[0,1])
fig1_axes[1,1] = plot.plot_PollutantVolume(data, FirstOrder='ReportingYear', ax=fig1_axes[1,1], color='r')
plt.show()
"""


"""testing exclavefilter
test1 = filter.f_db(db, CountryName='Spain', ExclaveExclude=True)[0]
test2 = filter.f_db(db, CountryName='Spain', ExclaveExclude=True)[1]
test3 = filter.f_mb(mb, ExclaveExclude=True)
"""

"""testing advanced plotting
plt.ioff()

fig1, fig1_axes = plt.subplots(2, 2)

fig1_axes[0,0] = plot.map_PollutantSource(data, mapdata, category='PollutantName', ax=fig1_axes[0, 0])[0]
fig1_axes[0,0].set_xlabel('Longitude')
fig1_axes[0,0].set_ylabel('Latitude')
fig1_axes[0,0].set_title('CO2 and Methane Sources')
fig1_axes[0,1] = mapdata.plot(ax=fig1_axes[0,1])
fig1_axes[1,0] = mb.plot(ax=fig1_axes[1,0])
fig1_axes[1,1] = mb.plot(ax=fig1_axes[1,1], color='r')
fig1_axes[1,0].set_ylim(40,80)
fig1_axes[0,0].collections[1].set_color('g')

timeline.append(time.time())

fig2 = plt.figure()
ax1 = fig2.add_subplot(1, 1, 1)
ax1 = mb.plot(ax=ax1, color='lightgrey')
ax1 = plot.map_PollutantSource(data, mapdata, ax=ax1)[0]

plt.show()
"""
timeline.append(time.time())




print(timeline[1]-timeline[0])
print(timeline[2]-timeline[1])
print(timeline[3]-timeline[2])
print(timeline[4]-timeline[3])
print(timeline[5]-timeline[4])
#print(timeline[6]-timeline[5])
#print(timeline[7]-timeline[6])
#print(timeline[8]-timeline[7])


#plot.plot_PollutantVolume(data, FirstOrder='ReportingYear', SecondOrder='CountryName')
#plot.map_PollutantSource(data, mapdata, markersize=0, category='PollutantName')


#db03 = db[db.NUTS3.isna()]
#gdf = geopandas.GeoDataFrame(db03, geometry=geopandas.points_from_xy(db03.Long, db03.Lat)).reset_index(drop=True)
#pointin = geopandas.sjoin(gdf, mb, how='left')
#pointin = pointin.drop(['NUTS3', 'index_right', 'FID', 'LEVL_CODE', 'CNTR_CODE', 'NAME_LATN', 'NUTS_NAME', 'MOUNT_TYPE', 'URBN_TYPE', 'COAST_TYPE', 'FID'], axis=1)


#db02 = db[db.NUTS3.notna()]
#gdf = geopandas.GeoDataFrame(db02, geometry=geopandas.points_from_xy(db02.Long, db02.Lat)).reset_index(drop=True)
#pointin = geopandas.sjoin(gdf, mb, how='left')
#pointin = pointin.drop(['index_right', 'FID', 'LEVL_CODE', 'CNTR_CODE', 'NAME_LATN', 'NUTS_NAME', 'MOUNT_TYPE', 'URBN_TYPE', 'COAST_TYPE', 'FID'], axis=1)
