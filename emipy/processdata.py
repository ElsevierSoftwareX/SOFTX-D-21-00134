# -*- coding: utf-8 -*-
"""
This module contains all functions to produce the data set of interest.
"""

import pandas as pd
import os

import geopandas
import configparser
import copy


def read_db(path=None, NewData=False):
    """
    Loads complete pollution record.

    Parameters
    ----------
    path : String, optional
        Path to the file, that is to be loaded. The file has to be a .pkl file. If None is given, the function loades the data file, stored in the emipy project, that is specified in the config file. The default is 'None'.
    NewData : Boolean, optional
        If this is set to True, the data base with data from 2017 - 2019 is loaded instead of the one with data from 2001 - 2017. The default is False.

    Returns
    -------
    db : DataFrame
        Pollution record for either the years 2001-2017 or 2017-2019.

    """

    if path is None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 'configuration', 'configuration.ini'))
        path = config['PATH']['path']
        path = os.path.join(path, 'PollutionData')
        if NewData is False:
            path = os.path.join(path, 'db.pkl')
        else:
            path = os.path.join(path, 'dbnew.pkl')

    try:
        db = pd.read_pickle(path)
    except FileNotFoundError:
        print('File not found in the given path.')
        return None

    return db


def read_mb(path=None, resolution='10M', SpatialType='RG', NUTS_LVL=0, m_year=2016, projection=4326):
    """
    Reads the shp file with the specifications given in the input to load the map data.

    Parameters
    ----------
    path : String, optional
        Path of the file, that is to be loaded. The file has to be a .shp file. If None is given, the function loads the shp file in the emipy project, that is specified in the config file. The default is None.
    resolution : String
        Resolution of the map. The default is '10M'.
    SpatialType : String
        Format of data presentation. The default is 'RG'.
    NUTS_LVL : Int, optional
        NUTS-classification level, defined by the eurostat. The default is 0.
    m_year : Int
        Year of publication of the geographical data. The default is 2016.
    projection : Int
        Projection on the globe. The default is 4326.

    Returns
    -------
    mb : DataFrame
        DataFrame with geometry data.

    """

    if path is None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'))
        path = config['PATH']['path']
        path = os.path.join(path, 'MappingData')
        if NUTS_LVL is None:
            if SpatialType == 'LB':
                foo = 'NUTS_' + SpatialType + '_' + str(m_year) + '_' + str(projection) + '.shp'
            else:
                foo = 'NUTS_' + SpatialType + '_' + resolution + '_' + str(m_year) + '_' + str(projection) + '.shp'
        else:
            if SpatialType == 'LB':
                foo = 'NUTS_' + SpatialType + '_' + str(m_year) + '_' + str(projection) + '_LEVL_' + str(
                    NUTS_LVL) + '.shp'
            else:
                foo = 'NUTS_' + SpatialType + '_' + resolution + '_' + str(m_year) + '_' + str(
                    projection) + '_LEVL_' + str(NUTS_LVL) + '.shp'
        path = os.path.join(path, foo)

    try:
        mb = geopandas.read_file(path)
    except FileNotFoundError:
        print('File not found in the given path.')

    return mb


def get_NACECode_filter(specify=None):
    """
    If not specified, this function returns a dict with all stored NACECODE dictionaries. If specified, it returns the corresponding NACECODES as a list.

    Parameters
    ----------
    specify : String/List of Strings, optional
        Specify for wich economical categories you want to have the NACECODES. You can get a list of all selection options, with executing this function with specify=None.  The default is None.

    Returns
    -------
    NACElist : Dict/List
        If specify is None it returns a Dict with all stored NACECODE dictionarys. If specify is not None it returns the according NACECODES in a list.

    """
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'))
    if specify is None:
        NACElist = dict(config.items('NACECODES'))
    elif isinstance(specify, list):
        NACElist = []
        for items in specify:
            NACElist = NACElist + config['NACECODES'][items].split(',')
    else:
        NACElist = config['NACECODES'][specify].split(',')
    return NACElist


def get_NACECode_filter_industry(group=None):
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
        NACECode = ['16.21', '16.22', '16.23', '16.24', '16.29', '17.11', '17.12', '17.21', '17.22', '17.23', '17.24',
                    '17.29']
    elif group == 'chem':
        NACECode = ['20.11', '20.12', '20.13', '20.14', '20.15', '20.16', '20.17', '20.20', '20.30', '20.41', '20.42',
                    '20.51', '20.52', '20.53', '20.59', '21.10', '10.20', '22.11', '22.19', '22.21', '22.22', '22.23',
                    '22.29']
    elif group == 'alu':
        NACECode = ['24.42']
    elif group == 'ref':
        NACECode = ['19.20']
    elif group == 'gla':
        NACECode = ['23.11', '23.12', '23.13', '23.14', '23.19']
    elif group == 'wa':
        NACECode = ['38.11', '38.12', '38.21', '38.22', '38.31', '38.32']

    return NACECode


def change_NACECode_filter(total=None, add=None, sub=None):
    """
    Changes the NACE code dict in the config file.

    Parameters
    ----------
    total : Dict, optional
        Replacement dictionary that replaces the complete NACE code dict. The default is None.
    add : Dict, optional
        Dictionary that gets added to the NACE code dict. The default is None.
    sub : Dict, optional
        Dictionary that is substracted from the NACE code dict. The default is None.

    Returns
    -------
    None

    """
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'))
    if total is not None:
        config['NACECODES'] = total
    if add is not None:
        config['NACECODES'].update(add)
    if sub is not None:
        all(map(config['NACECODES'].pop, sub))
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'),
              'w') as configfile:
        config.write(configfile)
    return None


