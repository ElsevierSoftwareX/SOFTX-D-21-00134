# -*- coding: utf-8 -*-
"""
Testing area.
Maybe template for init file.
"""

#testing area
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import geopandas
import filter
import plot
import rawdata
import time
import csv


"""
setup area initiation:
"""

path = 'C:\\Witthaut\\Daten\\test1'
# rawdata.download_PollutionData(path=path)
# rawdata.download_MapFiles(path=path)
# rawdata.download_postalcode_NUTS_transition(path=path)
# rawdata.pickle_rawdata(path=path, force_rerun = True)
# rawdata.merge_frompickle(path=path, force_rerun = True)

"""
setup area data tables:
"""
path = 'C:\\Witthaut\\Daten\\test1'
#db = filter.read_db(path)

# Countrylist = ['Germany']
# Pollutantlist = ['Carbon dioxide (CO2)']
# Pollutantlist = ['Methane (CH4)', 'Carbon dioxide (CO2)']
# ReportingYear = [2017]
# NUTS_ID = ['DE92']
# data = filter.f_db(db, CountryName=Countrylist, PollutantName=Pollutantlist, ReportingYear=ReportingYear)


"""
setup area map table loading:
"""
# NUTS_LVL = '3'
# Resolution = '01M'
# datatype = 'shp'
# projection = '4326'
# spatialtype = 'RG'
# m_year = '2021'


"""
loading map table:
"""
# mb = filter.read_mb(path=path, Resolution=Resolution, spatialtype=spatialtype, NUTS_LVL=NUTS_LVL, m_year=m_year, projection=projection)

# CNTR_CODE = ['DE']
# NUTS_ID = ['DE92']
# mapdata = filter.f_mb(mb, CNTR_CODE=CNTR_CODE)


"""
testing functions area:
"""


































"""
Function for merging, to check for NUTS3 Code:


fr = pd.read_pickle(os.path.join(path, 'PollutionData\\fr.pkl'))
pr = pd.read_pickle(os.path.join(path, 'PollutionData\\pr.pkl'))
pratr = pd.read_pickle(os.path.join(path, 'PollutionData\\pratr.pkl'))

db01 = pd.merge(fr, pratr, on=['PollutantReleaseAndTransferReportID', 'CountryName', 'CountryCode'])
db02 = pd.merge(db01, pr, on=['FacilityReportID', 'ConfidentialIndicator', 'ConfidentialityReasonCode', 'ConfidentialityReasonName'], how='right')

df = pd.DataFrame()
for item in os.listdir(os.path.join(path, 'PostalCode_NUTS')):
    if item.endswith('.pkl'):
        print(item)
        item_data = pd.read_pickle(os.path.join(os.path.join(path, 'PostalCode_NUTS'), item))
        # some PostalCodes are present multiple times, drop for each item, because countrys may use same postal code
        item_data = item_data.drop_duplicates(subset=['CODE'])
        df = pd.concat([df, item_data])
df = df.rename(columns={'CODE': 'PostalCode'})
df['CountryCode'] = df['NUTS3'].str[1:3]
df.PostalCode = df['PostalCode'].str[1:-1]
df.NUTS3 = df['NUTS3'].str[1:-1]


db = pd.merge(db02, df, how='left', on=['PostalCode', 'CountryCode'])

test1 = db[db.NUTS3.isna()]
test2 = db[db.PostalCode.isna()]
"""
# mapdata.plot()

# countrylist = mapping.get_CNTR_CODE_list(mb)
# lines=plot.map_PollutantSource(data, mapdata, markersize=0)
# lines=plot.map_PollutantSource(data, mapdata,markersize=50, category='ReportingYear')[0]


