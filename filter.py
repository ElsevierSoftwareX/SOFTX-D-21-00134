# -*- coding: utf-8 -*-
"""
XXX We need a proper description here XXX
addapted filter.py script to work with data, that are not located in folder of the script
"""

import pandas as pd
import os
from os.path import join, isfile
import geopandas


def read_db(path):
    """
    Loads complete pollution record.

    Parameters
    ----------
    path : String
        Path to the root of the project.

    Returns
    -------
    db : DataFrame
        complete pollution record.

    """
    try:
        db = pd.read_pickle(os.path.join(path, 'PollutionData\\db.pkl'))
    except FileNotFoundError:
        print('File not found in the given path.')
    return db


def read_mb(path, Resolution, spatialtype, NUTS_LVL=None, m_year='2021', projection='4326', subset=None):
    """
    Reads the shp file with the specifications given in the input.

    Parameters
    ----------
    path : String
        Path to root of your project.
    Resolution : String
        Resolution of the map.
    spatialtype : String
        Format of data presentation.
    NUTS_LVL : Int
        NUTS-classification level, defined by the eurostat.
    m_year : Int, optional
        Year of publication of the geographical data. The default is 2021.
    projection : Int, optional
        Projection on the globe. The default is 4326.
    subset : String, optional
        Specification of spatialtype. The default is None.

    Returns
    -------
    mb : DataFrame
        DataFrame with geometry data.

    """
    m_year = str(m_year)
    projection = str(projection)

    path = os.path.join(path, 'MappingData')
    if NUTS_LVL is None:
        foo = 'NUTS_' + spatialtype + '_' + Resolution + '_' + m_year + '_' + projection + '.shp'
    else:
        NUTS_LVL = str(NUTS_LVL)
        foo = 'NUTS_' + spatialtype + '_' + Resolution + '_' + m_year + '_' + projection + '_LEVL_' + NUTS_LVL + '.shp'
    path = os.path.join(path, foo)
    try:
        mb = geopandas.read_file(path)
    except FileNotFoundError:
        print('file not found in the given path')
    return mb


def get_NACECode_filter_list():
    """
    Displays a list of predefined industry sectors.

    Returns
    -------
    NACElist : list
        list of predefined industry sectors.

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
    Creates a list of NACE codes corresponding to the selected industry sectors.

    Parameters
    ----------
    group : String, optional
        industry sector. The default is None.

    Returns
    -------
    NACECode : List
        list of NACE codes corresponding to the specified industry sectors.

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


def get_CNTR_CODE_list(mb):
    """
    returns list of all possible CountryCodes in the given DataFrame.

    Parameters
    ----------
    mb : DataFrame
        Data of interest.

    Returns
    -------
    CNTR_CODE_list : list
        list of all Country codes present in the current DataFrame.

    """
    CNTR_CODE_list = []
    for items in mb.CNTR_CODE.unique():
        CNTR_CODE_list.append(items)
    return CNTR_CODE_list


def f_db(db, CountryName=None, ReportingYear=None, ReleaseMediumName=None, PollutantName=None, PollutantGroupName=None, NACEMainEconomicActivityCode=None, NUTSRegionGeoCode=None):
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

    if NUTSRegionGeoCode is not None:
        if isinstance(NUTSRegionGeoCode, list):
            db = db[db.NUTSRegionGeoCode.isin(NUTSRegionGeoCode)]
        else:
            db = db[db.NUTSRegionGeoCode == NUTSRegionGeoCode]
            
    return db


def f_mb(mb, NUTS_ID=None, CNTR_CODE=None, NAME_LATIN=None):
    """
    Filters the geomatry data of the DataFrame by the specifications of the input.

    Parameters
    ----------
    mb : DataFrame
        Input DataFrame.
    NUTS_ID : TYPE, optional
        NUTS:ID assigned from eurostat. The default is None.
    CNTR_CODE : TYPE, optional
        Country code. The default is None.
    NAME_LATIN : TYPE, optional
        Name of Region, classified by eurostat. The default is None.

    Returns
    -------
    mb : DataFrame
        DataFrame with geometry data of the specified conditions.

    """
    if CNTR_CODE is not None:
        if isinstance(CNTR_CODE, list):
            mb = mb[mb.CNTR_CODE.isin(CNTR_CODE)]
        else:
            mb = mb[mb.CNTR_CODE == CNTR_CODE]
    if NUTS_ID is not None:
        if isinstance(NUTS_ID, list):
            mb = mb[mb.NUTS_ID.isin(NUTS_ID)]
        else:
            mb = mb[mb.NUTS_ID == NUTS_ID]
    if NAME_LATIN is not None:
        if isinstance(NAME_LATIN, list):
            mb = mb[mb.NAME_LATIN.isin(NAME_LATIN)]
        else:
            mb = mb[mb.NAME_LATIN == NAME_LATIN]
    return mb


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


def export_db(db, path, filename):
    """
    Exports the filtered database to a .pkl file in the folder filterdata

    Parameters
    ----------
    db : DataFrame
        Filtered database, that is to export.
    path : string
        path to the storage folder.
    filename : String
        Name of .pkl file

    Returns
    -------
    Export of .pkl file

    """
    filename = 'filterdata' + filename
    db.to_pickle(os.path.join(path, filename))