def get_CountryList(db):
    """
    Returns a list of all appearing countries in given dataframe.

    Parameters
    ----------
    db : DataFrame
        Data in which is looked for unique countries.

    Returns
    -------
    CountryList : List
        List of unique countries.

    """
    CountryList = []
    for items in db.CountryName.unique():
        CountryList.append(items)
    return CountryList


def get_YearList(db):
    """
    Returns a list of all appearing reporting years in given dataframe.

    Parameters
    ----------
    db : DataFrame
        Data in which is looked for unique reporting years.

    Returns
    -------
    YearList : List
        List of unique reporting years.

    """
    YearList = []
    for items in db.ReportingYear.unique():
        YearList.append(items)
    return YearList


def get_PollutantList(db):
    """
    Returns a list of all appearing pollutant names in given dataframe.

    Parameters
    ----------
    db : DataFrame
        Data in which is looked for unique pollutant names.

    Returns
    -------
    PollutantList : List
        List of unique pollutant names.

    """
    PollutantList = []
    for items in db.PollutantName.unique():
        PollutantList.append(items)
    return PollutantList


def get_CNTR_CODEList(mb):
    """
    returns list of all possible CountryCodes in the given DataFrame.

    Parameters
    ----------
    mb : DataFrame
        Data of interest.

    Returns
    -------
    CNTR_CODEList : list
        list of all Country codes present in the current DataFrame.

    """
    CNTR_CODEList = []
    for items in mb.CNTR_CODE.unique():
        CNTR_CODEList.append(items)
    return CNTR_CODEList


