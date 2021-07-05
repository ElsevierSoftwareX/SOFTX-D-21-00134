# -*- coding: utf-8 -*-
"""
This module contains all functions, necessary for the inititation of an emipy project.
"""

import pandas as pd
import os

import requests
import zipfile
import io

import configparser
import urllib.request

path_sep = os.sep


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
        url = ('https://www.eea.europa.eu/data-and-maps/data/' +
               'member-states-reporting-art-7-under-the-european-pollutant' +
               '-release-and-transfer-register-e-prtr-regulation-23/european-' +
               'pollutant-release-and-transfer-register-e-prtr-data-base/eprtr_v9_csv.zip/at_download/file')
        r = requests.get(url, stream=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(path)


def download_MapData(path, resolution=10, clear=False, chunk_size=128):
    """
    Download shp files to given path

    Parameters
    ----------
    path : String
        Path to the root of the project.
    resolution : int/list, optional
        Defines the resolution, that the downloaded maps have. Selectable are 1,3,10,20,60. The default is 10.
    clear : Boolean
        If put on True, the function clears the MappingData Directory, before downloading the data., The default is False.
    chunk_size : TYPE, optional
        DESCRIPTION. The default is 128.

    Returns
    -------
    None.

    """
    oldcwd = os.getcwd()
    directory = 'MappingData'
    path = os.path.join(path, directory)

    try:
        if os.path.isdir(path) is False:
            os.mkdir(path)

        if clear:
            os.chdir(path)
            for item in os.listdir(path):
                file_name = os.path.abspath(item)
                os.remove(file_name)

        urldict = {
            202101: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2021-01m.shp.zip',
            202103: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2021-03m.shp.zip',
            202110: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2021-10m.shp.zip',
            202120: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2021-20m.shp.zip',
            202160: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2021-60m.shp.zip',

            201601: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2016-01m.shp.zip',
            201603: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2016-03m.shp.zip',
            201610: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2016-10m.shp.zip',
            201620: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2016-20m.shp.zip',
            201660: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2016-60m.shp.zip',

            201301: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2013-01m.shp.zip',
            201303: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2013-03m.shp.zip',
            201310: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2013-10m.shp.zip',
            201320: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2013-20m.shp.zip',
            201360: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2013-60m.shp.zip',

            201001: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2010-01m.shp.zip',
            201003: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2010-03m.shp.zip',
            201010: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2010-10m.shp.zip',
            201020: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2010-20m.shp.zip',
            201060: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2010-60m.shp.zip',

            200601: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2006-01m.shp.zip',
            200603: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2006-03m.shp.zip',
            200610: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2006-10m.shp.zip',
            200620: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2006-20m.shp.zip',
            200660: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2006-60m.shp.zip',

            200301: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2003-01m.shp.zip',
            200303: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2003-03m.shp.zip',
            200310: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2003-10m.shp.zip',
            200320: 'http://gisco-services.ec.europa.eu/distribution/v2/nuts/download/ref-nuts-2003-20m.shp.zip',
        }

        publist = [2021, 2016, 2013, 2010, 2006, 2003]
        urllist = []
        for items in publist:
            if isinstance(resolution, list):
                for res in resolution:
                    if len(str(res)) == 1:
                        urlkey = int(str(items) + str(0) + str(res))
                    else:
                        urlkey = int(str(items) + str(res))
                    urllist.append(urldict.get(urlkey))
            else:
                if len(str(resolution)) == 1:
                    urlkey = int(str(items) + str(0) + str(resolution))
                else:
                    urlkey = int(str(items) + str(resolution))
                urllist.append(urldict.get(urlkey))

        for items in urllist:
            if items is None:
                continue
            r = requests.get(items, stream=True)
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
    finally:
        os.chdir(oldcwd)


def download_NACE_TransitionTables(path):
    """
    Creates, if necessary, the folder TransitionData in the given path and downloads NACE transition tables from Eurostat to save them in the folder TransitionData.

    Parameters
    ----------
    path : String
        Path to the root of the project.

    Returns
    -------
    None.

    """
    directory = 'TransitionData'
    path = os.path.join(path, directory)
    if os.path.isdir(path) is False:
        os.mkdir(path)
    if not os.listdir(path):
        url1 = (r'https://ec.europa.eu/eurostat/documents/1965800/1978760/' +
                '52249E90762B69F8E0440003BA9322F9.xls/2314229f-7606-4230-96d4-da18f045b692')
        url2 = (r'https://ec.europa.eu/eurostat/documents/1965800/1978760/' +
                'Copy+of+5225C5EEBF016050E0440003BA9322F9.xls/6e1aec88-f15b-4d0f-bccc-4ee505c7f810')
        urllib.request.urlretrieve(url1, os.path.join(path, 'Correspondance+table+NACERev2-NACERev1_1+table+format.xls'))
        urllib.request.urlretrieve(url2, os.path.join(path, 'Correspondance+table+NACERev1_1-NACERev2+table+format.xls'))


def pickle_RawData(path, force_rerun=False):
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
    if (os.path.isfile(os.path.join(path, 'PollutionData', 'pratr.pkl')) is False) or force_rerun:
        pratr = pd.read_csv(os.path.join(path, 'PollutionData', 'dbo.PUBLISH_POLLUTANTRELEASEANDTRANSFERREPORT.csv'))
        pratr.to_pickle(os.path.join(path, 'PollutionData', 'pratr.pkl'))

    # FACILITYREPORT
    if (os.path.isfile(os.path.join(path, 'PollutionData', 'fr.pkl')) is False) or force_rerun:
        fr = pd.read_csv(os.path.join(path, 'PollutionData', 'dbo.PUBLISH_FACILITYREPORT.csv'), encoding='latin-1', low_memory=False)
        fr.to_pickle(os.path.join(path, 'PollutionData', 'fr.pkl'))

    # POLLUTANTRELEASE
    if (os.path.isfile(os.path.join(path, 'PollutionData', 'pr.pkl')) is False) or force_rerun:
        pr = pd.read_csv(os.path.join(path, 'PollutionData', 'dbo.PUBLISH_POLLUTANTRELEASE.csv'), low_memory=False)
        pr.to_pickle(os.path.join(path, 'PollutionData', 'pr.pkl'))

    return None


def merge_PollutionData(path, force_rerun=False):
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
    if (os.path.isfile(os.path.join(path, 'PollutionData', 'db.pkl')) is False) or force_rerun:
        try:
            fr = pd.read_pickle(os.path.join(path, 'PollutionData', 'fr.pkl'))
            pr = pd.read_pickle(os.path.join(path, 'PollutionData', 'pr.pkl'))
            pratr = pd.read_pickle(os.path.join(path, 'PollutionData', 'pratr.pkl'))
        except FileNotFoundError:
            print('Error. Run function pickle_RawData')
        # speed difference for variing merge-order?? Table length differs,
        # merge smart enough to add multiple one row to multiple?
        # problematic to merge by multiple coloum names?
        # Some data have no PostalCode, wrong fomrated postal code or not actual PostalCode
        db01 = pd.merge(fr, pratr, on=['PollutantReleaseAndTransferReportID', 'CountryName', 'CountryCode'])
        db02 = pd.merge(db01, pr, on=['FacilityReportID', 'ConfidentialIndicator', 'ConfidentialityReasonCode',
                                      'ConfidentialityReasonName'])
        db02.to_pickle(os.path.join(path, 'PollutionData', 'db.pkl'))
    return None


def generate_PollutionData_2(path):
    """
    Generates the new data set. For this, the function downloads the .pkl file from the emipy repository, decompresses it and renames the columns.

    Parameters
    ----------
    path : String
        Path to the root of the project.

    Returns
    -------
    data2 : DataFrame
        The new data base in the format, that enables the emipy functions to act on it.

    """
    directory = 'PollutionData'
    path = os.path.join(path, directory)
    if os.path.isdir(path) is False:
        os.mkdir(path)
    if 'emipy_newdb.pkl' not in os.listdir(path):
        url = ('https://gitlab-public.fz-juelich.de/network-science-group/emipy/'
               + '-/raw/master/additionaldata/emipy_newdb.pkl?inline=false')
        urllib.request.urlretrieve(url, os.path.join(path, 'emipy_newdb.pkl'))
    if 'dbnew.pkl' not in os.listdir(path):
        data = pd.read_pickle(os.path.join(path, 'emipy_newdb.pkl'), compression='xz')
        columndict = {
            'reportingYear': 'ReportingYear',
            'Facility_INSPIRE_ID': 'FacilityReportID',
            'parentCompanyName': 'ParentCompanyName',
            'nameOfFeature': 'FacilityName',
            'mainActivityCode': 'MainIAActivityCode',
            'mainActivityName': 'MainIAActivityName',
            'pointGeometryLon': 'Long',
            'pointGeometryLat': 'Lat',
            'streetName': 'StreetName',
            'buildingNumber': 'BuildingNumber',
            'postalCode': 'PostalCode',
            'city': 'City',
            'countryCode': 'CountryCode',
            'pollutantCode': 'PollutantCode',
            'pollutantName': 'PollutantName',
            'medium': 'ReleaseMediumCode',
            'totalPollutantQuantityKg': 'TotalQuantity',
            'AccidentalPollutantQuantityKG': 'AccidentalQuantity',
            'methodCode': 'MethodBasisCode',
            'methodName': 'MethodBasisName',
            'NUTSRegionSourceCode': 'NUTSRegionGeoCode',
            'NUTSRegionSourceName': 'NUTSRegionGeoName',
            'NACEMainEconomicActivityCode': 'NACEMainEconomicActivityCode',
            'NACEMainEconomicActivityName': 'NACEMainEconomicActivityName'
        }
        data2 = data.rename(columndict, axis='columns')

        data2.loc[:, 'TotalQuantity'] = data2.loc[:, 'TotalQuantity'].replace(',', '.', regex=True).astype(float)
        data2.loc[:, 'AccidentalQuantity'] = data2.loc[:, 'AccidentalQuantity'].replace(',', '.', regex=True).astype(float)
        data2.loc[:, 'Long'] = data2.loc[:, 'Long'].replace(',', '.', regex=True).astype(float)
        data2.loc[:, 'Lat'] = data2.loc[:, 'Lat'].replace(',', '.', regex=True).astype(float)
        data2.loc[:, 'NACEMainEconomicActivityCode'] = data2.loc[:, 'NACEMainEconomicActivityCode'].astype(str).apply(lambda x: '0' + x if x.find('.') == 1 else x).apply(lambda x: x + '0' if len(x) == 4 else x)

        data2.to_pickle(os.path.join(path, 'dbnew.pkl'))
    os.remove(os.path.join(path, 'emipy_newdb.pkl'))


def get_RootPath():
    """
    Returns the current root path, stored in the config file.

    Returns
    -------
    path : String
        Current path to the root of the project, stored in the config file.

    """
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration',
                             'configuration.ini'))
    path = config['PATH']['path']
    return path