# a=plot.get_PollutantVolume(data, FirstOrder='ReportingYear')
# a=plot.get_PollutantVolume(data, FirstOrder='ReportingYear', SecondOrder='CountryName')
# b=plot.get_PollutantVolumeChange(data, FirstOrder='ReportingYear')
# c=plot.get_PollutantVolume_rel(data, FirstOrder='ReportingYear',norm=2013)
# c=plot.get_PollutantVolume_rel(data, FirstOrder='ReportingYear', SecondOrder='CountryName')
# b=plot.get_PollutantVolumeChange(data, FirstOrder='ReportingYear', SecondOrder='CountryName')
# plot.plot_PollutantVolume(data, FirstOrder='ReportingYear', SecondOrder='CountryName', stacked=True)
# plot.plot_PollutantVolume(data,FirstOrder='ReportingYear')
# plot.plot_PollutantVolume_rel(data, FirstOrder='ReportingYear', SecondOrder='CountryName', stacked=False)
# plot.plot_PollutantVolume_hist(data, FirstOrder='ReportingYear')


""" testing merge routine
fr = pd.read_pickle(os.path.join(path, 'PollutionData\\fr.pkl'))
pr = pd.read_pickle(os.path.join(path, 'PollutionData\\pr.pkl'))
pratr = pd.read_pickle(os.path.join(path, 'PollutionData\\pratr.pkl'))

db01 = pd.merge(fr, pratr, on=['PollutantReleaseAndTransferReportID', 'CountryName', 'CountryCode'])
db02 = pd.merge(db01, pr, on=['FacilityReportID', 'ConfidentialIndicator' , 'ConfidentialityReasonCode', 'ConfidentialityReasonName'], how='right')



df = pd.DataFrame(columns={'PostalCode', 'NUTSID', 'CountryCode'})
start2 = time.time()
for item in os.listdir(os.path.join(path, 'PostalCode_NUTS')):
    if ('at' in item):
        if item.endswith('.pkl'):
            start1 = time.time()
            print(item)
            item_data = pd.read_pickle(os.path.join(os.path.join(path, 'PostalCode_NUTS'), item))
            dict = {}
            for i in range(len(item_data)):
                dict[i] = {'NUTSID': item_data.iloc[i][0][1:6], 'PostalCode': item_data.iloc[i][0][9:-1], 'CountryCode': item_data.iloc[i][0][1:3]}
                #dict[i] = {'NUTSID': item_data.iloc[i][0][1:item_data.iloc[i][0].find(';') - 1], 'PostalCode': item_data.iloc[i][0][item_data.iloc[i][0].find(';') + 2:-1], 'CountryCode': item_data.iloc[i][0][1:3]}
            item_df = pd.DataFrame.from_dict(dict, 'index')
            item_df = item_df.drop_duplicates(subset=['PostalCode'])
            end1 = time.time()
            print(end1 - start1)
            df = pd.concat([df, item_df])
db = pd.merge(db02, df, how='left', on=['PostalCode', 'CountryCode'])
end2 = time.time()
print(end2 - start2)
"""

# test1 = filter.f_db(db, CountryName='Austria')
# test2 = test1[test1.NUTSID.notna()]
# test3 = test1[test1.NUTSID.isna()]
# test4 = pd.DataFrame.from_dict(dict, 'index')
# test6 = test3.PostalCode.unique()
# test7 = test3[test3.ReportingYear == 2017]
# test8 = test3[test3.ReportingYear != 2017]
""" speed test for dict method for merge
start = time.time()
dict = {}
for i in range(len(item_data)):
    dict[i] = {'NUTSID': item_data.iloc[i][0][:item_data.iloc[i][0].find(';')], 'PostalCode': item_data.iloc[i][0][item_data.iloc[i][0].find(';') + 1:]}
df = pd.DataFrame.from_dict(dict, 'index')
end = time.time()
print(end-start)
"""

""" speed test for append method for merge
start = time.time()
df = pd.DataFrame(columns={'PostalCode', 'NUTSID'})
for i in range(len(item_data)):
    df = df.append({'NUTSID': item_data.iloc[i][0][:item_data.iloc[i][0].find(';')], 'PostalCode': item_data.iloc[i][0][item_data.iloc[i][0].find(';') + 1:]}, ignore_index=True)
end = time.time()
print(end-start)
"""
