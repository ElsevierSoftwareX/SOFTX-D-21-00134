# -*- coding: utf-8 -*-
"""
This module contains all functions to produce the data set of interest.
"""

import pandas as pd
import os
from os.path import join, isfile
import geopandas
import configparser
import copy


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
    if path == None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
        path = config['PATH']['path']
    try:
        db = pd.read_pickle(os.path.join(path, 'PollutionData\\db.pkl'))
    except FileNotFoundError:
        print('File not found in the given path.')
        return None
    return db


def read_mb(path=None, Resolution='10M', spatialtype='RG', NUTS_LVL=0, m_year=2016, projection=4326):
    """
    Reads the shp file with the specifications given in the input.

    Parameters
    ----------
    path : String, optional
        Path to root of your project.
    Resolution : String
        Resolution of the map. The default is '10M'.
    spatialtype : String
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

    if path == None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
        path = config['PATH']['path']
    path = os.path.join(path, 'MappingData')
    if NUTS_LVL is None:
        if spatialtype == 'LB':
            foo = 'NUTS_' + spatialtype + '_' + str(m_year) + '_' + str(projection) + '.shp'
        else:
            foo = 'NUTS_' + spatialtype + '_' + Resolution + '_' + str(m_year) + '_' + str(projection) + '.shp'
    else:
        if spatialtype == 'LB':
            foo = 'NUTS_' + spatialtype + '_' + str(m_year) + '_' + str(projection) + '_LEVL_' + str(NUTS_LVL) + '.shp'
        else:
            foo = 'NUTS_' + spatialtype + '_' + Resolution + '_' + str(m_year) + '_' + str(projection) + '_LEVL_' + str(NUTS_LVL) + '.shp'
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
    Yearlist : List
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
    Pollutant : List
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


def f_db(db, FacilityReportID=None, CountryName=None, ReportingYear=None, ReleaseMediumName=None, PollutantName=None, PollutantGroupName=None, NACEMainEconomicActivityCode=None, NUTSRegionGeoCode=None, ExclaveExclude=False, ReturnUnknown=False):
    """
    Takes DataFrame and filters out data, according to input parameters.

    Parameters
    ----------
    db : DataFrame
        Input DataFrame.
    FacilityReportID : Int/List, optional
        List of FacilityReportID's to be maintained. The default is None.
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
        # The following line ensures that dbna has just data that is na over all filter parameter. Not needed in first filter paramter, but stays here for consistency.
        dbna = dbna[dbna.FacilityReportID.isna()]
        if isinstance(FacilityReportID, list):
            db = db[db.FacilityReportID.isin(FacilityReportID)]
        else:
            db = db[db.FacilityReportID == FacilityReportID]

    if CountryName is not None:
        dbna = dbna.append(db[db.CountryName.isna()])
        dbna = dbna[dbna.CountryName.isna()]
        if isinstance(CountryName, list):
            db = db[db.CountryName.isin(CountryName)]
        else:
            db = db[db.CountryName == CountryName]

    if ReportingYear is not None:
        dbna = dbna.append(db[db.ReportingYear.isna()])
        dbna = dbna[dbna.ReportingYear.isna()]
        if isinstance(ReportingYear, list):
            db = db[db.ReportingYear.isin(ReportingYear)]
        else:
            db = db[db.ReportingYear == ReportingYear]

    if ReleaseMediumName is not None:
        dbna = dbna.append(db[db.ReleaseMediumName.isna()])
        dbna = dbna[dbna.ReleaseMediumName.isna()]
        if isinstance(ReleaseMediumName, list):
            db = db[db.ReleaseMediumName.isin(ReleaseMediumName)]
        else:
            db = db[db.ReleaseMediumName == ReleaseMediumName]

    if PollutantName is not None:
        dbna = dbna.append(db[db.PollutantName.isna()])
        dbna = dbna[dbna.PollutantName.isna()]
        if isinstance(PollutantName, list):
            db = db[db.PollutantName.isin(PollutantName)]
        else:
            db = db[db.PollutantName == PollutantName]

    if PollutantGroupName is not None:
        dbna = dbna.append(db[db.PollutantGroupName.isna()])
        dbna = dbna[dbna.PollutantGroupName.isna()]
        if isinstance(PollutantGroupName, list):
            db = db[db.PollutantGroupName.isin(PollutantGroupName)]
        else:
            db = db[db.PollutantGroupName == PollutantGroupName]

    if NACEMainEconomicActivityCode is not None:
        dbna = dbna.append(db[db.NACEMainEconomicActivityCode.isna()])
        dbna = dbna[dbna.NACEMainEconomicActivityCode.isna()]
        if isinstance(NACEMainEconomicActivityCode, list):
            db = db[db.NACEMainEconomicActivityCode.isin(NACEMainEconomicActivityCode)]
        else:
            db = db[db.NACEMainEconomicActivityCode == NACEMainEconomicActivityCode]

    if NUTSRegionGeoCode is not None:
        dbna = dbna.append(db[db.NUTSRegionGeoCode.isna()])
        dbna = dbna[dbna.NUTSRegionGeoCode.isna()]
        if isinstance(NUTSRegionGeoCode, list):
            db = db[db.NUTSRegionGeoCode.str.startswith(tuple(NUTSRegionGeoCode)) is True]
        else:
            db = db[db.NUTSRegionGeoCode.str.startswith(NUTSRegionGeoCode) is True]

    ExclaveList = ('ES7', 'FRY', 'FRA', 'FR9', 'PT2', 'PT3')
    if ExclaveExclude is True:
        # negation does not work on na-values
        dbna = dbna.append(db[db.NUTSRegionGeoCode.isna()])
        dbna = dbna[dbna.NUTSRegionGeoCode.isna()]
        db = db[db.NUTSRegionGeoCode.notna()]
        db = db[~db.NUTSRegionGeoCode.str.startswith(ExclaveList)]

    if ReturnUnknown == True:
        return dbna
    else:
        return db


