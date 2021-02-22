# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 12:33:42 2021

@author: f-ove

This is a script for generating the parameter list files for the documentation. You need a working emipy project.
"""
import emipy as ep
import os





"""""""""""
The following path has to be adapted to where ever you need the files. In the best way, they get automatically generated into the documentation directory ..\docs\source:
"""""""""""
path = r'C:\Witthaut\repository\2021-01-19\docs\source'















db = ep.read_db()

itemlist=['FacilityReportID', 'CountryName', 'ReportingYear', 'ReleaseMediumName', 'PollutantName', 'PollutantGroupName', 'NACEMainEconomicActivityCode', 'NUTSRegionGeoCode', 'ParentCompanyName', 'FacilityName', 'City', 'PostalCode', 'CountryCode', 'RBDGeoCode', 'RBDGeoName', 'NUTSRegionGeoName', 'NACEMainEconomicActivityName', 'MainIASectorCode', 'MainIASectorName', 'MainIAActivityCode', 'MainIAActivityName', 'PollutantReleaseID', 'ReleaseMediumCode', 'PollutantCode', 'PollutantGroupCode']

for j in itemlist:
    itemG = j
    itemk = itemG.lower()



    foo1 = list(db[itemG].unique())


    newfile = []
    counter = 0
    newfile.append('.. _' + itemk + ':'+'\n')
    newfile.append('\n')
    newfile.append(itemG+'\n')
    foo2 = ''
    for i in range(len(itemG)):
        foo2 = foo2 + '-'
    newfile.append(foo2+'\n')
    newfile.append('\n')

    for item in foo1:
        if type(item) is not str:
            item = str(item)
        newfile.append('| ' + item + ',\n')

    newfile[-1] = newfile[-1][:-2]     


    with open(os.path.join(path, itemk+'list.rst'), 'w+', encoding='utf-8')as f:
        for i in newfile:
            f.write(i)
