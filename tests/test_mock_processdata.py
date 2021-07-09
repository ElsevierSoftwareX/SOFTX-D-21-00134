# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:31:17 2021

@author: f-ove

This is a testscript for the module processdata of the package emipy.
"""

import emipy as ep
import pandas as pd
import numpy as np


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
     'NACEMainEconomicActivityCode': ['03.11', 'NACE_1.1:21.11', ['38.22', '21.11'], '35.12', 'NACE_1.1:90.00', '38.22'],
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


class Testgetfcts:

    def test_get_NACECode_filter1(self):
        # Test if NaceCode filter has the data type dict.
        NACE = ep.get_NACECode_filter()
        assert type(NACE) == dict

    def test_get_NACECode_filter2(self):
        # Test if NaceCode filter has the right number of entries
        NACE = ep.get_NACECode_filter()
        assert len(NACE) == 69

    def test_get_NACECode_filter3(self):
        # Test if NaceCode filter returns list, if specify is called.
        NACE = ep.get_NACECode_filter(specify='animal production')
        assert type(NACE) == list

    def test_get_NACECode_filter_industry(self):
        # test if get_NACECode_filter_industry() returns a list.
        NACE = ep.get_NACECode_filter_industry(group='cem')
        assert type(NACE) == list

    def test_get_CountryList1(self):
        # Test if get_CountryList returns the right data type.
        assert type(ep.get_CountryList(df)) is list

    def test_get_CountryList2(self):
        # Test if get_CountryList returns the right length of entries for the standard df.
        assert len(ep.get_CountryList(df)) == 2

    def test_get_YearList1(self):
        # Test if get_YearList returns the right data type.
        assert type(ep.get_YearList(df)) is list

    def test_get_YearList2(self):
        # Test if get_YearList returns the right length of entries for the standard df.
        assert len(ep.get_YearList(df)) == 2

    def test_get_PollutantList1(self):
        # Test if get_PollutantList returns the right data type.
        assert type(ep.get_PollutantList(df)) is list

    def test_get_PollutantList2(self):
        # Test if get_PollutantList returns the right length of entries for the standard df.
        assert len(ep.get_PollutantList(df)) == 5


class Testchangefcts:

    def test_change_NACECode_filter1(self):
        # Test if NACECode_filter addition works.
        ep.change_NACECode_filter(add={'metalmanufaction': '24.51,24.52,24.53,24.54'})
        assert ep.get_NACECode_filter(specify='metalmanufaction') == ['24.51', '24.52', '24.53', '24.54']

    def test_change_NACECode_filter2(self):
        # Test if NACECode_filter subtraction works.
        ep.change_NACECode_filter(sub={'metalmanufaction': '24.51,24.52,24.53,24.54'})
        assert len(ep.get_NACECode_filter()) == 69

    def test_change_NACECode_filter3(self):
        # Test if NACECode-filter total replacement works. This is not so smooth,
        # because if nothing would happen, we can't distinguish from succesfull test.
        foo = ep.get_NACECode_filter()
        ep.change_NACECode_filter(total=foo)
        assert len(ep.get_NACECode_filter()) == 69

    def test_change_unit1(self):
        # Test if change_unit() returns DataFrame, when no new unit is given.
        assert type(ep.change_unit(df)) == pd.core.frame.DataFrame

    def test_change_unit01(self):
        # Test if the number conversion  of change_unit() is working.
        # The 0.000000000003 is strange, but i think it is an pythonic problem with float.
        assert ep.change_unit(df, unit='kilogram').TotalQuantity.sum() == 342309410.0

    def test_change_unit02(self):
        # Test if the UnitCode conversion is working.
        foo = ep.change_unit(df, unit='kilogram')
        foo = foo.UnitCode == 'KGM'
        assert foo.all()

    def test_change_unit03(self):
        # Test if the UnitName conversion is working.
        foo = ep.change_unit(df, unit='kilogram')
        foo = foo.UnitName == 'kilogram'
        assert foo.all()

    def test_change_unit2(self):
        # Test if the number conversion  of change_unit() is working.
        # The 0.000000000003 is strange, but i think it is an pythonic problem with float.
        assert ep.change_unit(df, unit='ton').TotalQuantity.sum() == 342309.41000000003

    def test_change_unit3(self):
        # Test if the UnitCode conversion is working.
        foo = ep.change_unit(df, unit='ton')
        foo = foo.UnitCode == 'TN'
        assert foo.all()

    def test_change_unit4(self):
        # Test if the UnitName conversion is working.
        foo = ep.change_unit(df, unit='ton')
        foo = foo.UnitName == 'ton'
        assert foo.all()

    def test_change_unit5(self):
        # Test if the number conversion  of change_unit() is working.
        # The 0.000000000003 is strange, but i think it is an pythonic problem with float.
        assert ep.change_unit(df, unit='kiloton').TotalQuantity.sum() == 342.30941000000003

    def test_change_unit6(self):
        # Test if the UnitCode conversion is working.
        foo = ep.change_unit(df, unit='kiloton')
        foo = foo.UnitCode == 'KTN'
        assert foo.all()

    def test_change_unit7(self):
        # Test if the UnitName conversion is working.
        foo = ep.change_unit(df, unit='kiloton')
        foo = foo.UnitName == 'kiloton'
        assert foo.all()

    def test_change_unit8(self):
        # Test if the number conversion  of change_unit() is working.
        # The 0.000000000003 is strange, but i think it is an pythonic problem with float.
        assert ep.change_unit(df, unit='megaton').TotalQuantity.sum() == 0.34230941000000003

    def test_change_unit9(self):
        # Test if the UnitCode conversion is working.
        foo = ep.change_unit(df, unit='megaton')
        foo = foo.UnitCode == 'MTN'
        assert foo.all()

    def test_change_unit10(self):
        # Test if the UnitName conversion is working.
        foo = ep.change_unit(df, unit='megaton')
        foo = foo.UnitName == 'megaton'
        assert foo.all()

    def test_change_unit11(self):
        # Test if the number conversion  of change_unit() is working.
        # The 0.000000000003 is strange, but i think it is an pythonic problem with float.
        assert ep.change_unit(df, unit='gigaton').TotalQuantity.sum() == 0.00034230941

    def test_change_unit12(self):
        # Test if the UnitCode conversion is working.
        foo = ep.change_unit(df, unit='gigaton')
        foo = foo.UnitCode == 'GTN'
        assert foo.all()

    def test_change_unit13(self):
        # Test if the UnitName conversion is working.
        foo = ep.change_unit(df, unit='gigaton')
        foo = foo.UnitName == 'gigaton'
        assert foo.all()

    def test_change_unit14(self):
        # Test if the number conversion  of change_unit() is working.
        # The 0.000000000003 is strange, but i think it is an pythonic problem with float.
        assert ep.change_unit(df, unit='gram').TotalQuantity.sum() == 342309410000.00003

    def test_change_unit15(self):
        # Test if the UnitCode conversion is working.
        foo = ep.change_unit(df, unit='gram')
        foo = foo.UnitCode == 'GM'
        assert foo.all()

    def test_change_unit16(self):
        # Test if the UnitName conversion is working.
        foo = ep.change_unit(df, unit='gram')
        foo = foo.UnitName == 'gram'
        assert foo.all()

    def test_change_RenameDict1(self):
        # Test if change_RenameDict(add) does add one Rename element.
        # Improvable becuase we rely on the function rename_columns() to control the outcome.
        try:
            ep.change_RenameDict(add={'Lat': 'Latitude'})
            foo = ep.rename_columns(df)
            foo1 = 'Latitude' in list(foo.columns)
        finally:
            ep.change_RenameDict(reset=True)
        assert foo1

    def test_change_RenameDict2(self):
        # Test if change_RenameDict(add) does subtract one Rename element.
        # Improvable becuase we rely on the function rename_columns() to control the outcome.
        try:
            ep.change_RenameDict(sub={'ReportingYear': 'Year'})
            foo = ep.rename_columns(df)
            foo1 = 'Year' not in list(foo.columns)
        finally:
            ep.change_RenameDict(reset=True)
        assert foo1

    def test_change_RenameDict3(self):
        # Test if change_RenameDict(total) does replace all Rename elements.
        # Improvable becuase we rely on the function rename_columns() to control the outcome.
        try:
            ep.change_RenameDict(total={'Lat': 'Latitude', 'Long': 'Longitude'})
            foo = ep.rename_columns(df)
            foo1 = ('Longitude' in list(foo.columns)) and ('Latitude' in list(foo.columns)) and ('Year' not in list(foo.columns))
        finally:
            ep.change_RenameDict(reset=True)
        assert foo1

    def test_change_RenameDict4(self):
        # Test if change_RenameDict(reset) does reset all Rename elements.
        # Improvable becuase we rely on the function rename_columns() to control the outcome.
        try:
            ep.change_RenameDict(add={'Lat': 'Latitude'})
            ep.change_RenameDict(sub={'ReportingYear': 'Year'})
            ep.change_RenameDict(reset=True)
            foo = ep.rename_columns(df)
            foo1 = ('Latitude' not in list(foo.columns)) and ('Year' in list(foo.columns))
        finally:
            ep.change_RenameDict(reset=True)
        assert foo1

    def Test_rename_columns1(self):
        # Test if rename_columns() returns a DataFrame.
        assert type(ep.rename(df)) == pd.core.frame.DataFrame

    def Test_rename_columns2(self):
        # test if rename_columns() changes the column names.
        foo = ep.rename(df)
        foo1 = ('Year' in list(foo.columns)) and ('Country' in list(foo.columns)) and ('NUTSID' in list(foo.columns)) and ('NACEID' in list(foo.columns)) and ('NACEName' in list(foo.columns)) and ('Pollutant' in list(foo.columns)) and ('Unit' in list(foo.columns))
        assert foo1

    def test_change_ColumnsOfInterest1(self):
        # Test if change_ColumnsOfInterest(add) does add one element in the config file.
        # Improvable because we rely on row_reduction() to control the outcome.
        try:
            ep.change_ColumnsOfInterest(add='FacilityReportID')
            foo = ep.row_reduction(df)
            foo1 = ('FacilityReportID' in list(foo.columns))
        finally:
            ep.change_ColumnsOfInterest(reset=True)
        assert foo1

    def test_change_ColumnsOfInterest2(self):
        # Test if change_ColumnsOfInterest(sub) does subtract one element in the config file.
        # Improvable because we rely on row_reduction() to control the outcome.
        try:
            ep.change_ColumnsOfInterest(sub='CountryCode')
            foo = ep.row_reduction(df)
            foo1 = ('CountryCode' not in list(foo.columns))
        finally:
            ep.change_ColumnsOfInterest(reset=True)
        assert foo1

    def test_change_ColumnsOfInterest3(self):
        # Test if change_ColumnsOfInterest(total) does replace all elements in the config file.
        # Improvable because we rely on row_reduction() to control the outcome.
        try:
            ep.change_ColumnsOfInterest(total=['FacilityReportID', 'CountryName'])
            foo = ep.row_reduction(df)
            foo1 = ('FacilityReportID' in list(foo.columns)) and ('CountryName' in list(foo.columns)) and ('Lat' not in list(foo.columns))
        finally:
            ep.change_ColumnsOfInterest(reset=True)
        assert foo1

    def test_change_ColumnsOfInterest4(self):
        # Test if change_ColumnsOfInterest(reset) does reset all elements in the config file.
        # Improvable because we rely on row_reduction() to control the outcome.
        try:
            ep.change_ColumnsOfInterest(total=['FacilityReportID', 'Country'])
            ep.change_ColumnsOfInterest(reset=True)
            foo = ep.row_reduction(df)
        finally:
            ep.change_ColumnsOfInterest(reset=True)
        assert len(list(foo.columns)) == 12

    def test_row_reduction1(self):
        # Test if row_reduction() returns DataFrame.
        assert type(ep.row_reduction(df)) == pd.core.frame.DataFrame

    def test_row_reduction2(self):
        # Test if row_reduction() returns the right columns.
        foo = ep.row_reduction(df)
        assert ['CountryCode', 'CountryName', 'Lat', 'Long', 'NUTSRegionGeoCode',
                'NACEMainEconomicActivityCode', 'NACEMainEconomicActivityName', 'ReportingYear',
                'PollutantReleaseID', 'PollutantName', 'TotalQuantity', 'UnitCode'] == list(foo.columns)


"""
class Testperform_NACETransition:

    def test_perform_NACETransition1(self):
        # test if perform_NACETransition() returns a DataFrame
        foo = ep.perform_NACETransition(df)
        assert type(foo) == pd.core.frame.DataFrame

    def test_perform_NACETransition3(self):
        # Test if perform_NACETransition() transforms all entries from df into the corresponding NACE2 entries.
        foo = ep.perform_NACETransition(df).NACEMainEconomicActivityCode
        i = 0
        if foo[0] == ['17.11']:
            i = i + 1
        if foo[1] == ['17.11']:
            i = i + 1
        if foo[2] == ['17.11']:
            i = i + 1
        if foo[3] == ['17.11']:
            i = i + 1
        if foo[4] == ['37.00', '38.11', '38.12', '38.21', '38.22', '39.00', '81.29']:
            i = i + 1
        if foo[5] == '38.22':
            i = i + 1
        assert i == 6
