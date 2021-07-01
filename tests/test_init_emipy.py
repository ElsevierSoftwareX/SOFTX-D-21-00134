# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 23:22:28 2021

@author: f-ove
"""

import os
import emipy as ep
import shutil
import pandas as pd

RootPath = os.path.join(os.getcwd(), 'Project')

class TestCompleteInitiation:

    def test_init_emipy_start(self):
        # test complete initiation function.
        os.mkdir(RootPath)
        foo = os.getcwd()
        ep.init_emipy_project(RootPath)
        os.chdir(foo)
        assert os.path.isdir(RootPath) is True

    def test_init_emipy_1(self):
        # Test if the PollutionData directory is generated in the initiation process.
        assert os.path.isdir(os.path.join(RootPath, 'PollutionData')) is True

    def test_init_emipy_2(self):
        # Test if the MappingData directory is generated in the initiation process.
        assert os.path.isdir(os.path.join(RootPath, 'MappingData')) is True

    def test_init_emipy_3(self):
        # Test if the TransitionData directory is generated in the initiation process.
        assert os.path.isdir(os.path.join(RootPath, 'TransitionData')) is True

    def test_init_emipy_4(self):
        # Test if the pollutin data is downloaded in the initiation process.
        assert len(os.listdir(os.path.join(RootPath, 'PollutionData'))) == 17

    def test_init_emipy_5(self):
        # Test if the mapping data is downloaded in the initiation process.
        assert len(os.listdir(os.path.join(RootPath, 'MappingData'))) == 1365

    def test_init_emipy_6(self):
        # Test if the transition data is downloaded in the initiation process.
        assert len(os.listdir(os.path.join(RootPath, 'TransitionData'))) == 2

    def test_init_emipy_7(self):
        # Test if pratr.pkl, fr.pkl and pr.pkl is generated in the initiation process.
        i = 0
        if os.path.isfile(os.path.join(RootPath, 'PollutionData\\pratr.pkl')):
            i = i + 1
        if os.path.isfile(os.path.join(RootPath, 'PollutionData\\fr.pkl')):
            i = i + 1
        if os.path.isfile(os.path.join(RootPath, 'PollutionData\\pr.pkl')):
            i = i + 1
        assert i == 3

    def test_init_emipy_8(self):
        # Test if db.pkl is generated in the initiation process.
        assert os.path.isfile(os.path.join(RootPath, 'PollutionData\\db.pkl')) is True

    def test_init_emipy_9(self):
        # Test if directory 'ExportData' is generated in the initiation process.
        assert os.path.isdir(os.path.join(RootPath, 'ExportData')) is True

    def test_init_emipy_10(self):
        # test downloadinng addition MapData.
        foo = os.getcwd()
        ep.download_MapData(RootPath, resolution=60)
        os.chdir(foo)
        assert len(os.listdir(os.path.join(RootPath, 'MappingData'))) == 2120

class TestReadData:

    def test_read_db1(self):
        # Test if the complete data set is loadable (without specifing the path) and has 470203 rows and 73 columns.
        db = ep.read_db()
        i = 0
        if len(db) == 470203:
            i = i + 1
        if len(db.columns) == 73:
            i = i + 1
        assert i == 2

    def test_read_db2(self):
        # Test if the complete data set is loadable (with specifing the path) and has 470203 rows and 73 columns.
        db = ep.read_db(RootPath)
        i = 0
        if len(db) == 470203:
            i = i + 1
        if len(db.columns) == 73:
            i = i + 1
        assert i == 2

    def test_read_db3(self):
        # Test if the data type of the output is a pandas DataFrame
        db = ep.read_db()
        assert type(db) == pd.core.frame.DataFrame

    def test_read_mb1(self):
        # Test if basic mapbase is loadable (with specifing the path) and has 37 rows and 10 columns.
        mb = ep.read_mb(RootPath)
        i = 0
        if len(mb) == 37:
            i = i + 1
        if len(mb.columns) == 10:
            i = i + 1
        assert i == 2

    def test_read_mb2(self):
        # Test if the standard mapbases are all loadable (without outspecifing the path)
        mb = ep.read_mb(m_year=2003)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=0)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=0, projection=4326)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=0, projection=3035)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=0, projection=3857)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=1)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=1, projection=4326)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=1, projection=3035)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=1, projection=3857)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=2)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=2, projection=4326)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=2, projection=3035)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=2, projection=3857)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=3)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=3, projection=4326)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=3, projection=3035)
        mb = ep.read_mb(m_year=2003, NUTS_LVL=3, projection=3857)
        mb = ep.read_mb(m_year=2006)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=0)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=0, projection=4326)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=0, projection=3035)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=0, projection=3857)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=1)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=1, projection=4326)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=1, projection=3035)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=1, projection=3857)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=2)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=2, projection=4326)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=2, projection=3035)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=2, projection=3857)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=3)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=3, projection=4326)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=3, projection=3035)
        mb = ep.read_mb(m_year=2006, NUTS_LVL=3, projection=3857)
        mb = ep.read_mb(m_year=2010)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=0)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=0, projection=4326)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=0, projection=3035)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=0, projection=3857)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=1)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=1, projection=4326)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=1, projection=3035)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=1, projection=3857)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=2)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=2, projection=4326)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=2, projection=3035)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=2, projection=3857)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=3)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=3, projection=4326)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=3, projection=3035)
        mb = ep.read_mb(m_year=2010, NUTS_LVL=3, projection=3857)
        mb = ep.read_mb(m_year=2013)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=0)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=0, projection=4326)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=0, projection=3035)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=0, projection=3857)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=1)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=1, projection=4326)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=1, projection=3035)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=1, projection=3857)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=2)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=2, projection=4326)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=2, projection=3035)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=2, projection=3857)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=3)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=3, projection=4326)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=3, projection=3035)
        mb = ep.read_mb(m_year=2013, NUTS_LVL=3, projection=3857)
        mb = ep.read_mb(m_year=2016)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=0)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=0, projection=4326,)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=0, projection=3035)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=0, projection=3857)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=1)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=1, projection=4326)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=1, projection=3035)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=1, projection=3857)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=2)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=2, projection=4326)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=2, projection=3035)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=2, projection=3857)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=3)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=3, projection=4326)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=3, projection=3035)
        mb = ep.read_mb(m_year=2016, NUTS_LVL=3, projection=3857)
        mb = ep.read_mb(m_year=2021)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=0)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=0, projection=4326)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=0, projection=3035)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=0, projection=3857)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=1)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=1, projection=4326)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=1, projection=3035)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=1, projection=3857)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=2)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=2, projection=4326)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=2, projection=3035)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=2, projection=3857)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=3)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=3, projection=4326)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=3, projection=3035)
        mb = ep.read_mb(m_year=2021, NUTS_LVL=3, projection=3857)

        # This is for testing if the basic mb has the right number of entries.
        mb = ep.read_mb()
        i = 0
        if len(mb) == 37:
            i = i + 1
        if len(mb.columns) == 10:
            i = i + 1
        assert i == 2


def test_cleanup2():
    shutil.rmtree(RootPath, ignore_errors=True)
    assert os.path.isdir(RootPath) is False
