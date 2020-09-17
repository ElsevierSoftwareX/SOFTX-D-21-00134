# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:17:58 2020

@author: Morgenthaler
"""

import yaml
import pandas as pd

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
    return d


def prepare_csv(data, year):
    """
    """
    if not year in data.ReportingYear.unique():
        return print('Data does not match.')
    df = pd.DataFrame(index=pd.date_range(start=str(year),
                                          end=str(year)+'-12-31 23',
                                          freq='H'))
    for i, row in data.iterrows():
        column_name = row.FacilityName.replace(' ', '_').replace('.', '_').replace(',', '_').replace('-', '_')
        df[column_name] = row.TotalQuantity/len(df)
    return df