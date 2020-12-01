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
	
	"CountryName", "String or List of Strings", ":ref:`countrynamelist`", "f_db(db, CountryName=Spain)"
	"ReportingYear", "Integer or list of Integers", "test2", "data"


.. csv-table:: a title
   :header: "column name", "input data type", "list of entries"
   :widths: 20, 20, 10

   "CountryName", "String or List of Strings", "test1"
   "Smith", "John, Junior", 20


| 
| :ref:`tut5`


.. csv-table:: a title
   :header: "name", "firstname", "age"
   :widths: 20, 20, 10

   "Smith", "John", 40
   "Smith", "John, Junior", 20
   

.. list-table::
    :name: tab-beispieltabelle
    :widths: 50 50 50
    :header-rows: 0

    * - Art der Einträge
      - Eigenschaft 1
      - Eigenschaft 2
    * - Gegenstand 1
      - eckig
      - rot
    * - Gegenstand 2
      - rund
      - blau