# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:22:07 2021

@author: f-ove
This is a testscript for the module visualizedata of the package emipy.
"""

import pandas as pd

import numpy as np
import emipy as ep
import copy

d = {'FacilityReportID': [1856, 1856, 1856, 1856, 1857, 3110391],
     'PollutantReleaseAndTransferReportID': [1, 1, 1, 1, 1, 2453],
     'FacilityID': [5763, 5763, 5763, 5763, 5764, 8896],
     'NationalID': ['1013410312', '1013410312', '1013410312', '1013410312', '1013410313', '3428'],
     'ParentCompanyName': ['Lenzing AG', 'Lenzing AG', 'Lenzing AG', 'Lenzing AG', 'Lenzing AG', 'NORDGROUP A/S'],
     'FacilityName': ['Lenzing AG', 'Lenzing AG', 'Lenzing AG', 'Lenzing AG', 'Wasserreinhalteverband Lenzing - Lenzing AG', 'NORDGROUP A/S'],
     'StreetName': ['Werkstraße 1', 'Werkstraße 1', 'Werkstraße 1', 'Werkstraße 1', 'Werkstraße 1', 'LINDHOLMVEJ'],
     'BuildingNumber': [np.nan, np.nan, np.nan, np.nan, np.nan, 3],
     'City': ['Lenzing', 'Lenzing', 'Lenzing', 'Lenzing', 'Lenzing', 'NYBORG'],
     'PostalCode': ['4860', '4860', '4860', '4860', '4860', '5800'],
     'CountryCode': ['AT', 'AT', 'AT', 'AT', 'AT', 'DK'],
     'CountryName': ['Austria', 'Austria', 'Austria', 'Austria', 'Austria', 'Denmark'],
     'Lat': [47.966667, 47.966667, 47.966667, 47.966667, 47.966667, 55.3022382837],
     'Long': [13.616667000000001, 13.616667000000001, 13.616667000000001, 13.616667000000001, 13.61666700000000, 10.8151929632],
     'RBDGeoCode': ['AT1000', 'AT1000', 'AT1000', 'AT1000', 'AT1000', 'DK1'],
     'RBDGeoName': ['Danube', 'Danube', 'Danube', 'Danube', 'Danube', 'Jutland and Funen'],
     'NUTSRegionGeoCode': ['AT31', 'AT31', 'AT31', 'AT31', 'AT31', 'FRY1'],
     'NUTSRegionGeoName': ['Upper Austria', 'Upper Austria', 'Upper Austria', 'Upper Austria', 'Upper Austria', 'South Denmark'],
     'RBDSourceCode': ['UNKNOWN', 'UNKNOWN', 'UNKNOWN', 'UNKNOWN', 'UNKNOWN', 'DK1'],
     'RBDSourceName': [np.nan, np.nan, np.nan, np.nan, np.nan, 'Jutland and Funen'],
     'NUTSRegionSourceCode': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'NUTSRegionSourceName': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'NACEMainEconomicActivityCode': ['NACE_1.1:21.11', 'NACE_1.1:21.11', 'NACE_1.1:21.11', 'NACE_1.1:21.11', 'NACE_1.1:90.00', '38.22'],
     'NACEMainEconomicActivityName': ['Manufacture of pulp', 'Manufacture of pulp', 'Manufacture of pulp', 'Manufacture of pulp', 'Sewage and refuse disposal, sanitation and similar activities', 'Treatment and disposal of hazardous waste'],
     'CompetentAuthorityName': ['Not transferred from EPER', 'Not transferred from EPER', 'Not transferred from EPER', 'Not transferred from EPER', 'Not transferred from EPER', 'Miljøstyrelsen'],
     'CompetentAuthorityAddressStreetName': [np.nan, np.nan, np.nan, np.nan, np.nan, 'Tolderlundsvej'],
     'CompetentAuthorityAddressBuildingNumber': [np.nan, np.nan, np.nan, np.nan, np.nan, 5],
     'CompetentAuthorityAddressCity': [np.nan, np.nan, np.nan, np.nan, np.nan, 'Odense'],
     'CompetentAuthorityAddressPostalCode': [np.nan, np.nan, np.nan, np.nan, np.nan, '5000'],
     'CompetentAuthorityAddressCountryCode': ['AT', 'AT', 'AT', 'AT', 'AT', 'DK'],
     'CompetentAuthorityAddressCountryName': ['Austria', 'Austria', 'Austria', 'Austria', 'Austria', 'Denmark'],
     'CompetentAuthorityTelephoneCommunication': ['0', '0', '0', '0', '0', '72544000'],
     'CompetentAuthorityFaxCommunication': ['0', '0', '0', '0', '0', '72544000'],
     'CompetentAuthorityEmailCommunication': [np.nan, np.nan, np.nan, np.nan, np.nan, 'karbn@mst.dk'],
     'CompetentAuthorityContactPersonName': [np.nan, np.nan, np.nan, np.nan, np.nan, 'Kari Bach Nielsen'],
     'ProductionVolumeProductName': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'ProductionVolumeQuantity': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'ProductionVolumeUnitCode': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'ProductionVolumeUnitName': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'TotalIPPCInstallationQuantity': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'OperatingHours': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'TotalEmployeeQuantity': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'WebsiteCommunication': [np.nan, np.nan, np.nan, np.nan, np.nan, 'http://www.nordgroup.eu'],
     'PublicInformation': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'ConfidentialIndicator': [False, False, False, False, False, False],
     'ConfidentialityReasonCode': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'ConfidentialityReasonName': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'ProtectVoluntaryData': [False, False, False, False, False, False],
     'MainIASectorCode': ['EPER_4', 'EPER_4', 'EPER_4', 'EPER_4', 'EPER_5', '5'],
     'MainIASectorName': ['Chemical industry', 'Chemical industry', 'Chemical industry', 'Chemical industry', 'Waste management', 'Waste and waste water management'],
     'MainIAActivityCode': ['EPER_4.1', 'EPER_4.1', 'EPER_4.1', 'EPER_4.1', 'EPER_5.3/5.4', '5.(a)'],
     'MainIAActivityName': ['Basic organic chemicals', 'Basic organic chemicals', 'Basic organic chemicals', 'Basic organic chemicals', 'Disposal of non-hazardous waste and landfills', 'Installations for the recovery or disposal of hazardous waste'],
     'MainIASubActivityCode': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'MainIASubActivityName': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
     'ReportingYear': [2001, 2001, 2001, 2001, 2001, 2016],
     'CoordinateSystemCode': ['EPSG:4326', 'EPSG:4326', 'EPSG:4326', 'EPSG:4326', 'EPSG:4326', 'EPSG:4326'],
     'CoordinateSystemName': ['WGS 84', 'WGS 84', 'WGS 84', 'WGS 84', 'WGS 84', 'WGS 84'],
     'CdrReleased': [20060623000000, 20060623000000, 20060623000000, 20060623000000, 20060623000000, 20190828122729],
     'Published': [20061123000000.0, 20061123000000.0, 20061123000000.0, 20061123000000.0, 20061123000000.0, 20191010010100.0],
     'PollutantReleaseID': [10819, 10820, 10817, 10818, 24207, 3831580],
     'ReleaseMediumCode': ['AIR', 'AIR', 'AIR', 'AIR', 'WATER', 'AIR'],
     'ReleaseMediumName': ['Air', 'Air', 'Air', 'Air', 'Water', 'Air'],
     'PollutantCode': ['PM10', 'SOX', 'CO2 in EPER', 'NOX', 'ZN AND COMPOUNDS', 'CO2'],
     'PollutantName': ['Particulate matter (PM10)', 'Sulphur oxides (SOx/SO2)', 'Carbon dioxide (CO2)', 'Nitrogen oxides (NOx/NO2)', 'Zinc and compounds (as Zn)', 'Carbon dioxide (CO2)'],
     'PollutantGroupCode': ['INORG', 'OTHGAS', 'GRHGAS', 'OTHGAS', 'HEVMET', 'GRHGAS'],
     'PollutantGroupName': ['Inorganic substances', 'Other gases', 'Greenhouse gases', 'Other gases', 'Heavy metals', 'Greenhouse gases'],
     'PollutantCAS': [np.nan, np.nan, '124-38-9', np.nan, np.nan, '124-38-9'],
     'MethodBasisCode': ['E', 'M', 'E', 'M', 'M', 'M'],
     'MethodBasisName': ['Estimated', 'Measured', 'Estimated', 'Measured', 'Measured', 'Measured'],
     'TotalQuantity': [68200.0, 420000.0, 182000000.0, 818000.0, 3210.0, 159000000.0],
     'AccidentalQuantity': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     'UnitCode': ['KGM', 'KGM', 'KGM', 'KGM', 'KGM', 'KGM'],
     'UnitName': ['kilogram', 'kilogram', 'kilogram', 'kilogram', 'kilogram', 'kilogram']
     }

df = pd.DataFrame(data=d)

# The following part is just for testing get_PollutantVolumeChange().
# To construct datatables that are suitable takes very long. So we just use the real data base.

CountryName = ['Germany', 'Austria', 'Switzerland']
ReportingYear = [2014, 2015, 2016, 2017]
PollutantName = ['Carbon dioxide (CO2)']


class Testgetfcts_vis:

    def test_get_PollutantVolume1(self):
        # Test if get_PollutantVolume() returns DataFrame when no Orderparameters are given.
        assert type(ep.get_PollutantVolume(df)) == pd.core.frame.DataFrame

    def test_get_PollutantVolume2(self):
        # Test if get_PollutantVolume() returns DataFrame when FirstOrder parameter is given.
        assert type(ep.get_PollutantVolume(df, FirstOrder='CountryName')) == pd.core.frame.DataFrame

    def test_get_PollutantVolume3(self):
        # Test if get_PollutantVolume() returns DataFrame when SecondOrder parameter is given.
        assert type(ep.get_PollutantVolume(df, FirstOrder='CountryCode', SecondOrder='FacilityReportID')) == pd.core.frame.DataFrame

    def test_get_PollutantVolume4(self):
        # Test if get_PollutantVolume() returns the full sum of PollutionVolume when no OrderParameter is given.
        assert ep.get_PollutantVolume(df).iloc[0, 1] == 342309410.0

    def test_get_PollutantVolume5(self):
        # Test if get_PollutantVolume() sorts to the two CountryNames present in df.
        assert len(ep.get_PollutantVolume(df, FirstOrder='CountryName')) == 2

    def test_get_PollutantVolume6(self):
        # Test if get_PollutantVolume() returns the right values to the two CountryNames present in df.
        assert (ep.get_PollutantVolume(df, FirstOrder='CountryName').iloc[0, 1] == 183309410.0) and (ep.get_PollutantVolume(df, FirstOrder='CountryName').iloc[1, 1] == 159000000.0) == True

    def test_get_PollutantVolume7(self):
        # Test if get_PollutantVolume() sorts to the two CountryNames and two RMN present in df.
        assert len(ep.get_PollutantVolume(df, FirstOrder='CountryName', SecondOrder='ReleaseMediumName')) == 2

    def test_get_PollutantVolume8(self):
        # Test if get_PollutantVolume() sorts to the two CountryNames and two RMN present in df.
        assert len(ep.get_PollutantVolume(df, FirstOrder='CountryName', SecondOrder='ReleaseMediumName').columns) == 3

    def test_get_PollutantVolume9(self):
        # Test if get_PollutantVolume() returns the right values for the different combinations.
        i = 0
        foo = ep.get_PollutantVolume(df, FirstOrder='CountryName', SecondOrder='ReleaseMediumName')
        if foo.iloc[0, 1] == 183306200.0:
            i = i + 1
        if foo.iloc[0, 2] == 3210.0:
            i = i + 1
        if foo.iloc[1, 1] == 159000000.0:
            i = i + 1
        if pd.isnull(foo.iloc[1, 2]):
            i = i + 1
        assert i == 4

    def test_get_PollutantVolumeRel1(self):
        # Test if get_PollutantVolumeRel() returns DataFrame, when no other parameters are called.
        assert type(ep.get_PollutantVolumeRel(df)) == pd.core.frame.DataFrame

    def test_get_PollutantVolumeRel2(self):
        # Test if get_PollutantVolumeRel() returns DataFrame, when FirstOrder is called.
        assert type(ep.get_PollutantVolumeRel(df, FirstOrder='CountryName')) == pd.core.frame.DataFrame

    def test_get_PollutantVolumeRel3(self):
        # Test if get_PollutantVolumeRel() returns DataFrame, when FirstOrder and SecondOrder are called.
        assert type(ep.get_PollutantVolumeRel(df, FirstOrder='CountryCode', SecondOrder='ReleaseMediumName')) == pd.core.frame.DataFrame

    def test_get_PollutantVolumeRel4(self):
        # Test if get_PollutantVolumeRel() returns DataFrame, when FirstOrder, SecondOrder and normtop are called.
        assert type(ep.get_PollutantVolumeRel(df, FirstOrder='CountryCode', SecondOrder='ReleaseMediumName', normtop=['DK', 'Air'])) == pd.core.frame.DataFrame

    def test_get_PollutantVolumeRel4_1(self):
        # Test if get_PollutantVolumeRel() returns DataFrame, when FirstOrder, SecondOrder and normtov are called.
        assert type(ep.get_PollutantVolumeRel(df, FirstOrder='CountryCode', SecondOrder='ReleaseMediumName', normtov=159000000.0)) == pd.core.frame.DataFrame

    def test_get_PollutantVolumeRel5(self):
        # Test if get_PollutantVolumeRel() returns 1.0 for the PollutionVolume when no OrderParameter is given.
        assert ep.get_PollutantVolumeRel(df).iloc[0, 1] == 1.0

    def test_get_PollutantVolumeRel6(self):
        # Test if get_PollutantVolumeRel() sorts to the two CountryNames present in df.
        assert len(ep.get_PollutantVolumeRel(df, FirstOrder='CountryName')) == 2

    def test_get_PollutantVolumeRel7(self):
        # Test if get_PollutantVolumeRel() returns the right values to the two CountryNames present in df.
        assert ((ep.get_PollutantVolumeRel(df, FirstOrder='CountryName').iloc[0, 1] == 1.0) and (ep.get_PollutantVolumeRel(df, FirstOrder='CountryName').iloc[1, 1] == 0.8673859132490798)) == True

    def test_get_PollutantVolumeRel8(self):
        # Test if get_PollutantVolumeRel() returns the right values to the two CountryNames present in df.
        foo = ep.get_PollutantVolumeRel(df, FirstOrder='CountryName', normtop=['Denmark'])
        assert ((foo.iloc[0, 1] == 	1.1528893710691823) and (foo.iloc[1, 1] == 1)) == True

    def test_get_PollutantVolumeRel8_1(self):
        # Test if get_PollutantVolumeRel() returns the right values to the two CountryNames present in df.
        foo = ep.get_PollutantVolumeRel(df, FirstOrder='CountryName', normtov=159000000)
        assert ((foo.iloc[0, 1] == 	1.1528893710691823) and (foo.iloc[1, 1] == 1)) == True

    def test_get_PollutantVolumeRel9(self):
        # Test if get_PollutantVolumeRel() sorts to the two CountryNames and two RMN present in df.
        assert len(ep.get_PollutantVolumeRel(df, FirstOrder='CountryName', SecondOrder='ReleaseMediumName')) == 2

    def test_get_PollutantVolumeRel10(self):
        # Test if get_PollutantVolumeRel() sorts to the two CountryNames and two RMN present in df.
        assert len(ep.get_PollutantVolumeRel(df, FirstOrder='CountryName', SecondOrder='ReleaseMediumName').columns) == 3

    def test_get_PollutantVolumeRel11(self):
        # Test if get_PollutantVolumeRel() returns the right values for the different combinations.
        i = 0
        foo = ep.get_PollutantVolumeRel(df, FirstOrder='CountryName', SecondOrder='ReleaseMediumName')
        if foo.iloc[0, 1] == 1:
            i = i + 1
        if foo.iloc[0, 2] == 1.7511682638121352e-05:
            i = i + 1
        if foo.iloc[1, 1] == 0.8674011026359174:
            i = i + 1
        if pd.isnull(foo.iloc[1, 2]):
            i = i + 1
        assert  i == 4

    def test_get_PollutantVolumeRel12(self):
        # Test if get_PollutantVolumeRel() returns the right values for the different combinations.
        i = 0
        foo = ep.get_PollutantVolumeRel(df, FirstOrder='CountryName',
                                        SecondOrder='ReleaseMediumName', normtov=159000000.0)
        if foo.iloc[0, 1] == 1.152869182389937:
            i = i + 1
        if foo.iloc[0, 2] == 2.018867924528302e-05:
            i = i + 1
        if foo.iloc[1, 1] == 1:
            i = i + 1
        if pd.isnull(foo.iloc[1, 2]):
            i = i + 1
        assert  i == 4

    def test_get_PollutantVolumeRel13(self):
        # Test if get_PollutantVolumeRel() returns the right values for the different combinations.
        i = 0
        foo = ep.get_PollutantVolumeRel(df, FirstOrder='CountryName',
                                        SecondOrder='ReleaseMediumName',
                                        normtop=['Denmark', 'Air'])
        if foo.iloc[0, 1] == 1.152869182389937:
            i = i + 1
        if foo.iloc[0, 2] == 2.018867924528302e-05:
            i = i + 1
        if foo.iloc[1, 1] == 1:
            i = i + 1
        if pd.isnull(foo.iloc[1, 2]):
            i = i + 1
        assert  i == 4

    def test_get_PollutantVolumeChange1(self):
        # Test if get_PollutantVolumeChange() returns DataFrame when no Orderparameters are given.
        assert type(ep.get_PollutantVolumeChange(df)) == pd.core.frame.DataFrame

    def test_get_PollutantVolumeChange2(self):
        # Test if get_PollutantVolumeChange() returns DataFrame when FirstOrder parameter is given.
        assert type(ep.get_PollutantVolumeChange(df, FirstOrder='CountryName')) == pd.core.frame.DataFrame

    def test_get_PollutantVolumeChange3(self):
        # Test if get_PollutantVolumeChange() returns DataFrame when SecondOrder parameter is given.
        assert type(ep.get_PollutantVolumeChange(df, FirstOrder='CountryCode', SecondOrder='FacilityReportID')) == pd.core.frame.DataFrame

    def test_get_ImpurityVolume1(self):
        # Test if get_ImpurityVolume() returns a DataFrame when no keyword arguments are called.
        assert type(ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)')) == pd.core.frame.DataFrame

    def test_get_ImpurityVolume2(self):
        # Test if get_ImpurityVolume() returns a DataFrame when the keyword argument "absolute" is changed.
        assert type(ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)', absolute=True)) == pd.core.frame.DataFrame

    def test_get_ImpurityVolume3(self):
        # Test if get_ImpurityVolume() returns a DataFrame when the keyword argument "FacilityFocus" is changed.
        assert type(ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)', FacilityFocus=False)) == pd.core.frame.DataFrame

    def test_get_ImpurityVolume4(self):
        # Test if get_ImpurityVolume() returns a DataFrame when the keyword argument "impurity" is changed.
        assert type(ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)',
                                          impurity='Particulate matter (PM10)')) == pd.core.frame.DataFrame

    def test_get_ImpurityVolume5(self):
        # Test if get_ImpurityVolume() returns a DataFrame when the keyword argument "FirstOrder" is changed.
        assert type(ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)', FirstOrder='CountryName')) == pd.core.frame.DataFrame

    def test_get_ImpurityVolume6(self):
        # Test if get_ImpurityVolume() returns the right number of entries (dropping water impurities).
        assert len(ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)').columns) == 5

    def test_get_ImpurityVolume7(self):
        # Test if get_ImpurityVolume() sorts the right values to the TotalQuantity.
        assert (ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)').TotalQuantity.iloc[0] == 182000000.0) and (ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)').TotalQuantity.iloc[1] == 159000000.0) == True

    def test_get_ImpurityVolume8(self):
        # Test if get_ImpurityVolume() returns the right values for the entries (normalized)
        foo = ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)')
        i = 0
        if foo.iloc[0, 2] == 68200.0 / 182000000.0:
            i = i + 1
        if foo.iloc[0, 3] == 420000.0 / 182000000.0:
            i = i + 1
        if foo.iloc[0, 4] == 818000.0 / 182000000.0:
            i = i + 1
        if pd.isnull(foo.iloc[1, 2]) and pd.isnull(foo.iloc[1, 3]) and pd.isnull(foo.iloc[1, 4]):
            i = i + 1
        assert i == 4

    def test_get_ImpurityVolume9(self):
        # Test if get_ImpurityVolume() returns the right values for the entries (not normalized)
        foo = ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)', absolute=True)
        i = 0
        if foo.iloc[0, 2] == 68200.0:
            i = i + 1
        if foo.iloc[0, 3] == 420000.0:
            i = i + 1
        if foo.iloc[0, 4] == 818000.0:
            i = i + 1
        if pd.isnull(foo.iloc[1, 2]) and pd.isnull(foo.iloc[1, 3]) and pd.isnull(foo.iloc[1, 4]):
            i = i + 1
        assert i == 4

    def test_get_ImpurityVolume10(self):
        # Test if parameter impurity is called, the data table reduces to the expected structure.
        foo = ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)', impurity='Particulate matter (PM10)')
        assert foo.iloc[0, 2] == 68200.0 / 182000000.0

    def test_get_ImpurityVolume11(self):
        # Test if the the change of FirstOrder works the expected way
        assert list(ep.get_ImpurityVolume(df, 'Carbon dioxide (CO2)', FirstOrder='CountryCode').CountryCode.unique()) == ['AT', 'DK']

    def test_get_ImpurityVolume12(self):
        # Test if parameter FacilityFocus is working the expected way.
        df2 = copy.deepcopy(df)
        df2.loc[5, 'CountryCode'] = 'AT'
        foo1 = ep.get_ImpurityVolume(df2, 'Particulate matter (PM10)', FirstOrder='CountryCode', impurity='Carbon dioxide (CO2)', FacilityFocus=True)
        foo2 = ep.get_ImpurityVolume(df2, 'Particulate matter (PM10)', FirstOrder='CountryCode', impurity='Carbon dioxide (CO2)', FacilityFocus=False)
        assert (foo1.iloc[0, 2] == 182000000.0 / 68200.0) and (foo2.iloc[0, 2] == (182000000.0 + 159000000.0) / 68200.0) == True