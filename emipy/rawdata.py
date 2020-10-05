# -*- coding: utf-8 -*-
"""
This module contains all functions, necessary for the inititation of an emipy project.
"""

import pandas as pd
import os
from os.path import join, isfile
import matplotlib.pyplot as plt
import requests, zipfile, io
import csv
import configparser


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
        db02.to_pickle(os.path.join(path, 'PollutionData\\db.pkl'))
    return None


def change_rootpath(path):
    """
    changes the Path of the root to the project in the configuration.ini file

    Parameters
    ----------
    path : String
        Path to the project, which is to access.

    Returns
    -------
    None.

    """
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
    config.set('PATH', 'path', path)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'), 'w') as configfile:
        config.write(configfile)


def init_emipy_project(path, force_rerun=False):
    """
    Executes the initiation of a new project. Downloads all needed data and to the given path and merges data of interest.

    Parameters
    ----------
    path : String
        Path to root of project.
    force_rerun : Boolean, optional
        Forces the programm to rerun the merging routine, if True. The default is False.

    Returns
    -------
    None.

    """
    if path is None:
        print('A path to the root of the project is needed to initialize the project.')
        return None
    change_rootpath(path)
    download_PollutionData(path=path)
    download_MapFiles(path=path)
    pickle_rawdata(path=path, force_rerun=force_rerun)
    merge_frompickle(path=path, force_rerun=force_rerun)
    directory = 'ExportData'
    path = os.path.join(path, directory)
    if os.path.isdir(path) is False:
        os.mkdir(path)
    print('The Initialisation process is completed.')   
    return None
