.. _datainformation:

---------------
Data parameters
---------------

Pollution Data
--------------

The European Environmental Agency (EEA) provides a lot of information that are assigned to the pollution data. There are very intuitiv ones like the name of the country, in that the pollutants are emitted or the year of the emission. 
But there are also very "specialized" ones like the *facility report ID*, or the *NACE-main economic activity code* (an economic classification, performed by Eurostat). Here we provide a short explanation of the most used parameters and how to access them in the f_db() function.
For more detailed information, take a look at the `EEA webpage <https://www.eea.europa.eu/>`_ or the `Eurostat webpage <https://ec.europa.eu/eurostat/de/home>`_.


.. csv-table::
	:header: "Column Name", "Input Data Type", "List Of Entries", "Example"
	:widths: 10, 10, 10, 10
	
	"FacilityReportID", "Integer or List of Integers", ":ref:`facilityreportid`", "f_db(db, FacilityReportID=1856)"
	"CountryName", "String or List of Strings", ":ref:`countryname`", "f_db(db, CountryName='Spain')"
	"ReportingYear", "Integer or List of Integers", ":ref:`reportingyear`", "f_db(db, ReportingYear=2015)"
	"ReleaseMediumName", "String or List of Strings", ":ref:`releasemediumname`", "f_db(db, ReleaseMediumName='Air')"
	"PollutantName", "String or List of Strings", ":ref:`pollutantname`", "f_db(db, PollutantName='Carbon dioxide (CO2)')"
	"PollutantGroupName", "String or List of Strings", ":ref:`pollutantgroupname`", "f_db(db, PollutantGroupName='Inorganic substances')"
	"NACEMainEconomicActivityCode", "String or List of Strings", ":ref:`nacemaineconomicactivitycode`", "f_db(db, NACEMainEconomicActivityCode='25.91')"
	"NUTSRegionGeoCode", "String or List of Strings", ":ref:`nutsregiongeocode`", "f_db(db, NUTSRegionGeoCode='AT11')"
	"ParentCompanyName", "String or List of Strings", ":ref:`parentcompanyname`","f_db(db, ParentCompanyName='Lenzing AG')"
	"FacilityName", "String or List of Strings", ":ref:`facilityname`","f_db(db, FacilityName='Lenzing AG')"
	"City", "String or List of Strings", ":ref:`city`","f_db(db, City='Lenzing')"
	"PostalCode", "String or List of Strings", ":ref:`postalcode`","f_db(db, PostalCode='4860')"
	"CountryCode", "String or List of Strings", ":ref:`countrycode`","f_db(db, CountryCode='AT')"
	"RBDGeoCode", "String or List of Strings", ":ref:`rbdgeocode`","f_db(db, RBDGeoCode='')"
	"RBDGeoName", "String or List of Strings", ":ref:`rbdgeoname`","f_db(db, RBDGeoName='')"
	"NUTSRegionGeoName", "String or List of Strings", ":ref:`nutsregiongeoname`","f_db(db, NUTSRegionGeoName='')"
	"NACEMainEconomicActivityName", "String or List of Strings", ":ref:`nacemaineconomicactivityname`","f_db(db, NACEMainEconomicActivityName='')"
	"MainIASectorCode", "String or List of Strings", ":ref:`mainiasectorcode`","f_db(db, MainIASectorCode='')"
	"MainIASectorName", "String or List of Strings", ":ref:`mainiasectorname`","f_db(db, MainIASectorName='')"
	"MainIAActivityCode", "String or List of Strings", ":ref:`mainiaactivitycode`","f_db(db, MainIAActivityCode='')"
	"MainIAActivityName", "String or List of Strings", ":ref:`mainiaactivityname`","f_db(db, MainIAActivityName='')"
	"PollutantReleaseID", "String or List of Strings", ":ref:`pollutantreleaseid`","f_db(db, PollutantReleaseID='')"
	"ReleaseMediumCode", "String or List of Strings", ":ref:`releasemediumcode`","f_db(db, ReleaseMediumCode='')"
	"PollutantCode", "String or List of Strings", ":ref:`pollutantcode`","f_db(db, PollutantCode='')"
	"PollutantGroupCode", "String or List of Strings", ":ref:`pollutantgroupcode`","f_db(db, PollutantGroupCode='')"


Map Data
--------

| The map data are provided by `Eurostat <https://ec.europa.eu/eurostat/de/web/gisco/geodata/reference-data/administrative-units-statistical-units/nuts#nuts21>`_. The maps always show a complete view of Europe, but there are different parameters, that change the layout of the visualisation.
| There are two levels where you can choose parameters. These are first the download of the map data and second the load procedure into your session.
| During initialisation, emipy downloads, for every NUTS version, the map data with resolution 1:10 million. For storage size reasons, not all map files are downloaded. You can download additional map data with download_MapFiles(). See :ref:`tut5` for the correct usage.