def f_db(db, FacilityReportID=None, CountryName=None, ReportingYear=None, ReleaseMediumName=None, PollutantName=None,
         PollutantGroupName=None, NACEMainEconomicActivityCode=None, NUTSRegionGeoCode=None, ParentCompanyName=None,
         FacilityName=None, City=None, PostalCode=None, CountryCode=None, RBDGeoCode=None, RBDGeoName=None,
         NUTSRegionGeoName=None, NACEMainEconomicActivityName=None, MainIASectorCode=None, MainIASectorName=None,
         MainIAActivityCode=None, MainIAActivityName=None, PollutantReleaseID=None, ReleaseMediumCode=None,
         PollutantCode=None, PollutantGroupCode=None, ExclaveExclude=False, ReturnUnknown=False):
    """
    Takes DataFrame and filters out data, according to input parameters.

    Parameters
    ----------
    db : DataFrame
        Input DataFrame.
    FacilityReportID : Int/String/List, optional
        List of FacilityReportID's to be maintained. In the data from 2001-2017 this entry is an integer. Therefore we have to use integers or a list of integers for the filtering. In the data from 2017-2019 this is stored as a string. Therefore we have to use a string or a list of strings for the filtering. The default is None.
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
    ParentCompanyName : String/List, optional
        List of Parent company names to be maintained. The default is None.
    FacilityName : String/List, optional
        List of facility names to be maintained. The default is None.
    City : String/list, optional
        List of cities to be maintained. The default is None.
    PostalCode : String/List, optional
        List of postal codes to be a´maintained. The default is None.
    CountryCode : String/List, optional
        List of country codes to be maintained. The default is None.
    RBDGeoCode : String/List, optional
        List of River Basin District geo codes to be maintained. The default is None.
    RBDGeoName : String/List, optional
        List of River Basin District geo names to be maintained. The default is None.
    NUTSRegionGeoName : String/List, optional
        List of NUTS  region geo names to be maintained. The default is None.
    NACEMainEconomicActivityName : String/List, optional
        List of NACE main economic activity names to be maintained. The default is None.
    MainIASectorCode : String/List, optional
        List of Investment Association sector codes to be maintained. The default is None.
    MainIASectorName : String/List, optional
        List of Investmend Association sector names to be maintained. The default is None.
    MainIAActivityCode : String/List, optional
        List of Investmend Association activity codes to be maintained. The default is None.
    MainIAActivityName : String/List, optional
        List of Investmend Association activity names to be maintained. The default is None.
    PollutantReleaseID : Int/List, optional
        List of pollutant release IDs to be maintained. The default is None.
    ReleaseMediumCode : String/List, optional
        List of realease medium codes to be maintained. The default is None.
    PollutantCode : String/List, optional
        List of pollutant codes to be maintained. The default is None.
    PollutantGroupCode : String/List, optional
        List of pollutant group codes to be maintained. The default is None.
    ExclaveExclude : Boolean, optional
        If True, exclaves that are unique NUTS-LVL1 regions are excluded. The default is False.
    ReturnUnknown : Boolean, optional
        If True, function returns DataFrame that is sorted out due to not enough information for the filter process. The default is False.

    Returns
    -------
    db : DataFrame
        DataFrame after filter process.
    dbna : DataFrame
        DataFrame that is filtered out, but has na values for the filter column. If they are filtered out correctly is not known.

    """
    dbna = pd.DataFrame()

    if FacilityReportID is not None:
        dbna = dbna.append(db[db.FacilityReportID.isna()])
        foo1 = dbna[dbna.FacilityReportID.isna()]
        if isinstance(FacilityReportID, list):
            foo2 = dbna[dbna.FacilityReportID.isin(FacilityReportID)]
        else:
            foo2 = dbna[dbna.FacilityReportID == FacilityReportID]
        dbna = foo1.append(foo2)

        if isinstance(FacilityReportID, list):
            db = db[db.FacilityReportID.isin(FacilityReportID)]
        else:
            db = db[db.FacilityReportID == FacilityReportID]

    if CountryName is not None:
        dbna = dbna.append(db[db.CountryName.isna()])
        foo1 = dbna[dbna.CountryName.isna()]
        if isinstance(CountryName, list):
            foo2 = dbna[dbna.CountryName.isin(CountryName)]
        else:
            foo2 = dbna[dbna.CountryName == CountryName]
        dbna = foo1.append(foo2)

        if isinstance(CountryName, list):
            db = db[db.CountryName.isin(CountryName)]
        else:
            db = db[db.CountryName == CountryName]

    if ReportingYear is not None:
        dbna = dbna.append(db[db.ReportingYear.isna()])
        foo1 = dbna[dbna.ReportingYear.isna()]
        if isinstance(ReportingYear, list):
            foo2 = dbna[dbna.ReportingYear.isin(ReportingYear)]
        else:
            foo2 = dbna[dbna.ReportingYear == ReportingYear]
        dbna = foo1.append(foo2)

        if isinstance(ReportingYear, list):
            db = db[db.ReportingYear.isin(ReportingYear)]
        else:
            db = db[db.ReportingYear == ReportingYear]

    if ReleaseMediumName is not None:
        dbna = dbna.append(db[db.ReleaseMediumName.isna()])
        foo1 = dbna[dbna.ReleaseMediumName.isna()]
        if isinstance(ReleaseMediumName, list):
            foo2 = dbna[dbna.ReleaseMediumName.isin(ReleaseMediumName)]
        else:
            foo2 = dbna[dbna.ReleaseMediumName == ReleaseMediumName]
        dbna = foo1.append(foo2)

        if isinstance(ReleaseMediumName, list):
            db = db[db.ReleaseMediumName.isin(ReleaseMediumName)]
        else:
            db = db[db.ReleaseMediumName == ReleaseMediumName]

    if PollutantName is not None:
        dbna = dbna.append(db[db.PollutantName.isna()])
        foo1 = dbna[dbna.PollutantName.isna()]
        if isinstance(PollutantName, list):
            foo2 = dbna[dbna.PollutantName.isin(PollutantName)]
        else:
            foo2 = dbna[dbna.PollutantName == PollutantName]
        dbna = foo1.append(foo2)

        if isinstance(PollutantName, list):
            db = db[db.PollutantName.isin(PollutantName)]
        else:
            db = db[db.PollutantName == PollutantName]

    if PollutantGroupName is not None:
        dbna = dbna.append(db[db.PollutantGroupName.isna()])
        foo1 = dbna[dbna.PollutantGroupName.isna()]
        if isinstance(PollutantGroupName, list):
            foo2 = dbna[dbna.PollutantGroupName.isin(PollutantGroupName)]
        else:
            foo2 = dbna[dbna.PollutantGroupName == PollutantGroupName]
        dbna = foo1.append(foo2)

        if isinstance(PollutantGroupName, list):
            db = db[db.PollutantGroupName.isin(PollutantGroupName)]
        else:
            db = db[db.PollutantGroupName == PollutantGroupName]

    if NACEMainEconomicActivityCode is not None:
        dbna = dbna.append(db[db.NACEMainEconomicActivityCode.isna()])
        foo1 = dbna[dbna.NACEMainEconomicActivityCode.isna()]
        if isinstance(NACEMainEconomicActivityCode, list):
            foo2 = dbna[dbna.NACEMainEconomicActivityCode.isin(NACEMainEconomicActivityCode)]
        else:
            foo2 = dbna[dbna.NACEMainEconomicActivityCode == NACEMainEconomicActivityCode]
        dbna = foo1.append(foo2)

        if isinstance(NACEMainEconomicActivityCode, list):
            foo = pd.DataFrame(db.loc[:, 'NACEMainEconomicActivityCode'].tolist()).isin(
                NACEMainEconomicActivityCode).any(1).astype(int)
            db = db.assign(foo=foo.values)
            db = db[db.foo == 1].drop(['foo'], axis=1)
            # The following does not work. Seems like pandas can not handle lists as values in the dataframe.
            # db = db[db.NACEMainEconomicActivityCode.isin(NACEMainEconomicActivityCode)]
        else:
            NACEMainEconomicActivityCode = [NACEMainEconomicActivityCode]
            foo = pd.DataFrame(db.loc[:, 'NACEMainEconomicActivityCode'].tolist()).isin(
                NACEMainEconomicActivityCode).any(1).astype(int)
            db = db.assign(foo=foo.values)
            db = db[db.foo == 1].drop(['foo'], axis=1)

    if NUTSRegionGeoCode is not None:
        dbna = dbna.append(db[db.NUTSRegionGeoCode.isna()])
        foo1 = dbna[dbna.NUTSRegionGeoCode.isna()]
        if isinstance(NUTSRegionGeoCode, list):
            foo2 = dbna[dbna.NUTSRegionGeoCode.str.startswith(tuple(NUTSRegionGeoCode), na=False) == True]
        else:
            foo2 = dbna[dbna.NUTSRegionGeoCode.str.startswith(NUTSRegionGeoCode, na=False) == True]
        dbna = foo1.append(foo2)

        if isinstance(NUTSRegionGeoCode, list):
            db = db[db.NUTSRegionGeoCode.str.startswith(tuple(NUTSRegionGeoCode), na=False) == True]
        else:
            db = db[db.NUTSRegionGeoCode.str.startswith(NUTSRegionGeoCode, na=False) == True]

    if ParentCompanyName is not None:
        dbna = dbna.append(db[db.ParentCompanyName.isna()])
        foo1 = dbna[dbna.ParentCompanyName.isna()]
        if isinstance(ParentCompanyName, list):
            foo2 = dbna[dbna.ParentCompanyName.isin(ParentCompanyName)]
        else:
            foo2 = dbna[dbna.ParentCompanyName == ParentCompanyName]
        dbna = foo1.append(foo2)

        if isinstance(ParentCompanyName, list):
            db = db[db.ParentCompanyName.isin(ParentCompanyName)]
        else:
            db = db[db.ParentCompanyName == ParentCompanyName]

    if FacilityName is not None:
        dbna = dbna.append(db[db.FacilityName.isna()])
        foo1 = dbna[dbna.FacilityName.isna()]
        if isinstance(FacilityName, list):
            foo2 = dbna[dbna.FacilityName.isin(FacilityName)]
        else:
            foo2 = dbna[dbna.FacilityName == FacilityName]
        dbna = foo1.append(foo2)

        if isinstance(FacilityName, list):
            db = db[db.FacilityName.isin(FacilityName)]
        else:
            db = db[db.FacilityName == FacilityName]

    if City is not None:
        dbna = dbna.append(db[db.City.isna()])
        foo1 = dbna[dbna.City.isna()]
        if isinstance(City, list):
            foo2 = dbna[dbna.City.isin(City)]
        else:
            foo2 = dbna[dbna.City == City]
        dbna = foo1.append(foo2)

        if isinstance(City, list):
            db = db[db.City.isin(City)]
        else:
            db = db[db.City == City]

    if PostalCode is not None:
        dbna = dbna.append(db[db.PostalCode.isna()])
        foo1 = dbna[dbna.PostalCode.isna()]
        if isinstance(PostalCode, list):
            foo2 = dbna[dbna.PostalCode.isin(PostalCode)]
        else:
            foo2 = dbna[dbna.PostalCode == PostalCode]
        dbna = foo1.append(foo2)

        if isinstance(PostalCode, list):
            db = db[db.PostalCode.isin(PostalCode)]
        else:
            db = db[db.PostalCode == PostalCode]

    if CountryCode is not None:
        dbna = dbna.append(db[db.CountryCode.isna()])
        foo1 = dbna[dbna.CountryCode.isna()]
        if isinstance(CountryCode, list):
            foo2 = dbna[dbna.CountryCode.isin(CountryCode)]
        else:
            foo2 = dbna[dbna.CountryCode == CountryCode]
        dbna = foo1.append(foo2)

        if isinstance(CountryCode, list):
            db = db[db.CountryCode.isin(CountryCode)]
        else:
            db = db[db.CountryCode == CountryCode]

    if RBDGeoCode is not None:
        dbna = dbna.append(db[db.RBDGeoCode.isna()])
        foo1 = dbna[dbna.RBDGeoCode.isna()]
        if isinstance(RBDGeoCode, list):
            foo2 = dbna[dbna.RBDGeoCode.isin(RBDGeoCode)]
        else:
            foo2 = dbna[dbna.RBDGeoCode == RBDGeoCode]
        dbna = foo1.append(foo2)

        if isinstance(RBDGeoCode, list):
            db = db[db.RBDGeoCode.isin(RBDGeoCode)]
        else:
            db = db[db.RBDGeoCode == RBDGeoCode]

    if RBDGeoName is not None:
        dbna = dbna.append(db[db.RBDGeoName.isna()])
        foo1 = dbna[dbna.RBDGeoName.isna()]
        if isinstance(RBDGeoName, list):
            foo2 = dbna[dbna.RBDGeoName.isin(RBDGeoName)]
        else:
            foo2 = dbna[dbna.RBDGeoName == RBDGeoName]
        dbna = foo1.append(foo2)

        if isinstance(RBDGeoName, list):
            db = db[db.RBDGeoName.isin(RBDGeoName)]
        else:
            db = db[db.RBDGeoName == RBDGeoName]

    if NUTSRegionGeoName is not None:
        dbna = dbna.append(db[db.NUTSRegionGeoName.isna()])
        foo1 = dbna[dbna.NUTSRegionGeoName.isna()]
        if isinstance(NUTSRegionGeoName, list):
            foo2 = dbna[dbna.NUTSRegionGeoName.isin(NUTSRegionGeoName)]
        else:
            foo2 = dbna[dbna.NUTSRegionGeoName == NUTSRegionGeoName]
        dbna = foo1.append(foo2)

        if isinstance(NUTSRegionGeoName, list):
            db = db[db.NUTSRegionGeoName.isin(NUTSRegionGeoName)]
        else:
            db = db[db.NUTSRegionGeoName == NUTSRegionGeoName]

    if NACEMainEconomicActivityName is not None:
        dbna = dbna.append(db[db.NACEMainEconomicActivityName.isna()])
        foo1 = dbna[dbna.NACEMainEconomicActivityName.isna()]
        if isinstance(NACEMainEconomicActivityName, list):
            foo2 = dbna[dbna.NACEMainEconomicActivityName.isin(NACEMainEconomicActivityName)]
        else:
            foo2 = dbna[dbna.NACEMainEconomicActivityName == NACEMainEconomicActivityName]
        dbna = foo1.append(foo2)

        if isinstance(NACEMainEconomicActivityName, list):
            db = db[db.NACEMainEconomicActivityName.isin(NACEMainEconomicActivityName)]
        else:
            db = db[db.NACEMainEconomicActivityName == NACEMainEconomicActivityName]

    if MainIASectorCode is not None:
        dbna = dbna.append(db[db.MainIASectorCode.isna()])
        foo1 = dbna[dbna.MainIASectorCode.isna()]
        if isinstance(MainIASectorCode, list):
            foo2 = dbna[dbna.MainIASectorCode.isin(MainIASectorCode)]
        else:
            foo2 = dbna[dbna.MainIASectorCode == MainIASectorCode]
        dbna = foo1.append(foo2)

        if isinstance(MainIASectorCode, list):
            db = db[db.MainIASectorCode.isin(MainIASectorCode)]
        else:
            db = db[db.MainIASectorCode == MainIASectorCode]

    if MainIASectorName is not None:
        dbna = dbna.append(db[db.MainIASectorName.isna()])
        foo1 = dbna[dbna.MainIASectorName.isna()]
        if isinstance(MainIASectorName, list):
            foo2 = dbna[dbna.MainIASectorName.isin(MainIASectorName)]
        else:
            foo2 = dbna[dbna.MainIASectorName == MainIASectorName]
        dbna = foo1.append(foo2)

        if isinstance(MainIASectorName, list):
            db = db[db.MainIASectorName.isin(MainIASectorName)]
        else:
            db = db[db.MainIASectorName == MainIASectorName]

    if MainIAActivityCode is not None:
        dbna = dbna.append(db[db.MainIAActivityCode.isna()])
        foo1 = dbna[dbna.MainIAActivityCode.isna()]
        if isinstance(MainIAActivityCode, list):
            foo2 = dbna[dbna.MainIAActivityCode.isin(MainIAActivityCode)]
        else:
            foo2 = dbna[dbna.MainIAActivityCode == MainIAActivityCode]
        dbna = foo1.append(foo2)

        if isinstance(MainIAActivityCode, list):
            db = db[db.MainIAActivityCode.isin(MainIAActivityCode)]
        else:
            db = db[db.MainIAActivityCode == MainIAActivityCode]

    if MainIAActivityName is not None:
        dbna = dbna.append(db[db.MainIAActivityName.isna()])
        foo1 = dbna[dbna.MainIAActivityName.isna()]
        if isinstance(MainIAActivityName, list):
            foo2 = dbna[dbna.MainIAActivityName.isin(MainIAActivityName)]
        else:
            foo2 = dbna[dbna.MainIAActivityName == MainIAActivityName]
        dbna = foo1.append(foo2)

        if isinstance(MainIAActivityName, list):
            db = db[db.MainIAActivityName.isin(MainIAActivityName)]
        else:
            db = db[db.MainIAActivityName == MainIAActivityName]

    if PollutantReleaseID is not None:
        dbna = dbna.append(db[db.PollutantReleaseID.isna()])
        foo1 = dbna[dbna.PollutantReleaseID.isna()]
        if isinstance(PollutantReleaseID, list):
            foo2 = dbna[dbna.PollutantReleaseID.isin(PollutantReleaseID)]
        else:
            foo2 = dbna[dbna.PollutantReleaseID == PollutantReleaseID]
        dbna = foo1.append(foo2)

        if isinstance(PollutantReleaseID, list):
            db = db[db.PollutantReleaseID.isin(PollutantReleaseID)]
        else:
            db = db[db.PollutantReleaseID == PollutantReleaseID]

    if ReleaseMediumCode is not None:
        dbna = dbna.append(db[db.ReleaseMediumCode.isna()])
        foo1 = dbna[dbna.ReleaseMediumCode.isna()]
        if isinstance(ReleaseMediumCode, list):
            foo2 = dbna[dbna.ReleaseMediumCode.isin(ReleaseMediumCode)]
        else:
            foo2 = dbna[dbna.ReleaseMediumCode == ReleaseMediumCode]
        dbna = foo1.append(foo2)

        if isinstance(ReleaseMediumCode, list):
            db = db[db.ReleaseMediumCode.isin(ReleaseMediumCode)]
        else:
            db = db[db.ReleaseMediumCode == ReleaseMediumCode]

    if PollutantCode is not None:
        dbna = dbna.append(db[db.PollutantCode.isna()])
        foo1 = dbna[dbna.PollutantCode.isna()]
        if isinstance(PollutantCode, list):
            foo2 = dbna[dbna.PollutantCode.isin(PollutantCode)]
        else:
            foo2 = dbna[dbna.PollutantCode == PollutantCode]
        dbna = foo1.append(foo2)

        if isinstance(PollutantCode, list):
            db = db[db.PollutantCode.isin(PollutantCode)]
        else:
            db = db[db.PollutantCode == PollutantCode]

    if PollutantGroupCode is not None:
        dbna = dbna.append(db[db.PollutantGroupCode.isna()])
        foo1 = dbna[dbna.PollutantGroupCode.isna()]
        if isinstance(PollutantGroupCode, list):
            foo2 = dbna[dbna.PollutantGroupCode.isin(PollutantGroupCode)]
        else:
            foo2 = dbna[dbna.PollutantGroupCode == PollutantGroupCode]
        dbna = foo1.append(foo2)

        if isinstance(PollutantGroupCode, list):
            db = db[db.PollutantGroupCode.isin(PollutantGroupCode)]
        else:
            db = db[db.PollutantGroupCode == PollutantGroupCode]

    ExclaveList = ('ES7', 'FRY', 'FRA', 'FR9', 'PT2', 'PT3')
    if ExclaveExclude is True:
        # negation does not work on na-values
        dbna = dbna.append(db[db.NUTSRegionGeoCode.isna()])
        foo1 = dbna[dbna.NUTSRegionGeoCode.isna()]
        foo2 = dbna[dbna.NUTSRegionGeoCode.str.startswith(ExclaveList, na=False)]
        dbna = foo1.append(foo2)
        db = db[db.NUTSRegionGeoCode.notna()]
        db = db[~db.NUTSRegionGeoCode.str.startswith(ExclaveList)]

    if ReturnUnknown == True:
        return dbna
    else:
        return db


