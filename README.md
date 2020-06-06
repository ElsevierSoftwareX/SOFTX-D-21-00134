# About
emipy is a package for processing data of pollutant releases and pollutant transfers.
It's main target is to enable a fast output of individual data set requests and to provide visualisation options.

The data are provided by the [European Environment Agency](https://www.eea.europa.eu/data-and-maps/data/member-states-reporting-art-7-under-the-european-pollutant-release-and-transfer-register-e-prtr-regulation-23).

# Documentation
To do


# Quick start
The quickest installation is via the package manager [pip](https://pip.pypa.io/en/stable/):
```bash
pip install emipy
```
Inside the environment one can access the three modules rawdata/filter/plot and respective functions with:
```python
from emipy import module_name

module_name.function_name()
```
At first the data have to be prepared for data requests. Create a folder for your project, and add a folder "rawdata" inside of it. Then execute the following lines with 'path', the project folders path. (Remark: All backslashs have to be doubled)
```python
rawdata.download_url('path')
rawdata.pickle_rawdata('path')
rawdata.merge_frompickle('path')
```
By now there is a data base with complete information which we can call by:
```python
filter.read_db('path')
```
The output is a dataframe which is used as an input for further processing functions.
A short example for a data request and visualisation:
```python
db = filter.read_db('path')  #loads data frame
DE = filter.f_db(db, CountryName='Germany',	PollutantName='Carbon dioxide (CO2)')   #filter for Germany and CO2
plot.plot_PollutantVolume(DE)   #Plots the CO2 release in Germany against the year
```
# Requirements
This package uses [pandas](https://pandas.pydata.org/) and [matplotlib](https://matplotlib.org/).