---------------
Data parameters
---------------

Pollution Data
--------------

The European Environmental Agency (EEA) provides a lot of information that are assigned to the pollution data. There are very intuitiv ones like the name of the country, in that the pollutants are emitted or the year of the emission. 
But there are also very "specialized" ones like the facility report ID, or the NACE-main economic activity code (an economic classification, performed by Eurostat). Here we provide a short explanation of the most used parameters and how to access them in the f_db() function.
For more detailed information, take a look at the `EEA webpage <https://www.eea.europa.eu/>`_ or the `Eurostat webpage <https://ec.europa.eu/eurostat/de/home>`_ .


.. csv-table::
	:header: "column name", "input data type", "list of entries", "example"
	:widths: 50, 50, 50, 50
	
	"FacilityReportID", "Integer or List of Integers", ":ref:`facilityreportidlist`", "f_db(db, FacilityReportID=1856)"
	"CountryName", "String or List of Strings", ":ref:`countrynamelist`", "f_db(db, CountryName='Spain')"
	"ReportingYear", "Integer or List of Integers", ":ref:`reportingyearlist`", "f_db(db, ReportingYear=2015)"
	"ReleaseMediumName", "String or List of Strings", ":ref:`releasemediumnamelist`", "f_db(db, ReleaseMediumName='Air')"
	"PollutantName", "String or List of Strings", ":ref:`pollutantnamelist`", "f_db(db, PollutantName='Carbon dioxide (CO2)')"
	"PollutantGroupName", "String or List of Strings", ":ref:`pollutantgroupnamelist`", "f_db(db, PollutantGroupName='Inorganic substances')"


