Special Features
----------------

| There are several functions that enhance the usage of emipy. In this tutorial we take a look at these functions and work threw their use cases.
|
| At first let's take a look at the configuration options of emipy. When initialise an emipy project, we defined a path to the root of the project. This path is stored in a config file and is used when the data is loaded in a session or auto exported to the export folder.
| When you use emipy in another environment, than the one in which you initialised emipy, your root path is not set to the projects folder. If you want to continue your work in this project, or simply dont want to download all data again, you can adapt this path.

.. code-block:: python

    import emipy as ep

	ep.change_rootpath(r'Your\individual\path\to\your\project')

| During the initialization, emipy downloads `map data <https://ec.europa.eu/eurostat/de/web/gisco/geodata/reference-data/administrative-units-statistical-units/nuts#nuts21>`_ from Eurostat. There is not just one map, but a lot of different ways to visualize the countries.
| Emipy downloads the predefined set with resolution factor 1:10 Million, but you can download additional map data if wanted. For the download you can choose from the resolution (1:1,3,10,20,60 Million) and emipy downloads the map data for all publication years, projections and NUTS-LVL into the projects MappingData folder. With read_mb() you can make further choices of the way, your map is diplayed.
| The Resolution can be a Integer or a list of Integers which values has to be the resolution factor. You can put the parameter clear to True, to clear the MappingData folder before downloading. This prevents doublication of data and reduces the memory size.
	
.. code-block:: python

	example_res =[3,60]
	ep.download_MapFiles(r'The\path\to\the\root\of\your\project', Resolution=example_res, clear=True)

| When working with the pollution data you might want to change the unit of the emission. The function change_Unit() reads the current unit for all entries and recalculates the emission value to the new unit and stores the unit in the DataFrame.

.. code-block:: python

	data2 = ep.change_Unit(data1, Unit='megaton')

| For the export you might not need all of the 73 columns and want to increase your overview. You can exclude columns and reduce the columns to those which you are interested in.
| The function row_reduction() uses information from the config file to determine which columns are defined as columns of interest. You can change these configuration with change_ColumnsOfInterest(). You can use the paramter "total" to change the complete list, "add" to add column names or "sub" to substract from present column names. If you put the parameter reset on True, you reset the list of column names to the initial state.

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





