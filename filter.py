# -*- coding: utf-8 -*-
"""
XXX We need a proper description here XXX
addapted filter.py script to work with data, that are not located in folder of the script
"""

import pandas as pd
import os
from os.path import join, isfile

def read_db(path):
    """
    Reads complete database
    Returns the whole database as dataframe
    """
    try:
        db = pd.read_pickle(os.path.join(path, 'rawdata\\db.pkl'))
    except FileNotFoundError:
        print('db.pkl does not exist, please rerun merging routine')
    return db


def get_NACECode_filter_list():
    """
    returns list of industry sectors
    """
    NACElist = []
    NACElist.append(' Cement & Chalk: cem')
    NACElist.append(' Iron & Steel: is')
    NACElist.append(' Paper & Wood: pap')
    NACElist.append(' Chemistry: chem')
    NACElist.append(' Aluminium: alu')
    NACElist.append(' Refinery: ref')
    NACElist.append(' Glas: gla')
    NACElist.append(' Waste: wa')
    return NACElist


def get_NACECode_filter(group=None):
    """
    returns a list with the NACECode for preselected industry sectors (actual selection: Simon's list)
    """
    if group == 'cem':
        NACECode = ['23.51', '23.52']
    elif group == 'is':
        NACECode = ['19.10', '24.10', '24.20', '24.51', '24.52', '24.53', '24.54']
    elif group == 'pap':
        NACECode = ['16.21', '16.22', '16.23', '16.24', '16.29', '17.11', '17.12', '17.21', '17.22', '17.23', '17.24', '17.29']
    elif group == 'chem':
        NACECode = ['20.11', '20.12', '20.13', '20.14', '20.15', '20.16', '20.17', '20.20', '20.30', '20.41', '20.42', '20.51', '20.52', '20.53', '20.59', '21.10', '10.20', '22.11', '22.19', '22.21', '22.22', '22.23', '22.29']
    elif group == 'alu':
        NACECode = ['24.42']
    elif group == 'ref':
        NACECode = ['19.20']
    elif group == 'gla':
        NACECode = ['23.11', '23.12', '23.13', '23.14', '23.19']
    elif group == 'wa':
        NACECode = ['38.11', '38.12', '38.21', '38.22', '38.31', '38.32']
    return NACECode


def get_Countrylist(db):
    """
    Reads db.pkl
    Returns a list of all appearing countrys in given dataframe
    """
    Countrylist = []
    for items in db.CountryName.unique():
        Countrylist.append(items)
    return Countrylist


def get_Yearlist(db):
    """
    Reads db.pkl
    Returns a list of all appearing reporting years in given dataframe
    """
    Yearlist = []
    for items in db.ReportingYear.unique():
        Yearlist.append(items)
    return Yearlist


def get_Pollutantlist(db):
    """
    Returns a list of all appearing pollutants in given dataframe
    """
    Pollutantlist = []
    for items in db.PollutantName.unique():
        Pollutantlist.append(items)
    return Pollutantlist


def f_db(db, CountryName=None, ReportingYear=None, ReleaseMediumName=None, PollutantName=None, PollutantGroupName=None, NACEMainEconomicActivityCode=None):
    """
    filters db by country, year, release medium name, pollutant name, pollutantgroupname, NACEMainEconomicActivityCode

    To do: Think about excluding filters, not just wanted filters
    """
    if CountryName is not None:
        if isinstance(CountryName, list):
            db = db[db.CountryName.isin(CountryName)]
        else:
            db = db[db.CountryName == CountryName]

    if ReportingYear is not None:
        if isinstance(ReportingYear, list):
            db = db[db.ReportingYear.isin(ReportingYear)]
        else:
            db = db[db.ReportingYear == ReportingYear]

    if ReleaseMediumName is not None:
        if isinstance(ReleaseMediumName, list):
            db = db[db.ReleaseMediumName.isin(ReleaseMediumName)]
        else:
            db = db[db.ReleaseMediumName == ReleaseMediumName]

    if PollutantName is not None:
        if isinstance(PollutantName, list):
            db = db[db.PollutantName.isin(PollutantName)]
        else:
            db = db[db.PollutantName == PollutantName]

    if PollutantGroupName is not None:
        if isinstance(PollutantGroupName, list):
            db = db[db.PollutantGroupName.isin(PollutantGroupName)]
        else:
            db = db[db.PollutantGroupName == PollutantGroupName]

    if NACEMainEconomicActivityCode is not None:
        if isinstance(NACEMainEconomicActivityCode, list):
            db = db[db.NACEMainEconomicActivityCode.isin(NACEMainEconomicActivityCode)]
        else:
            db = db[db.NACEMainEconomicActivityCode == NACEMainEconomicActivityCode]

    return db


def rename_columns(db):
    """
    Change columnnames of db
    """
    db = db.rename(columns={'CountryName': 'Country'})
    db = db.rename(columns={'ReportingYear': 'Year'})
    return db


def row_reduction(db):
    """
    Reduces table to wanted rows
    To do: reduction to row names, that are given by input
    """
    db = db[['PollutantReleaseAndTransferReportID', 'CountryName', 'ReportingYear', 'FacilityReportID', 'PollutantReleaseID', 'ReleaseMediumName', 'PollutantName', 'PollutantGroupName', 'TotalQuantity', 'NACEMainEconomicActivityCode']]
    return db
