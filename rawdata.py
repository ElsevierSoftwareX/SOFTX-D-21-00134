# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:10:56 2020

@author: f-ove

addapted rawdataversion to work with data, that are not located in folder of the scripts
"""

import pandas as pd
import os
from os.path import join, isfile
import matplotlib.pyplot as plt
import requests, zipfile, io


def download_url(save_path, chunk_size=128):
    """
    download the .csv files from the following url 'https://www.eea.europa.eu/data-and-maps/data/member-states-reporting-art-7-under-the-european-pollutant-release-and-transfer-register-e-prtr-regulation-23/european-pollutant-release-and-transfer-register-e-prtr-data-base/eprtr_v9_csv.zip/at_download/file' 
    and saves them to given path.

    """
    url = 'https://www.eea.europa.eu/data-and-maps/data/member-states-reporting-art-7-under-the-european-pollutant-release-and-transfer-register-e-prtr-regulation-23/european-pollutant-release-and-transfer-register-e-prtr-data-base/eprtr_v9_csv.zip/at_download/file'
    r = requests.get(url, stream=True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(save_path)


def pickle_rawdata(path, force_rerun=False):
    """
    Write the following csv Sheets to Pickle Files:
    - POLLUTANTRELEASEANDTRANSFERREPORT
    - FACILITYREPORT
    - POLLUTANTRELEASE

    The script checks if the pickle files already exists in the given path.
    If it does, it skips the operation.

    If you set force_rerun to True, it will redo all operations.
    """

    # POLLUTANTRELEASEANDTRANSFERREPORT
    if ((os.path.isfile(os.path.join(path, 'rawdata\\pratr.pkl')) is False) or force_rerun):
        pratr = pd.read_csv(os.path.join(path, 'rawdata\\dbo.PUBLISH_POLLUTANTRELEASEANDTRANSFERREPORT.csv'))
        pratr.to_pickle(os.path.join(path, 'rawdata\\pratr.pkl'))

    # FACILITYREPORT
    if ((os.path.isfile(os.path.join(path, 'rawdata\\fr.pkl')) is False) or force_rerun):
        fr = pd.read_csv(os.path.join(path, 'rawdata\\dbo.PUBLISH_FACILITYREPORT.csv'), encoding='latin-1', low_memory=False)
        fr.to_pickle(os.path.join(path, 'rawdata\\fr.pkl'))

    # POLLUTANTRELEASE
    if ((os.path.isfile(os.path.join(path, 'rawdata\\pr.pkl')) is False) or force_rerun):
        pr = pd.read_csv(os.path.join(path, 'rawdata\\dbo.PUBLISH_POLLUTANTRELEASE.csv'), low_memory=False)
        pr.to_pickle(os.path.join(path, 'rawdata\\pr.pkl'))
    return None


def merge_frompickle(path, force_rerun=False):
    """
    This function will merge the desired data to one dataframe and stores it as pickle

    The script checks if the pickle files already exists in the given path.
    If it does, it skips the operation.

    If you set force_rerun to True, it will redo all operations.
    """
    if (os.path.isfile(os.path.join(path, 'rawdata\\db.pkl')) is False) or force_rerun:
        try:
            fr = pd.read_pickle(os.path.join(path, 'rawdata\\fr.pkl'))
            pr = pd.read_pickle(os.path.join(path, 'rawdata\\pr.pkl'))
            pratr = pd.read_pickle(os.path.join(path, 'rawdata\\pratr.pkl'))
        except FileNotFoundError:
            print('Error. Run function pickle_rawdata')

        try:
            # speed difference for variing merge-order?? Table length differs, merge smart enough to add multiple one row to multiple?
            # problematic to merge by multiple coloum names?
            db01 = pd.merge(fr, pratr, on=['PollutantReleaseAndTransferReportID', 'CountryName', 'CountryCode'])
            db02 = pd.merge(db01, pr, on=['FacilityReportID', 'ConfidentialIndicator', 'ConfidentialityReasonCode', 'ConfidentialityReasonName'])
            db02.to_pickle(os.path.join(path, 'rawdata\\db.pkl'))
        except NameError:
            print('Error. Merging not possible')
    return None












