# -*- coding: utf-8 -*-
"""
XXX We need a proper description here XXX
addapted rawdataversion to work with data, that are not located in folder of the scripts
"""

import pandas as pd
import os
from os.path import join, isfile
import matplotlib.pyplot as plt
import requests, zipfile, io
import csv


def download_PollutionData(path, chunk_size=128):
    """
    Downloads the pollution data into given path.

    Parameters
    ----------
    path : String
        Path to the root of the project.
    chunk_size : TYPE, optional
        DESCRIPTION. The default is 128.

    Returns
    -------
    None.

    """
    directory = 'PollutionData'
    path = os.path.join(path, directory)
    if os.path.isdir(path) is False:
        os.mkdir(path)
    if not os.listdir(path):
        url = 'https://www.eea.europa.eu/data-and-maps/data/member-states-reporting-art-7-under-the-european-pollutant-release-and-transfer-register-e-prtr-regulation-23/european-pollutant-release-and-transfer-register-e-prtr-data-base/eprtr_v9_csv.zip/at_download/file'
        r = requests.get(url, stream=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(path)


def download_MapFiles(path, chunk_size=128):
    """
    Download shp files to given path

    Parameters
    ----------
    path : String
        Path to the root of the project.
    chunk_size : TYPE, optional
        DESCRIPTION. The default is 128.

    Returns
    -------
    None.

    """
    directory = 'MappingData'
    path = os.path.join(path, directory)
    if os.path.isdir(path) is False:
        os.mkdir(path)
    if not os.listdir(path):
        # It might be better to feed the process for each link in order to reuse cache
        url1 = 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2021-01m.shp.zip'
        url3 = 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2021-03m.shp.zip'
        url10 = 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2021-10m.shp.zip'
        url20 = 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2021-20m.shp.zip'
        url60 = 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2021-60m.shp.zip'
        r1 = requests.get(url1, stream=True)
        r3 = requests.get(url3, stream=True)
        r10 = requests.get(url10, stream=True)
        r20 = requests.get(url20, stream=True)
        r60 = requests.get(url60, stream=True)
        z1 = zipfile.ZipFile(io.BytesIO(r1.content))
        z3 = zipfile.ZipFile(io.BytesIO(r3.content))
        z10 = zipfile.ZipFile(io.BytesIO(r10.content))
        z20 = zipfile.ZipFile(io.BytesIO(r20.content))
        z60 = zipfile.ZipFile(io.BytesIO(r60.content))
        z1.extractall(path)
        z3.extractall(path)
        z10.extractall(path)
        z20.extractall(path)
        z60.extractall(path)
        extension = '.zip'
        os.chdir(path)
        for item in os.listdir(path):
            if item.endswith(extension):
                file_name = os.path.abspath(item)
                zip_ref = zipfile.ZipFile(file_name)
                zip_ref.extractall(path)
                zip_ref.close()
                os.remove(file_name)


def download_postalcode_NUTS_transition(path, chunk_size=128):
    """
    Download csv files for postal code to NUTS code transition to given path.

    Parameters
    ----------
    path : String
        Path to the root of the project.
    chunk_size : TYPE, optional
        DESCRIPTION. The default is 128.

    Returns
    -------
    None.

    """
    directory = 'PostalCode_NUTS'
    path = os.path.join(path, directory)
    if os.path.isdir(path) is False:
        os.mkdir(path)
    if not os.listdir(path):
        url = 'https://gisco-services.ec.europa.eu/tercet/NUTS-2021/pc2020_NUTS-2021_v1.0.zip'
        r = requests.get(url, stream=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(path)
        extension = '.zip'
        os.chdir(path)
        for item in os.listdir(path):
            if item.endswith(extension):
                file_name = os.path.abspath(item)
                zip_ref = zipfile.ZipFile(file_name)
                zip_ref.extractall(path)
                zip_ref.close()
                os.remove(file_name)
    for item in os.listdir(path):
        if item.endswith('.csv'):
            with open(os.path.join(path,item)) as filein:
                with open(os.path.join(path, item[:-3])+'edit'+'.csv', 'w') as fileout:
                    for line in filein.readlines():
                        fileout.write(line.replace(';', ','))


def pickle_rawdata(path, force_rerun=False):
    """
    loads files of interest, converts them into .pkl file and saves them in the same path.

    Parameters
    ----------
    path : String
        Path to the root of the project.
    force_rerun : Boolean, optional
        If true, the function executes the routine even if the destination folder already contains corresponding files.. The default is False.

    Returns
    -------
    None.

    """
    # POLLUTANTRELEASEANDTRANSFERREPORT
    if ((os.path.isfile(os.path.join(path, 'PollutionData\\pratr.pkl')) is False) or force_rerun):
        pratr = pd.read_csv(os.path.join(path, 'PollutionData\\dbo.PUBLISH_POLLUTANTRELEASEANDTRANSFERREPORT.csv'))
        pratr.to_pickle(os.path.join(path, 'PollutionData\\pratr.pkl'))

    # FACILITYREPORT
    if ((os.path.isfile(os.path.join(path, 'PollutionData\\fr.pkl')) is False) or force_rerun):
        fr = pd.read_csv(os.path.join(path, 'PollutionData\\dbo.PUBLISH_FACILITYREPORT.csv'), encoding='latin-1', low_memory=False)
        fr.to_pickle(os.path.join(path, 'PollutionData\\fr.pkl'))

    # POLLUTANTRELEASE
    if ((os.path.isfile(os.path.join(path, 'PollutionData\\pr.pkl')) is False) or force_rerun):
        pr = pd.read_csv(os.path.join(path, 'PollutionData\\dbo.PUBLISH_POLLUTANTRELEASE.csv'), low_memory=False)
        pr.to_pickle(os.path.join(path, 'PollutionData\\pr.pkl'))

    # NUTS_Code
    for item in os.listdir(os.path.join(path, 'PostalCode_NUTS')):
        if (os.path.isfile(os.path.join(os.path.join(path, 'PostalCode_NUTS'), (item[:-3] + '.pkl'))) is False) or force_rerun:
            if item.endswith('edit.csv'):
                item_data = pd.read_csv(os.path.join(os.path.join(path, 'PostalCode_NUTS'), item), low_memory=False, sep=',')
                #if len(item_data.columns) == 1:
                #    item_data = pd.read_csv(os.path.join(os.path.join(path, 'PostalCode_NUTS'), item), low_memory=False, sep=',')
                item_data.to_pickle(os.path.join(os.path.join(path, 'PostalCode_NUTS'), (item[:-3] + '.pkl')))

    return None


def merge_frompickle(path, force_rerun=False):
    """
    Inserts tables with different data into each other.

    Parameters
    ----------
    path : String
        Path to the root of the project.
    force_rerun : Boolean, optional
        If true, the function executes the routine even if the destination folder already contains corresponding files.. The default is False.

    Returns
    -------
    None.

    """
    if (os.path.isfile(os.path.join(path, 'PollutionData\\db.pkl')) is False) or force_rerun:
        try:
            fr = pd.read_pickle(os.path.join(path, 'PollutionData\\fr.pkl'))
            pr = pd.read_pickle(os.path.join(path, 'PollutionData\\pr.pkl'))
            pratr = pd.read_pickle(os.path.join(path, 'PollutionData\\pratr.pkl'))
        except FileNotFoundError:
            print('Error. Run function pickle_rawdata')
        # speed difference for variing merge-order?? Table length differs, merge smart enough to add multiple one row to multiple?
        # problematic to merge by multiple coloum names?
        # Some data have no PostalCode, wrong fomrated postal code or not actual PostalCode
        db01 = pd.merge(fr, pratr, on=['PollutantReleaseAndTransferReportID', 'CountryName', 'CountryCode'])
        db02 = pd.merge(db01, pr, on=['FacilityReportID', 'ConfidentialIndicator', 'ConfidentialityReasonCode', 'ConfidentialityReasonName'])
        df = pd.DataFrame()
        for item in os.listdir(os.path.join(path, 'PostalCode_NUTS')):
            if item.endswith('.pkl'):
                item_data = pd.read_pickle(os.path.join(os.path.join(path, 'PostalCode_NUTS'), item))
                # some PostalCodes are present multiple times
                item_data = item_data.drop_duplicates(subset=['CODE'])
                df = pd.concat([df, item_data])
        df = df.rename(columns={'CODE': 'PostalCode'})
        df['CountryCode'] = df['NUTS3'].str[1:3]
        df.PostalCode = df['PostalCode'].str[1:-1]
        df.NUTS3 = df['NUTS3'].str[1:-1]
        db = pd.merge(db02, df, how='left', on=['PostalCode', 'CountryCode'])
        db.to_pickle(os.path.join(path, 'PollutionData\\db.pkl'))


    return None

    """
        df = pd.DataFrame(columns={'PostalCode', 'NUTSID', 'CountryCode'})
        for item in os.listdir(os.path.join(path, 'PostalCode_NUTS')):
            if item.endswith('.pkl'):
                item_data = pd.read_pickle(os.path.join(os.path.join(path, 'PostalCode_NUTS'), item))
                dict = {}
                for i in range(len(item_data)):
                    #additional column CountryCode is needed, because PostalCodes can exists in multiple countrys. Comment line is more general but slower and this function takes about 15 minutes (UK has 1.7 million different postal codes.)
                    dict[i] = {'NUTSID': item_data.iloc[i][0][1:6], 'PostalCode': item_data.iloc[i][0][9:-1], 'CountryCode': item_data.iloc[i][0][1:3]}
                    #dict[i] = {'NUTSID': item_data.iloc[i][0][1:item_data.iloc[i][0].find(';') - 1], 'PostalCode': item_data.iloc[i][0][item_data.iloc[i][0].find(';') + 2:-1], 'CountryCode': item_data.iloc[i][0][1:3]}
                item_df = pd.DataFrame.from_dict(dict, 'index')
                #following line is needed because some postal codes exist multiple times (Germany). Could there be a reason??
                item_df = item_df.drop_duplicates(subset=['PostalCode'])
                df = pd.concat([df, item_df])
    """