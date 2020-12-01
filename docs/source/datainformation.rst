---------------
Data parameters
---------------

Pollution Data
--------------

The European Environmental Agency (EEA) provides a lot of information that are assigned to the pollution data. There are very intuitiv ones like the name of the country, in that the pollutants are emitted or the year of the emission. 
But there are also very "specialized" ones like the facility report ID, or the NACE-main economic activity code (an economic classification, performed by Eurostat). Here we provide a short explanation of the most used parameters and how to access them in the f_db() function.
For more detailed information, take a look at the `EEA webpage <https://www.eea.europa.eu/>`_ or the `Eurostat webpage <https://ec.europa.eu/eurostat/de/home>`_ .


.. csv-table:: 
	:widths: 50 50 50 50
	
	column name , input data type , list of entries , example
	CountryName , String or List of Strings , test1 , data = f_db(db, CountryName='Spain')


| :ref:`countrynamelist`
| :ref:`tut5`