def f_mb(mb, NUTS_ID=None, CNTR_CODE=None, NAME_LATN=None, ExclaveExclude=False):
    """
    Filters the geometry data of the DataFrame by the specifications of the input.

    Parameters
    ----------
    mb : DataFrame
        Input DataFrame.
    NUTS_ID : String/List, optional
        NUTS:ID assigned from eurostat. The default is None.
    CNTR_CODE : String/List, optional
        Country code. The default is None.
    NAME_LATN : String/List, optional
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
            mb = mb[mb.NUTS_ID.str.startswith(tuple(NUTS_ID)) == True]
        else:
            mb = mb[mb.NUTS_ID.str.startswith(NUTS_ID) == True]

    if NAME_LATN is not None:
        if isinstance(NAME_LATN, list):
            mb = mb[mb.NAME_LATN.isin(NAME_LATN)]
        else:
            mb = mb[mb.NAME_LATN == NAME_LATN]
    # ExclaveList has to be a tuple. invert does not work with list
    ExclaveList = ('ES7', 'FRY', 'FRA', 'FR9', 'PT2', 'PT3')
    if ExclaveExclude is True:
        if mb.LEVL_CODE.sum() < len(mb):
            print('Exclave Exclusion is not yet possible on this NUTS_LVL.')
        else:
            mb = mb[~mb.NUTS_ID.str.startswith(ExclaveList)]

    return mb


def change_unit(db, unit=None):
    """
    Changes the units of the emission in the table and adapts the numbers of TotalQuantity and AccidentalQuantity in the according way. If no unit is given, no changes are applied.

    Parameters
    ----------
    db : DataFrame
        DataFrame which units are to be changed.
    unit : string, optional
        New unit. The default is None.

    Returns
    -------
    data : DataFrame
        DataFrame with changed emission units.

    """
    if unit is None:
        print('New unit is needed. No changes applied.')
        return db
    UnitNumberDict = {
        'gram': 1,
        'kilogram': 10 ** 3,
        'ton': 10 ** 6,
        'kiloton': 10 ** 9,
        'megaton': 10 ** 12,
        'gigaton': 10 ** 15}
    UnitCodeDict = {
        'gram': 'GM',
        'kilogram': 'KGM',
        'ton': 'TN',
        'kiloton': 'KTN',
        'megaton': 'MTN',
        'gigaton': 'GTN'}

    data = copy.deepcopy(db).reset_index(drop=True)
    if len(data.UnitName.unique()) > 1:
        print('Warning: multiple units in DataFrame!')

    data_out = pd.DataFrame()
    for obj in data.UnitName.unique():
        foo = data[data.UnitName == obj]
        foo2 = foo[['TotalQuantity', 'AccidentalQuantity']] * UnitNumberDict[obj]/UnitNumberDict[unit]
        foo = foo.assign(TotalQuantity = foo2['TotalQuantity'])
        foo = foo.assign(AccidentalQuantity = foo2['AccidentalQuantity'])
        data_out = data_out.append(foo)
    data_out.loc[:, 'UnitName'] = unit
    data_out.loc[:, 'UnitCode'] = UnitCodeDict[unit]
    data_out = data_out.sort_index()
    return data_out


def perform_NACETransition(db, NewNACE=2, path=None):
    """
    Changes the NACE_1_1 Codes of the input DataFrame into NACE_2 Codes.

    Parameters
    ----------
    db : DataFrame
        Input DataFrame with partly entries that are coded with NACE_1_1.
    NewNACE : Int, optional
        The target NACE-code. The default is 2.
    path : String, optional
        Path to the root of your project. If None is given, emipy searches for the path, stored in the config file. The default is None.

    Returns
    -------
    final : DataFrame
        The input DataFrame with changed NACE-codes if necessary.

    """
    if path is None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'))
        path = config['PATH']['path']

    # The following lines are for loading the transition table into the session.
    if NewNACE == 2:
        try:
            tt = pd.read_excel(os.path.join(path, 'TransitionData',
                                            'Correspondance+table+NACERev1_1-NACERev2+table+format.xls'))
        except FileNotFoundError:
            print('File not found in the given path.')
            return None
    elif NewNACE == 1:
        try:
            tt = pd.read_excel(os.path.join(path, 'TransitionData',
                                            'Correspondance+table+NACERev2-NACERev1_1+table+format.xls'))
        except FileNotFoundError:
            print('File not found in the given path.')
            return None

    # The following lines are just for converting the columns NACE_1_1_CODE and NACE_2007_CODE to strings with the needed format (add 0)
    tt = tt.astype({'NACE_1_1_CODE': str, 'NACE_2007_CODE': str})
    foo1, foo2 = [], []
    for i in range(len(tt)):
        foo1.append(tt.NACE_1_1_CODE.iloc[i])
        foo2.append(tt.NACE_2007_CODE.iloc[i])
        if tt.NACE_1_1_CODE.iloc[i].find('.') != 2:
            foo1[i] = '0' + foo1[i]
        if tt.NACE_2007_CODE.iloc[i].find('.') != 2:
            foo2[i] = '0' + foo2[i]
        if tt.NACE_1_1_CODE.iloc[i].find('.') == len(tt.NACE_1_1_CODE.iloc[i]) - 2:
            foo1[i] = foo1[i] + '0'
        if tt.NACE_2007_CODE.iloc[i].find('.') == len(tt.NACE_2007_CODE.iloc[i]) - 2:
            foo2[i] = foo2[i] + '0'
    tt.drop('NACE_1_1_CODE', axis=1, inplace=True)
    tt['NACE_1_1_CODE'] = pd.Series(foo1)
    tt.drop('NACE_2007_CODE', axis=1, inplace=True)
    tt['NACE_2007_CODE'] = pd.Series(foo2)

    # The following lines are for seperating into NACE2 and NACE_1_1 entries.
    post2007 = db[~db.NACEMainEconomicActivityCode.str.startswith('NACE')]
    pre2007 = db[db.NACEMainEconomicActivityCode.str.startswith('NACE')]

    # The following lines are just for slicing the string "NACE1_1" out of the column NACEMainEconomicActivityCode. Perhaps more easy way but pandas has problems with changing values dependend on these values.
    foo = pre2007['NACEMainEconomicActivityCode'].str.slice(start=9)
    pre2007 = pre2007.drop(columns=['NACEMainEconomicActivityCode'])
    pre2007['NACEMainEconomicActivityCode'] = foo
    cols = pre2007.columns.tolist()
    a, b = cols.index('NACEMainEconomicActivityName'), cols.index('NACEMainEconomicActivityCode')
    cols.insert(a, cols.pop(b))
    pre2007 = pre2007[cols]

    # The following lines are for creating the transition dict. This is partly direct the transition table but for some old codes there is no transition, so we have to search for the appropriate codes.
    transitiondict = {}
    for items in tt.NACE_1_1_CODE.unique():
        foo3 = list(tt[tt.NACE_1_1_CODE == items].NACE_2007_CODE.unique())
        transitiondict.update({items: foo3})

    foo4 = pre2007[pre2007.NACEMainEconomicActivityCode.str.endswith('0')]
    foo5 = tt[tt.NACE_1_1_CODE.str.endswith('0')]
    for items in foo5.NACE_1_1_CODE.unique():
        foo4 = foo4[foo4.NACEMainEconomicActivityCode != items]
    for items in foo4.NACEMainEconomicActivityCode.unique():
        if items[3] == '0':
            foo6 = list(tt[tt.NACE_1_1_CODE.str.startswith(items[0:2])].NACE_2007_CODE.unique())
            transitiondict.update({items: foo6})
        else:
            foo6 = list(tt[tt.NACE_1_1_CODE.str.startswith(items[0:3])].NACE_2007_CODE.unique())
            transitiondict.update({items: foo6})
    # These are for 2 nace codes that have no transition (perhaps forgotten by eurostat?) We have assigned values that we think fit the best. Further explanation, how we come to the decision, can be found on the documentation side.
    transitiondict.update({'27.35': ['24.10']})
    transitiondict.update({'74.84': list(('59.20', '63.99', '74.10', '74.90', '77.40', '82.30', '82.91', '82.99'))})

    # The following lines are for performing the transition.
    for i in range(len(pre2007)):
        pre2007.at[i, 'NACEMainEconomicActivityCode'] = transitiondict[pre2007.loc[i, 'NACEMainEconomicActivityCode']]

    # The following line is just for combining both DataFrames to receive the final DataFrame.
    final = post2007.append(pre2007)
    return (final)


def change_RenameDict(total=None, add=None, sub=None, reset=False):
    """
    Changes the column name dict in the config file and returns the actual column names dict.

    Parameters
    ----------
    total : Dict, optional
        Replacement dictionary that replaces the complete column name dict. The default is None.
    add : Dict, optional
        Dictionary that gets added to the column name dict. The default is None.
    sub : Dict, optional
        Dictionary that is substracted from the column name dict. The default is None.
    reset : Boolean, optional
        If True, the column name dict gets resetted to the standard settings. The default is False.

    Returns
    -------
    config['COLUMNNAMES'] : dict
        actualised column name dictionary.

    """
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'))
    if reset is True:
        resetdict = {'ReportingYear': 'Year', 'CountryName': 'Country', 'NUTSRegionGeoCode': 'NUTSID',
                     'NACEMainEconomicActivityCode': 'NACEID', 'NACEMainEconomicActivityName': 'NACEName',
                     'PollutantName': 'Pollutant', 'UnitCode': 'Unit'}
        config['COLUMNNAMES'] = resetdict
    if total is not None:
        config['COLUMNNAMES'] = total
    if add is not None:
        config['COLUMNNAMES'].update(add)
    if sub is not None:
        all(map(config['COLUMNNAMES'].pop, sub))
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'),
              'w') as configfile:
        config.write(configfile)

    return config['COLUMNNAMES']


def rename_columns(db):
    """
    Renames column names of the DataFrame, specified by the "COLUMNNAMES" dict in the config file.

    Parameters
    ----------
    db : DataFrame
        DataFrame which's column names should be changed.

    Returns
    -------
    db : DataFrame
        DataFrame with changed column names.

    """
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'))
    columndict = dict(config.items('COLUMNNAMES'))
    db = db.rename(columns=columndict)
    return db


def change_ColumnsOfInterest(total=None, add=None, sub=None, reset=False):
    """
    Changes the list of column names in the config file, that are of interest.

    Parameters
    ----------
    total : List/String, optional
        Replaces the column names at all with the given list. If total is a string the names have to be seperated by a ",".  The default is None.
    add : List/String, optional
        Adds the given column names to the existing ones. If add is a string the names have to be seperated by a ",".The default is None.
    sub : List/String, optional
        Subtracts the given column names from the existing ones. If sub is a string the names have to be seperated by a ",".The default is None.
    reset : Boolean, optional
        Resets the list of column names to the presettings. The default is False.

    Returns
    -------
    config['COLUMNSOFINTEREST'] : dict
        Updated list of columnsofinterest.

    """
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'))
    if reset:
        columnnames = ('CountryCode,CountryName,Lat,Long,NUTSRegionGeoCode,NACEMainEconomicActivityCode,' +
                       'NACEMainEconomicActivityName,ReportingYear,PollutantReleaseID,' +
                       'PollutantName,TotalQuantity,UnitCode')

        config.set('COLUMNSOFINTEREST', 'columnnames', columnnames)
    if total is not None:
        if isinstance(total, list):
            columnnames = ','.join(total)
            config.set('COLUMNSOFINTEREST', 'columnnames', columnnames)
        else:
            config.set('COLUMNSOFINTEREST', 'columnnames', total)
    if add is not None:
        if isinstance(add, list):
            columnnames = config['COLUMNSOFINTEREST']['columnnames'].split(',') + add
            columnnames = ','.join(columnnames)
            config.set('COLUMNSOFINTEREST', 'columnnames', columnnames)
        else:
            columnnames = config['COLUMNSOFINTEREST']['columnnames'] + ',' + add
            config.set('COLUMNSOFINTEREST', 'columnnames', columnnames)
    if sub is not None:
        if isinstance(sub, list):
            columnnames = [item for item in config['COLUMNSOFINTEREST']['columnnames'].split(',') if item not in sub]
            columnnames = ','.join(columnnames)
            config.set('COLUMNSOFINTEREST', 'columnnames', columnnames)
        else:
            columnnames = config['COLUMNSOFINTEREST']['columnnames'].split(',')
            # this method stores the variable automatically
            columnnames.remove(sub)
            columnnames = ','.join(columnnames)
            config.set('COLUMNSOFINTEREST', 'columnnames', columnnames)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'),
              'w') as configfile:
        config.write(configfile)
    return config['COLUMNSOFINTEREST']


def row_reduction(db):
    """
    Reduces DataFrame to columns specified in the config file.

    Parameters
    ----------
    db : DataFrame
        DataFrame which data shall be reduced.

    Returns
    -------
    db : DatFrame
        DataFrame with reduced number of columns.

    """
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'))
    remain = config['COLUMNSOFINTEREST']['columnnames']
    remain = remain.split(',')
    db = db[remain]
    return db


def export_db_to_pickle(db, path=None, filename=None, **kwargs):
    """
    Stores the DataFrame given in the input as a .pkl file to the given path, or if the path is
     not given to the ExportData folder in the root path with the given filename.

    Parameters
    ----------
    db : DataFrame
        Filtered database, that is to export.
    path : String, optional
        Path under which the DataFrame is stored.
    filename : String, optional
        If the path is not given, this is the file name under which the DataFrame is
         stored in the ExportData folder of the project
    kwargs : Type, optional
        pandas.to_pickle() input arguments

    Returns
    -------
    None

    """
    if path is None and filename is None:
        print('A filename is required')
        return None

    elif path is None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'))
        path = config['PATH']['path']
        path = os.path.join(os.path.join(path, 'ExportData'), filename)

    elif path is not None and filename is not None:
        path = os.path.join(path, filename)

    if path.endswith('.pkl') is False:
        print('The file name or path must end with .pkl')
        return None

    db.to_pickle(path, **kwargs)

    return None


def export_db_to_csv(db, path=None, filename=None, **kwargs):
    """
    Stores the DataFrame given in the input as a .csv file to the given path,
     or if the path is not given to the ExportData folder in the root path with the given filename.

    Parameters
    ----------
    db : DataFrame
        Filtered database, that is to export.
    path : String, optional
        Path under which the DataFrame is stored.
    filename : String, optional
        If the path is not given, this is the file name under which the DataFrame is stored
         in the ExportData folder of the project
    kwargs : Type, optional
        pandas.to_csv() input arguments

    Returns
    -------
    None

    """
    if path is None and filename is None:
        print('A filename is required')
        return None

    elif path is None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration', 'configuration.ini'))
        path = config['PATH']['path']
        path = os.path.join(os.path.join(path, 'ExportData'), filename)

    elif path is not None and filename is not None:
        path = os.path.join(path, filename)

    if path.endswith('.csv') is False:
        print('The file name or path must end with .csv')

        return None

    db.to_csv(path, **kwargs)

    return None


def export_db_to_excel(db, path=None, filename=None, **kwargs):
    """
    Stores the DataFrame given in the input as a .xlsx file to the given path, or if the path is not given
    to the ExportData folder in the root path with the given filename.

    Parameters
    ----------
    db : DataFrame
        Filtered database, that is to export.
    path : String, optional
        Path under which the DataFrame is stored.
    filename : String, optional
        If the path is not given, this is the file name under which the DataFrame
        is stored in the ExportData folder of the project
    kwargs : Type, optional
        pandas.to_excel() input arguments

    Returns
    -------
    None

    """
    if path is None and filename is None:
        print('A filename is required')
        return None
    elif path is None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration',
                                 'configuration.ini'))
        path = config['PATH']['path']
        path = os.path.join(os.path.join(path, 'ExportData'), filename)

    elif path is not None and filename is not None:
        path = os.path.join(path, filename)

    if path.endswith('.xlsx') is False:
        print('The file name or path must end with .xlsx')

        return None

    db.to_excel(path, **kwargs)

    return None
