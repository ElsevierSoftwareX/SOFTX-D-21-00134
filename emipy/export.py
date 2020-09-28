# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:17:58 2020

@author: Morgenthaler
"""

import yaml
import pandas as pd
import copy

def get_default_config():
    """
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
    """
    years = sorted(data.ReportingYear.unique())
    df = pd.DataFrame()
    for y in years:
        df0 = pd.DataFrame(index=pd.date_range(start=str(y),
                                          end=str(y)+'-12-31 23',
                                          freq='H'))
        df = pd.concat([df, df0])

    coords = {}
    for y in years:
        for i, row in data[data.ReportingYear == y].iterrows():
            column_name = row.FacilityName.replace(' ', '_').replace('.', '_').replace(',', '_').replace('-', '_').replace('\&', '_').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
            df.loc[str(y), column_name] = row.TotalQuantity/len(df)
            coords[column_name] = (row.Lat, row.Long)
    return df, coords


def export_calliope(data, sc=0.07):
    """
    """

    df, coords = prepare_csv(data)
    d = get_default_config()
    config = {}
    
    for c in df.columns:
        config[c] = copy.deepcopy(d)
        s = 'emipy.csv:' + str(c)
        config[c]['techs']['co2_supply']['constraints']['resource'] = s
        config[c]['techs']['co2_supply']['constraints']['energy_cap_max'] = float(df.loc[:, c].max())
        config[c]['coordinates'] = {'lat': coords.get(c)[0], 'lon': coords.get(c)[1]}
        config[c]['techs']['co2_supply']['costs']['monetary']['om_prod'] = sc

    with open('emipy2calliope.yaml', 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

    df.to_csv('emipy.csv')

    return None


    