def f_mb(mb, NUTS_ID=None, CNTR_CODE=None, NAME_LATIN=None, ExclaveExclude=False):
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
    NAME_LATIN : String/List, optional
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

    if NAME_LATIN is not None:
        if isinstance(NAME_LATIN, list):
            mb = mb[mb.NAME_LATIN.isin(NAME_LATIN)]
        else:
            mb = mb[mb.NAME_LATIN == NAME_LATIN]
    # ExclaveList has to be a tuple. invert does not work with list
    ExclaveList = ('ES7', 'FRY', 'FRA', 'FR9', 'PT2', 'PT3')
    if ExclaveExclude is True:
        if mb.LEVL_CODE.sum() < len(mb):
            print('Exclave Exclusion is not yet possible on this NUTS_LVL.')
        else:
            mb = mb[~mb.NUTS_ID.str.startswith(ExclaveList)]

    return mb


def change_Unit(db, Unit=None):
    """
    Changes the Units of the emission in the table and adapts the numbers of TotalQuantity in the according way. If no Unit is given, no changes are applied.

    Parameters
    ----------
    db : DataFrame
        DataFrame which Units are to be changed.
    Unit : string, optional
        New Unit. The default is None.

    Returns
    -------
    data : DataFrame
        DataFrame with changed emission units.

    """
    if Unit == None:
        print('New Unit is needed. No changes applied.')
        return None
    UnitNumberDict = {
        'gram': 1,
        'kilogram': 10**3,
        'ton': 10**6,
        'kiloton': 10**9,
        'megaton': 10**12,
        'gigaton': 10**15}
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

    # The first two lines are just applicable, if the DataFrame has just one Unit. They represent two ways how to call the values that are to change.
    # factor = UnitNumberDict[db.UnitName.unique()[0]] / UnitNumberDict[Unit]
    # The third line is more generally applicable. It's written more "Pythonic" but the dict can't be called from a hasable object.
    # data.loc[:, 'TotalQuantity'] = data.loc[:, 'TotalQuantity'] * factor
    # data.TotalQuantity = data.TotalQuantity * factor
    # data.TotalQuantity = data.TotalQuantity * UnitNumberDict[data.UnitName] / UnitNumberDict[Unit]
    for i in range(len(data)):
        data.loc[i, 'TotalQuantity'] = data.loc[i, 'TotalQuantity'] * UnitNumberDict[data.loc[i, 'UnitName']] / UnitNumberDict[Unit]

    data.loc[:, 'UnitName'] = Unit
    data.loc[:, 'UnitCode'] = UnitCodeDict[Unit]
    return data


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
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
    if reset == True:
        resetdict = {'ReportingYear': 'Year', 'CountryName': 'Country', 'NUTSRegionGeoCode': 'NUTSID', 'NACEMainEconomicActivityCode': 'NACEID', 'NACEMainEconomicActivityName': 'NACEName', 'PollutantName': 'Pollutant', 'UnitCode': 'Unit'}
        config['COLUMNNAMES'] = resetdict
    if total != None:
        config['COLUMNNAMES'] = total
    if add != None:
        config['COLUMNNAMES'].update(add)
    if sub != None:
        all(map(config['COLUMNNAMES'].pop, sub))
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'), 'w') as configfile:
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
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
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
    None.

    """
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
    if reset == True:
        columnnames = 'CountryCode,CountryName,Lat,Long,NUTSRegionGeoCode,NACEMainEconomicActivityCode,NACEMainEconomicActivityName,ReportingYear,PollutantReleaseID,PollutantName,TotalQuantity,UnitCode'
        config.set('COLUMNSOFINTEREST', 'columnnames', columnnames)
    if total != None:
        if isinstance(total, list):
            columnnames = ','.join(total)
            config.set('COLUMNSOFINTEREST', 'columnnames', columnnames)
        else:
            config.set('COLUMNSOFINTEREST', 'columnnames', total)
    if add != None:
        if isinstance(add, list):
            columnnames = config['COLUMNSOFINTEREST']['columnnames'].split(',') + add
            columnnames = ','.join(columnnames)
            config.set('COLUMNSOFINTEREST', 'columnnames', columnnames)
        else:
            columnnames = config['COLUMNSOFINTEREST']['columnnames'] + ',' + add
            config.set('COLUMNSOFINTEREST', 'columnnames', columnnames)
    if sub != None:
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
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'), 'w') as configfile:
        config.write(configfile)


def row_reduction(db):
    """
    Reduces DataFrame to columns specified in the conifg file.

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
    config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
    remain = config['COLUMNSOFINTEREST']['columnnames']
    remain = remain.split(',')
    db = db[remain]
    return db