"""


class Testf_db:

    def test_f_db00(self):
        #
        assert type(ep.f_db(df)) == pd.core.frame.DataFrame

    def test_f_db01(self):
        #
        assert len(ep.f_db(df)) == 6

    def test_f_db1(self):
        #
        assert type(ep.f_db(df, FacilityReportID=1857)) == pd.core.frame.DataFrame

    def test_f_db2(self):
        #
        assert len(ep.f_db(df, FacilityReportID=1857)) == 1

    def test_f_db3(self):
        #
        assert type(ep.f_db(df, CountryName='Austria')) == pd.core.frame.DataFrame

    def test_f_db4(self):
        #
        assert len(ep.f_db(df, CountryName='Austria')) == 5

    def test_f_db5(self):
        #
        assert type(ep.f_db(df, ReportingYear=2016)) == pd.core.frame.DataFrame

    def test_f_db6(self):
        #
        assert len(ep.f_db(df, ReportingYear=2016)) == 1

    def test_f_db7(self):
        #
        assert type(ep.f_db(df, ReleaseMediumName='Water')) == pd.core.frame.DataFrame

    def test_f_db8(self):
        #
        assert len(ep.f_db(df, ReleaseMediumName='Water')) == 1

    def test_f_db9(self):
        #
        assert type(ep.f_db(df, PollutantName='Particulate matter (PM10)')) == pd.core.frame.DataFrame

    def test_f_db10(self):
        #
        assert len(ep.f_db(df, PollutantName='Particulate matter (PM10)')) == 1

    def test_f_db11(self):
        #
        assert type(ep.f_db(df, PollutantGroupName='Greenhouse gases')) == pd.core.frame.DataFrame

    def test_f_db12(self):
        #
        assert len(ep.f_db(df, PollutantGroupName='Greenhouse gases')) == 2

    def test_f_db13(self):
        #
        assert type(ep.f_db(df, NACEMainEconomicActivityCode='38.22')) == pd.core.frame.DataFrame

    def test_f_db14(self):
        # Check for the argument NACEMainEconomicActivityCode, when value is never in list
        assert len(ep.f_db(df, NACEMainEconomicActivityCode='35.12')) == 1
        
    def test_f_db14_2(self):
        # when value is in list and in single entry
        assert len(ep.f_db(df, NACEMainEconomicActivityCode='38.22')) == 2

    def test_f_db14_3(self):
        # when value is just in list
        assert len(ep.f_db(df, NACEMainEconomicActivityCode='21.11')) == 1

    def test_f_db14_4(self):
        #
        assert len(ep.f_db(df, NACEMainEconomicActivityCode=['35.12'])) == 1
        
    def test_f_db14_5(self):
        #
        assert len(ep.f_db(df, NACEMainEconomicActivityCode=['38.22'])) == 2

    def test_f_db14_6(self):
        #
        assert len(ep.f_db(df, NACEMainEconomicActivityCode=['21.11'])) == 1

    def test_f_db14_7(self):
        #
        assert len(ep.f_db(df, NACEMainEconomicActivityCode=['21.11', '35.12', '03.11'])) == 3

    def test_f_db14_8(self):
        #
        assert len(ep.f_db(pd.DataFrame(columns=list(df.columns)), NACEMainEconomicActivityCode=['21.11'])) == 0

    def test_f_db15(self):
        #
        assert type(ep.f_db(df, NUTSRegionGeoCode='AT31')) == pd.core.frame.DataFrame

    def test_f_db16(self):
        #
        assert len(ep.f_db(df, NUTSRegionGeoCode='AT31')) == 5

    def test_f_db17(self):
        #
        assert type(ep.f_db(df, ParentCompanyName='Lenzing AG')) == pd.core.frame.DataFrame

    def test_f_db18(self):
        #
        assert len(ep.f_db(df, ParentCompanyName='Lenzing AG')) == 5

    def test_f_db19(self):
        #
        assert type(ep.f_db(df, FacilityName='Wasserreinhalteverband Lenzing - Lenzing AG')) == pd.core.frame.DataFrame

    def test_f_db20(self):
        #
        assert len(ep.f_db(df, FacilityName='Wasserreinhalteverband Lenzing - Lenzing AG')) == 1

    def test_f_db21(self):
        #
        assert type(ep.f_db(df, City='NYBORG')) == pd.core.frame.DataFrame

    def test_f_db22(self):
        #
        assert len(ep.f_db(df, City='NYBORG')) == 1

    def test_f_db23(self):
        #
        assert type(ep.f_db(df, PostalCode='4860')) == pd.core.frame.DataFrame

    def test_f_db24(self):
        #
        assert len(ep.f_db(df, PostalCode='4860')) == 5

    def test_f_db25(self):
        #
        assert type(ep.f_db(df, CountryCode='DK')) == pd.core.frame.DataFrame

    def test_f_db26(self):
        #
        assert len(ep.f_db(df, CountryCode='DK')) == 1

    def test_f_db27(self):
        #
        assert type(ep.f_db(df, RBDGeoCode='AT1000')) == pd.core.frame.DataFrame

    def test_f_db28(self):
        #
        assert len(ep.f_db(df, RBDGeoCode='AT1000')) == 5

    def test_f_db29(self):
        #
        assert type(ep.f_db(df, RBDGeoName='Jutland and Funen')) == pd.core.frame.DataFrame

    def test_f_db30(self):
        #
        assert len(ep.f_db(df, RBDGeoName='Jutland and Funen')) == 1

    def test_f_db31(self):
        #
        assert type(ep.f_db(df, NACEMainEconomicActivityName='Sewage and refuse disposal,'
                                                             ' sanitation and similar activities')) == pd.core.frame.DataFrame

    def test_f_db32(self):
        #
        assert len(ep.f_db(df, NACEMainEconomicActivityName='Sewage and refuse disposal,'
                                                            ' sanitation and similar activities')) == 1

    def test_f_db33(self):
        #
        assert type(ep.f_db(df, MainIASectorCode='EPER_5')) == pd.core.frame.DataFrame

    def test_f_db34(self):
        #
        assert len(ep.f_db(df, MainIASectorCode='EPER_5')) == 1

    def test_f_db35(self):
        #
        assert type(ep.f_db(df, MainIASectorName='Waste management')) == pd.core.frame.DataFrame

    def test_f_db36(self):
        #
        assert len(ep.f_db(df, MainIASectorName='Waste management')) == 1

    def test_f_db37(self):
        #
        assert type(ep.f_db(df, MainIAActivityCode='EPER_5.3/5.4')) == pd.core.frame.DataFrame

    def test_f_db38(self):
        #
        assert len(ep.f_db(df, MainIAActivityCode='EPER_5.3/5.4')) == 1

    def test_f_db39(self):
        #
        assert type(ep.f_db(df, MainIAActivityName='Disposal of non-hazardous waste and landfills')) == pd.core.frame.DataFrame

    def test_f_db40(self):
        #
        assert len(ep.f_db(df, MainIAActivityName='Disposal of non-hazardous waste and landfills')) == 1

    def test_f_db41(self):
        #
        assert type(ep.f_db(df, PollutantReleaseID=10820)) == pd.core.frame.DataFrame

    def test_f_db42(self):
        #
        assert len(ep.f_db(df, PollutantReleaseID=10820)) == 1

    def test_f_db43(self):
        #
        assert type(ep.f_db(df, ReleaseMediumCode='WATER')) == pd.core.frame.DataFrame

    def test_f_db44(self):
        #
        assert len(ep.f_db(df, ReleaseMediumCode='WATER')) == 1

    def test_f_db45(self):
        #
        assert type(ep.f_db(df, PollutantCode='SOX')) == pd.core.frame.DataFrame

    def test_f_db46(self):
        #
        assert len(ep.f_db(df, PollutantCode='SOX')) == 1

    def test_f_db47(self):
        #
        assert type(ep.f_db(df, PollutantGroupCode='OTHGAS')) == pd.core.frame.DataFrame

    def test_f_db48(self):
        #
        assert len(ep.f_db(df, PollutantGroupCode='OTHGAS')) == 2

    def test_f_db49(self):
        #
        assert type(ep.f_db(df, ExclaveExclude=True)) == pd.core.frame.DataFrame

    def test_f_db50(self):
        #
        assert len(ep.f_db(df, ExclaveExclude=True)) == 5

    """
    One could build in a test series, which controls, if the according column has the right entries.
    """

    def test_f_db51(self):
        # Test if ReturnUnkown = True really returns a DataFrame.
        assert type(ep.f_db(df, ReturnUnknown=True)) == pd.core.frame.DataFrame