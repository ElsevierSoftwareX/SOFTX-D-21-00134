# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:45:28 2020

@author: f-ove

Functions for pickle editing
"""


import pandas as pd
import os
import matplotlib.pyplot as plt




def get_PollutantVolume(db, Table=True):
    """
    Returns the Volume of a Pollutant
    if Table is True it returns dataframe, if Table is False it returns Integer

    Really necessary? if table is not put false, it just returns db...

    """
    if Table is True:
        return db
    else:
        PollutantVolume = db['TotalQuantity'].sum()
        return PollutantVolume


def plot_PollutantVolume(db, form=1):
    """
    Plots the Pollutant Volume to wanted category.
    form = 1: against year
    form = 2: against country
    form = 3: against pollutant
    """

    # Volume against ReportingYear
    if form == 1:
        db = db.groupby(['ReportingYear']).sum().reset_index()
        db.plot(x='ReportingYear', y='TotalQuantity', kind='bar')
    # Volume against CountryName
    elif form == 2:
        db = db.groupby(['CountryName']).sum().reset_index()
        db.plot(x='CountryName', y='TotalQuantity', kind='bar')
    # Volume against PollutantName
    else:
        db = db.groupby(['PollutantName']).sum().reset_index()
        db.plot(x='PollutantName', y='TotalQuantity', kind='bar')