def export_db_topickle(db, path=None, filename=None, **kwargs):
    """
    Stores the DataFrame given in the input as a .pkl file to the given path, or if the path is not given to the ExportData folder in the root path with the given filename.

    Parameters
    ----------
    db : DataFrame
        Filtered database, that is to export.
    path : String, optional
        Path under which the DataFrame is stored.
    filename : String, optional
        If the path is not given, this is the file name under which the DataFrame ist stored in the ExportData folder of the project
    kwargs : Type, optional
        pandas.to_pickle() input arguments

    Returns
    -------
    None

    """
    if (path == None and filename == None):
        print('A filename is required')
        return None
    elif path == None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
        path = config['PATH']['path']
        path = os.path.join(os.path.join(path, 'ExportData'), filename)
    elif (path != None and filename != None):
        path = os.path.join(path, filename)

    if path.endswith('.pkl') == False:
        print('The file name or path must end with .pkl')
        return None

    db.to_pickle(path, **kwargs)
    return None


def export_db_tocsv(db, path=None, filename=None, **kwargs):
    """
    Stores the DataFrame given in the input as a .csv file to the given path, or if the path is not given to the ExportData folder in the root path with the given filename.

    Parameters
    ----------
    db : DataFrame
        Filtered database, that is to export.
    path : String, optional
        Path under which the DataFrame is stored.
    filename : String, optional
        If the path is not given, this is the file name under which the DataFrame ist stored in the ExportData folder of the project
    kwargs : Type, optional
        pandas.to_csv() input arguments

    Returns
    -------
    None

    """
    if (path == None and filename == None):
        print('A filename is required')
        return None
    elif path == None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
        path = config['PATH']['path']
        path = os.path.join(os.path.join(path, 'ExportData'), filename)
    elif (path != None and filename != None):
        path = os.path.join(path, filename)

    if path.endswith('.csv') == False:
        print('The file name or path must end with .csv')
        return None

    db.to_csv(path, **kwargs)
    return None


def export_db_toexcel(db, path=None, filename=None, **kwargs):
    """
    Stores the DataFrame given in the input as a .xlsx file to the given path, or if the path is not given to the ExportData folder in the root path with the given filename.

    Parameters
    ----------
    db : DataFrame
        Filtered database, that is to export.
    path : String, optional
        Path under which the DataFrame is stored.
    filename : String, optional
        If the path is not given, this is the file name under which the DataFrame ist stored in the ExportData folder of the project
    kwargs : Type, optional
        pandas.to_excel() input arguments

    Returns
    -------
    None

    """
    if (path == None and filename == None):
        print('A filename is required')
        return None
    elif path == None:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
        path = config['PATH']['path']
        path = os.path.join(os.path.join(path, 'ExportData'), filename)
    elif (path != None and filename != None):
        path = os.path.join(path, filename)

    if path.endswith('.xlsx') == False:
        print('The file name or path must end with .xlsx')
        return None

    db.to_excel(path, **kwargs)
    return None