+------------------------+------------------+-------------+
| Statistical Unit       | Publication Date | Resolution  |
+========================+==================+=============+
| NUTS 2021              | 01/02/2020       | 1:1 Million |
|                        |                  +-------------+
|                        |                  | 1:3 Million |
|                        |                  +-------------+
|                        |                  | 1:10 Million|
|                        |                  +-------------+
|                        |                  | 1:20 Million|
|                        |                  +-------------+
|                        |                  | 1:60 Million|
+------------------------+------------------+-------------+
| NUTS 2016              | 14/03/2019       | 1:1 Million |
|                        |                  +-------------+
|                        |                  | 1:3 Million |
|                        |                  +-------------+
|                        |                  | 1:10 Million|
|                        |                  +-------------+
|                        |                  | 1:20 Million|
|                        |                  +-------------+
|                        |                  | 1:60 Milion |
+------------------------+------------------+-------------+
| NUTS 2013              | 03/12/2015       | 1:1 Million |
|                        |                  +-------------+
|                        |                  | 1:3 Million |
|                        |                  +-------------+
|                        |                  | 1:10 Million|
|                        |                  +-------------+
|                        |                  | 1:20 Milion |
|                        |                  +-------------+
|                        |                  | 1:60 Milion |
+------------------------+------------------+-------------+
| NUTS 2010              | 01/12/2012       | 1:1 Million |
|                        |                  +-------------+
|                        |                  | 1:3 Million |
|                        |                  +-------------+
|                        |                  | 1:10 Million|
|                        |                  +-------------+
|                        |                  | 1:20 Million|
|                        |                  +-------------+
|                        |                  | 1:60 Million|
+------------------------+------------------+-------------+
| NUTS 2006              | 01/12/2008       | 1:1 Million |
|                        |                  +-------------+
|                        |                  | 1:3 Million |
|                        |                  +-------------+
|                        |                  | 1:10 Million|
|                        |                  +-------------+
|                        |                  | 1:20 Million|
|                        |                  +-------------+
|                        |                  | 1:60 Million|
+------------------------+------------------+-------------+
| NUTS 2003              | 03/12/2005       | 1:1 Million |
|                        |                  +-------------+
|                        |                  | 1:3 Million |
|                        |                  +-------------+
|                        |                  | 1:10 Million|
|                        |                  +-------------+
|                        |                  | 1:20 Million|
+------------------------+------------------+-------------+

| The following sub categories are downloaded for every publication year and resolution:

+------------------------+------------------+-------------+
| Spatial Type           | NUTS_LVL         | Projection  |
+========================+==================+=============+
| BN                     | None             | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 0          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 1          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 2          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 3          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
+------------------------+------------------+-------------+
| LB                     | None             | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 0          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 1          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 2          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 3          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
+------------------------+------------------+-------------+
| RG                     | None             | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 0          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 1          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 2          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
|                        +------------------+-------------+
|                        | Level 3          | 3035        |
|                        |                  +-------------+
|                        |                  | 3857        |
|                        |                  +-------------+
|                        |                  | 4326        |
+------------------------+------------------+-------------+

| When loading the map data into your session, you can choose from the parameters *resolution*, *spatialtype*, *NUTS_LVL*, *m_year* and *projection*. *Resolution* and *m_year* do correspond to the above given resolutions and NUTS versions. 
| *Spatialtype* has three different options: RG (region), BD (boundary) and LB. For the emipy visualisation functions, the information, stored in the RG file are necessary. Therefore it is chosen by default. Mainly for layout configuration, you can choose BD to only show the borders.
Take into acount, that for the higher NUTS levels, the file just stores new occuring borders. So you would have to plot level 0, 1, 2 and then 3 on top of each other (or level None) to get a map with the complete level 3 borders. LB displays points for the regions.
| *NUTS_LVL* is the Level of the NUTS-classification. You can choose from no level at all up to level 0, 1, 2 and 3. If you put the level on *None*, the loaded shp file contains all objects from the other levels.
| *Projection* refers to the spatial projetion of the displayed map. You can choose from EPSG: 4326, 3035, 3857. When the data is loaded into the session you can also transfer the corresponding reference system (crs) with geopandas or emipy.
| The default setting is:

.. code-block:: python

	read_mb(path=None, Resolution='10M', spatialtype='RG', NUTS_LVL=0, m_year=2016, projection=4326)

