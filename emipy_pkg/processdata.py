# -*- coding: utf-8 -*-
"""
This module contains all functions to produce the data set of interest.
"""

import pandas as pd
import os
from os.path import join, isfile
import geopandas
import configparser


def read_db(path=None):
    """
    Loads complete pollution record.

    Parameters
    ----------
    path : String, optional
        Path to the root of the project.

    Returns
    -------
    db : DataFrame
        complete pollution record.

    """
    if path==None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'configuration.ini'))        
        path = config['PATH']['Path']
        print(path)
    try:
        db = pd.read_pickle(os.path.join(path, 'PollutionData\\db.pkl'))
    except FileNotFoundError:
        print('File not found in the given path.')
    return db


def read_mb(Resolution='01M', spatialtype='RG', path=None, NUTS_LVL=None, m_year='2021', projection='4326', subset=None):
    """
    Reads the shp file with the specifications given in the input.

    Parameters
    ----------
    Resolution : String
        Resolution of the map. The default is 01M
    spatialtype : String
        Format of data presentation. The default is RG
    path : String, optional
        Path to root of your project.
    NUTS_LVL : Int, optional
        NUTS-classification level, defined by the eurostat.
    m_year : Int
        Year of publication of the geographical data. The default is 2021.
    projection : Int
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
    if path==None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'configuration.ini'))        
        path = config['PATH']['Path']
        print(path)
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
    Returns a list of all appearing countries in given dataframe.

    Parameters
    ----------
    db : DataFrame
        Data in which is looked for unique countries.

    Returns
    -------
    Countrylist : List
        List of unique countries.

    """
    Countrylist = []
    for items in db.CountryName.unique():
        Countrylist.append(items)
    return Countrylist


def get_Yearlist(db):
    """
    Returns a list of all appearing reporting years in given dataframe.

    Parameters
    ----------
    db : DataFrame
        Data in which is looked for unique reporting years.

    Returns
    -------
    Countrylist : List
        List of unique reporting years.

    """
    Yearlist = []
    for items in db.ReportingYear.unique():
        Yearlist.append(items)
    return Yearlist


def get_Pollutantlist(db):
    """
    Returns a list of all appearing pollutant names in given dataframe.

    Parameters
    ----------
    db : DataFrame
        Data in which is looked for unique pollutant names.

    Returns
    -------
    Countrylist : List
        List of unique pollutant names.

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


def f_db(db, CountryName=None, ReportingYear=None, ReleaseMediumName=None, PollutantName=None, PollutantGroupName=None, NACEMainEconomicActivityCode=None, NUTSRegionGeoCode=None, ExclaveExclude=False):
    """
    Takes DataFrame and filters out data, according to input parameters.

    Parameters
    ----------
    db : DataFrame
        Input DataFrame.
    CountryName : String/List, optional
        List of countries to be maintained. The default is None.
    ReportingYear : String/List, optional
        List of reporting years to be maintained. The default is None.
    ReleaseMediumName : String/List, optional
        List of release medium names to be maintained. The default is None.
    PollutantName : String/List, optional
        List of pollutant names to be maintained. The default is None.
    PollutantGroupName : String/List, optional
        List of polllutant group names to be maintained. The default is None.
    NACEMainEconomicActivityCode : String/List, optional
        List of NACE main economic activity codes to be maintained. The default is None.
    NUTSRegionGeoCode : String/List, optional
        List of NUTS region geocodes to be maintained. The default is None.
    ExclaveExclude : Boolean, optional
        If True, exclaves that are unique NUTS-LVL1 regions are excluded. The default is False.

    Returns
    -------
    db : DataFrame
        DataFrame after filter process.
    dbna : DataFrame
        DataFrame that is filtered out, but has na values for the filter column. If they are filtered out correctly is not known.

    """
    dbna = pd.DataFrame()
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
            db = db[db.NUTSRegionGeoCode.str.startswith(tuple(NUTSRegionGeoCode)) is True]
        else:
            db = db[db.NUTSRegionGeoCode.str.startswith(NUTSRegionGeoCode) is True]

    ExclaveList = ('ES7', 'FRY', 'PT2', 'PT3')
    if ExclaveExclude is True:
        # negation does not work on na-values
        dbna = db[db.NUTSRegionGeoCode.isna()]
        db = db[db.NUTSRegionGeoCode.notna()]
        db = db[~db.NUTSRegionGeoCode.str.startswith(ExclaveList)]
    return (db, dbna)


def f_mb(mb, NUTS_ID=None, CNTR_CODE=None, NAME_LATIN=None, ExclaveExclude=False):
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
            mb = mb[mb.NUTS_ID.str.startswith(tuple(NUTS_ID)) is True]
        else:
            mb = mb[mb.NUTS_ID.str.startswith(NUTS_ID) is True]

    if NAME_LATIN is not None:
        if isinstance(NAME_LATIN, list):
            mb = mb[mb.NAME_LATIN.isin(NAME_LATIN)]
        else:
            mb = mb[mb.NAME_LATIN == NAME_LATIN]
    #ExclaveList has to be a tuple. invert does not work with list
    ExclaveList = ('ES7', 'FRY', 'PT2', 'PT3')           
    if ExclaveExclude is True:
        if mb.LEVL_CODE.sum() < len(mb):
            print('Exclave Exclusion is not yet possible on this NUTS_LVL.')
        else:
            mb = mb[~mb.NUTS_ID.str.startswith(ExclaveList)]

    return mb


def rename_columns(db):
    """
    Renames specific column names of the DataFrame.

    Parameters
    ----------
    db : DataFrame
        DataFrame which's column names should be changed.

    Returns
    -------
    db : DataFrame
        DataFrame with changed column names.

    """
    db = db.rename(columns={'CountryName': 'Country'})
    db = db.rename(columns={'ReportingYear': 'Year'})
    return db


def row_reduction(db):
    """
    Reduced DataFrame to specific columns.

    Parameters
    ----------
    db : DataFrame
        DataFrame which data shall be reduced.

    Returns
    -------
    db : DatFrame
        DataFrame with reduced number of columns.

    """
    db = db[['PollutantReleaseAndTransferReportID', 'CountryName', 'ReportingYear', 'FacilityReportID', 'PollutantReleaseID', 'ReleaseMediumName', 'PollutantName', 'PollutantGroupName', 'TotalQuantity', 'NACEMainEconomicActivityCode']]
    return db


def export_db(db, filename, path=None):
    """
    Exports the filtered database to a .pkl file in the folder filterdata

    Parameters
    ----------
    db : DataFrame
        Filtered database, that is to export.
    filename : String
        Name of .pkl file
    path : string, optional
        path to the storage folder.

    Returns
    -------
    Export of .pkl file

    """
    filename = 'ExportData' + filename
    db.to_pickle(os.path.join(path, filename))