def change_RootPath(path):
    """
    Changes the path of the root to the project in the configuration.ini file.

    Parameters
    ----------
    path : String
        Path to the project, which is to access.

    Returns
    -------
    None.

    """
    config = configparser.ConfigParser()
    print(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration',
                       'configuration.ini'))
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration',
                             'configuration.ini'))
    config.set('PATH', 'path', path)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration',
                           'configuration.ini'), 'w') as configfile:
        config.write(configfile)


def init_emipy_project(path, resolution=10, force_rerun=False):
    """
    Executes the initiation of a new project. Downloads all needed data to the given path and merges data of interest.

    Parameters
    ----------
    path : String
        Path to root of project.
    force_rerun : Boolean, optional
        Forces the programm to rerun the merging routine, if True. The default is False.
    resolution : int/list, optional
        Defines the resolution, that the downloaded maps have. Selectable are 1,3,10,20,60. The default is 10.

    Returns
    -------
    None.

    """
    if path is None:
        print('A path to the root of the project is needed to initialize the project.')
        return

    change_RootPath(path)
    print('Root path successfully changed.')
    download_PollutionData(path=path)
    print('Pollution data successfully downloaded and extracted.')
    download_MapData(path=path, resolution=resolution)
    print('Map data successfully downloaded and extractet.')
    download_NACE_TransitionTables(path)
    print('Transition tables successfully downloaded.')
    pickle_RawData(path=path, force_rerun=force_rerun)
    merge_PollutionData(path=path, force_rerun=force_rerun)
    print('Data merged and pickled.')
    generate_PollutionData_2(path)
    print('New data base with data from 2017-2019 is generated.')
    directory = 'ExportData'
    path = os.path.join(path, directory)
    if os.path.isdir(path) is False:
        os.mkdir(path)
    print('The initialisation process is completed.')

    return
