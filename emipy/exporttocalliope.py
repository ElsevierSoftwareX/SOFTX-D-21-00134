# -*- coding: utf-8 -*-

import ruamel.yaml
import pandas as pd
import copy
import configparser
import os

def get_default_config():
    """
    Returns the default configuration 

    Returns
    -------
    d : dict
        dictionary with default configuration.

    """
    d = {'techs': {
        'amine_scrubbing': {
            'essentials': {
                'color': '#5d5142',
                'name': 'Amine Scrubbing', 
                'parent': 'conversion_plus',
                'carrier_in': 'electricity',
                'carrier_out': 'co2'},
            'constraints': {
                'energy_cap_max': 'inf',
                'energy_eff': 3.095975232,
                'lifetime': 20},
            'costs': {
                'monetary': {
                    'interest_rate': 0.08,
                    'energy_cap': 275,
                    'om_prod': 0.00239}}},
        'co2_supply': {
            'essentials': {
                'name': 'CO2 Supply',
                'color': '#0b95ef',
                'parent': 'supply',
                'carrier': 'co2'},
            'constraints': {
                'resource': 'inf',
                'energy_cap_max': 'inf',
                'lifetime': 1},
            'costs': {
                'monetary': {
                    'interest_rate': 0,
                    'om_prod': 0.07
                    }}}}}

    # For now, let's focus on supply only!
    d['techs'].pop('amine_scrubbing')
    return d


def prepare_csv(data):
    """
    Creates a DataFrame with the emission volume of the different facilitys distributed over a time series.

    Parameters
    ----------
    data : DataFrame
        Data from which a time series is to be generated.

    Returns
    -------
    df : DataFrame
        Time series of the pollutant emission for all present facility ID's.
    coords : dict
        Dictionary that stores the coordinates of each facility.
    FacilityIDDict : dict
        Dictionary that stores the facility names of each facility.

    """
    years = sorted(data.ReportingYear.unique())
    df = pd.DataFrame()
    for y in years:
        df0 = pd.DataFrame(index=pd.date_range(start=str(y),
                                          end=str(y)+'-12-31 23',
                                          freq='H'))
        df = pd.concat([df, df0])
    FacilityIDDict = {}
    coords = {}
    for y in years:
        df0 = pd.DataFrame(index=pd.date_range(start=str(y), end=str(y)+'-12-31 23', freq='H'))
        for i, row in data[data.ReportingYear == y].iterrows():
            FacilityIDDict[row.FacilityID] = row.FacilityName.replace(' ', '_').replace('.', '_').replace(',', '_').replace('-', '_').replace('\&', '_').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
            column_name = row.FacilityReportID
            # Warum FacilityID, ist ja genausowenig unique
            # Wäre FacilityReportID nicht eindeutig?
            # GEGENCHECKEN !!!!
            df.loc[str(y), column_name] = row.TotalQuantity / len(df0)
            # NEU EINGEFÜGT BZW ALTEN CODE GENOMMEN
            coords[column_name] = (row.Lat, row.Long)
    return df, coords, FacilityIDDict


def export_calliope(data, path=None, yamlfilename='emipy2calliope.yaml', csvfilename='emipy2calliope.csv', sc=0.07):
    """
    Exports the data to a csv file readable by the calliope project.

    Parameters
    ----------
    data : DataFrame
        Data that are to be exported.
    path : String, optional
        Path to the storage place. If None is given, emipy uses the path, stored in the config file. The default ist None.
    yamlfilename : String, optional
        filename for the yaml file. The default is emipy2calliope.yaml.
    csvfilename : String, optional
        filename for the csv file. The default is emipy2calliope.csv.
    sc : int, optional
        monetary cost factor. The default is 0.07.

    Returns
    -------
    None.

    """

    df, coords, FacilityIDDict = prepare_csv(data)
    d = get_default_config()
    config = {}

    for c in df.columns:
        config[c] = copy.deepcopy(d)
        s = 'file=emipy.csv:' + str(c)
        config[c]['coordinates'] = {'lat': coords.get(c)[0], 'lon': coords.get(c)[1]}
        config[c]['techs']['co2_supply']['constraints']['resource'] = s
        config[c]['techs']['co2_supply']['constraints']['energy_cap_max'] = float(df.loc[:, c].max())
        config[c]['techs']['co2_supply']['costs']['monetary']['om_prod'] = sc

    yaml = ruamel.yaml.YAML()
    yaml.indent(mapping=4, sequence=4, offset=2)

    if path == None:
        configuration = configparser.ConfigParser()
        configuration.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration\\configuration.ini'))
        path = configuration['PATH']['path']
        path = os.path.join(path, 'ExportData')

    with open(os.path.join(path, yamlfilename), 'w') as f:
        yaml.dump(config, f)

    df.to_csv(os.path.join(path, csvfilename))

    return None
