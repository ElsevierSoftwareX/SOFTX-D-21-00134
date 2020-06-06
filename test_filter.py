# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:41:15 2020

@author: f-ove

Testscript for module filter.py
"""

import pytest
from emipy import filter


@pytest.fixture
def db():
    db = filter.read_db('C:\\Witthaut\\Daten')
    return db


def test1_get_Yearlist(db):
    """
    tests for datatype
    """
    dt = filter.get_Yearlist(db)
    assert type(dt) == list


def test2_get_Yearlist(db):
    """
    test for length of list
    """
    length = filter.get_Yearlist(db)
    assert len(length) == 13


def test1_get_Countrylist(db):
    """
    tests for datatype
    """
    dt = filter.get_Countrylist(db)
    assert type(dt) == list


def test2_get_Countrylist(db):
    """
    tests for length of list
    """
    length = filter.get_Countrylist(db)
    assert len(length) == 32


def test1_get_Pollutantlist(db):
    """
    tests for datatype
    """
    dt = filter.get_Pollutantlist(db)
    assert type(dt) == list


def test2_get_Pollutantlist(db):
    """
    tests fo length of list
    """
    length = filter.get_Pollutantlist(db)
    assert len(length) == 94
