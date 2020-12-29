.. _tut5:

Special Features
================

| There are several functions that enhance the usage of emipy. In this tutorial we take a look at these functions and work threw their use cases.

Change root path
----------------

| At first let's take a look at the configuration options of emipy. When initialise an emipy project, we defined a path to the root of the project. This path is stored in a config file and is used when the data is loaded in a session or auto exported to the export folder.
| When you use emipy in another environment than the one in which you initialised emipy, your root path is not set to the projects folder. If you want to continue your work in this project, or simply dont want to download all data again, you can adapt this path.

.. code-block:: python

    import emipy as ep

    ep.change_rootpath(r'Your\individual\path\to\your\project')

Downloading additional map data
-------------------------------

| During the initialization, emipy downloads `map data <https://ec.europa.eu/eurostat/de/web/gisco/geodata/reference-data/administrative-units-statistical-units/nuts#nuts21>`_ from Eurostat. There is not just one map, but a lot of different ways to visualize the countries.
| Emipy downloads the predefined set with resolution factor 1:10 Million, but you can download additional map data if wanted. For the download you can choose from the resolution (1:1,3,10,20,60 Million) and emipy downloads the map data for all publication years, projections and NUTS-LVL into the projects MappingData folder. With read_mb() you can make further choices of the way, your map is diplayed. For more details see :ref:`datainformation`.
| The Resolution can be an Integer or a list of Integers which values has to be the resolution factor. You can put the parameter clear to True, to clear the MappingData folder before downloading. This prevents doublication of data and reduces the memory size.
	
.. code-block:: python

	example_res =[3,60]
	ep.download_MapFiles(r'The\path\to\the\root\of\your\project', Resolution=example_res, clear=True)

Change Units
------------

| When working with the pollution data, you might want to change the unit of the emission. The function *change_Unit()* reads the current unit for all entries and recalculates the emission value to the new unit and stores the new unit code in the DataFrame.

.. code-block:: python

	data2 = ep.change_Unit(data1, Unit='megaton')

Data Table Adaption
-------------------

| For the export you might not need all of the 73 columns and want to increase your overview. You can exclude columns and reduce the columns to those which you are interested in.
| The function *row_reduction()* uses information from the config file to determine which columns are defined as columns of interest. You can change these configuration with *change_ColumnsOfInterest(). You can use the paramter "total" to change the complete list, "add" to add column names or "sub" to substract from present column names. If you put the parameter reset on True, you reset the list of column names to the initial state.

.. code-block:: python

	total=['CountryCode', 'CountryName']
	ep.change_ColumnsOfInterest(total=total, add=None, sub=None, reset=False)
	data4 = ep.row_reduction(data3)
	ep.change_ColumnsOfInterest(total=None, add='Lat', sub=None, reset=False)
	data5 = ep.row_reduction(data3)
	ep.change_ColumnsOfInterest(total=None, add=None, sub='CountryCode', reset=False)
	data6 = ep.row_reduction(data3)
	ep.change_ColumnsOfInterest(total=None, add=None, sub=None, reset=True)
	data7 = ep.row_reduction(data3)

| There is also an option to rename the columns at large scale. The working principle is the same as the column reduction but you have to insert dicts instead of strings or lists.

.. code-block :: python

	addition={'Lat': 'Latitude'}
	ep.change_RenameDict(total=None, add=addition, sub=None, reset=False)
	data8 = ep.rename_columns(data3)

	ep.change_RenameDict(total=None, add=None, sub=None, reset=True)
	data9 = ep.rename_columns(data3)


Emission information
--------------------

| So far you have produced a filtered data base and plots of these data base. But perhaps you want to get the information of your plot in form of a data table. 

.. code-block :: python

	data10 = ep.get_PollutantVolume(data2, FirstOrder='ReportingYear')
	data11 = ep.get_PollutantVolume_rel(data2, FirstOrder='ReportingYear')
	data12 = ep.get_PollutantVolumeChange(data2, FirstOrder='ReportingYear')

| In comparison to your data base, this table has summed up all emissions for your order parameter. The usage of the order parameter is the same as in the plot functions.

NACE-Code selection
-------------------

| The economical classification of the entries with the NACE-Code is not consistent over time. The European Union performed a revision of the NACE-Classification NACE 1.1 to NACE 2. In consequence, the entries for the years 2001 and 2004 are encoded in the old classification, while the newer entries are encoded by NACE 2.
| Emipy provides a function that performes an transition of the old codes to the new, based on the `transition tables <https://ec.europa.eu/eurostat/de/web/nace-rev2/correspondence_tables>`_, provided by Eurostat.

.. code-block :: python

	db = ep.perform_NACETransition(db)

| The transition does not allow an unique assignment of new codes, which is why the new codes may be stored as list of multiple codes. In a consequence, entries might pass your filter, but are not truly part of your requested data. You might want to check for these entries, if they really are part of your economic field.
| You can finde the NACE-Codes in the `NACE Rev.2 <https://ec.europa.eu/eurostat/documents/portlet_file_entry/3859598/KS-RA-07-015-EN.PDF.pdf/dd5443f5-b886-40e4-920d-9df03590ff91>`_ starting at page 63. Choosing the right code enables you to filter for your request. NACEMainEconomicActivityCode needs a string with the complete NACE Code like '01.46' or list of these Codes.

.. code-block :: python

	data13 = ep.f_db(db, NACEMainEconomicActivityCode='35.11')

| Some groups of NACE codes are stored in the config file. You can access them with get_NACECode_filter(). If the parameter specify is None, which it is by default, you receive a list of dictionaries which have the NACE Codes as list corresponding to the key name. You can put specify to on of the keys to receive the value, the list of NACE Codes.

.. code-block :: python

	print(ep.get_NACECode_filter())
	NACECode = ep.get_NACECode_filter(specify = 'Animal production')
	data14 = ep.f_db(db, NACEMainEconomicActivityCode=NACECode)

| You can create your own NACE-Code lists with change_NACECode_filter(). This works very much like change_RenameDict(). You can add and subtract single key/value pairs, or replace the complete dictionary. For the right syntax, make sure your codes are 5 characters long and seperated by a comma.

.. code-block :: python

	ep.change_NACECode_filter(add={'metalmanufaction':'24.51,24.52,24.53,24.54'})
	ep.change_NACECode_filter(sub={'metalmanufaction':'24.51,24.52,24.53,24.54'})

