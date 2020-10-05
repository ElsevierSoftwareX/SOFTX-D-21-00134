Tutorials
=========

Generating data sets
--------------------

| At first import the module processdata and read the data base.
| The programm stored the path to the project initialisation and automatically searches for the data there and loads it. You can aswell read explicit databases. For this, give the function `read_db()` the path in form of a String as an argument.

.. code-block:: python

    from emipy import processdata

    db = processdata.read_db()
    db.head()

.. raw:: html

    <div style="overflow-x:auto;">
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>FacilityReportID</th>
          <th>PollutantReleaseAndTransferReportID</th>
          <th>FacilityID</th>
          <th>NationalID</th>
          <th>ParentCompanyName</th>
          <th>FacilityName</th>
          <th>StreetName</th>
          <th>BuildingNumber</th>
          <th>City</th>
          <th>PostalCode</th>
          <th>...</th>
          <th>PollutantName</th>
          <th>PollutantGroupCode</th>
          <th>PollutantGroupName</th>
          <th>PollutantCAS</th>
          <th>MethodBasisCode</th>
          <th>MethodBasisName</th>
          <th>TotalQuantity</th>
          <th>AccidentalQuantity</th>
          <th>UnitCode</th>
          <th>UnitName</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>1856</td>
          <td>1</td>
          <td>5763</td>
          <td>1013410312</td>
          <td>Lenzing AG</td>
          <td>Lenzing AG</td>
          <td>Werkstraße 1</td>
          <td>NaN</td>
          <td>Lenzing</td>
          <td>4860</td>
          <td>...</td>
          <td>Particulate matter (PM10)</td>
          <td>INORG</td>
          <td>Inorganic substances</td>
          <td>NaN</td>
          <td>E</td>
          <td>Estimated</td>
          <td>68200.0</td>
          <td>0.0</td>
          <td>KGM</td>
          <td>kilogram</td>
        </tr>
        <tr>
          <th>1</th>
          <td>1856</td>
          <td>1</td>
          <td>5763</td>
          <td>1013410312</td>
          <td>Lenzing AG</td>
          <td>Lenzing AG</td>
          <td>Werkstraße 1</td>
          <td>NaN</td>
          <td>Lenzing</td>
          <td>4860</td>
          <td>...</td>
          <td>Sulphur oxides (SOx/SO2)</td>
          <td>OTHGAS</td>
          <td>Other gases</td>
          <td>NaN</td>
          <td>M</td>
          <td>Measured</td>
          <td>420000.0</td>
          <td>0.0</td>
          <td>KGM</td>
          <td>kilogram</td>
        </tr>
        <tr>
          <th>2</th>
          <td>1856</td>
          <td>1</td>
          <td>5763</td>
          <td>1013410312</td>
          <td>Lenzing AG</td>
          <td>Lenzing AG</td>
          <td>Werkstraße 1</td>
          <td>NaN</td>
          <td>Lenzing</td>
          <td>4860</td>
          <td>...</td>
          <td>Carbon dioxide (CO2)</td>
          <td>GRHGAS</td>
          <td>Greenhouse gases</td>
          <td>124-38-9</td>
          <td>E</td>
          <td>Estimated</td>
          <td>182000000.0</td>
          <td>0.0</td>
          <td>KGM</td>
          <td>kilogram</td>
        </tr>
        <tr>
          <th>3</th>
          <td>1856</td>
          <td>1</td>
          <td>5763</td>
          <td>1013410312</td>
          <td>Lenzing AG</td>
          <td>Lenzing AG</td>
          <td>Werkstraße 1</td>
          <td>NaN</td>
          <td>Lenzing</td>
          <td>4860</td>
          <td>...</td>
          <td>Nitrogen oxides (NOx/NO2)</td>
          <td>OTHGAS</td>
          <td>Other gases</td>
          <td>NaN</td>
          <td>M</td>
          <td>Measured</td>
          <td>818000.0</td>
          <td>0.0</td>
          <td>KGM</td>
          <td>kilogram</td>
        </tr>
        <tr>
          <th>4</th>
          <td>1857</td>
          <td>1</td>
          <td>5764</td>
          <td>1013410313</td>
          <td>Lenzing AG</td>
          <td>Wasserreinhalteverband Lenzing - Lenzing AG</td>
          <td>Werkstraße 1</td>
          <td>NaN</td>
          <td>Lenzing</td>
          <td>4860</td>
          <td>...</td>
          <td>Zinc and compounds (as Zn)</td>
          <td>HEVMET</td>
          <td>Heavy metals</td>
          <td>NaN</td>
          <td>M</td>
          <td>Measured</td>
          <td>3210.0</td>
          <td>0.0</td>
          <td>KGM</td>
          <td>kilogram</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 73 columns</p>
    </div>


| A list of possible column names to filter for is displayed with:

.. code-block:: python

    db.columns

.. parsed-literal::

    Index(['FacilityReportID', 'PollutantReleaseAndTransferReportID', 'FacilityID',
           'NationalID', 'ParentCompanyName', 'FacilityName', 'StreetName',
           'BuildingNumber', 'City', 'PostalCode', 'CountryCode', 'CountryName',
           'Lat', 'Long', 'RBDGeoCode', 'RBDGeoName', 'NUTSRegionGeoCode',
           'NUTSRegionGeoName', 'RBDSourceCode', 'RBDSourceName',
           'NUTSRegionSourceCode', 'NUTSRegionSourceName',
           'NACEMainEconomicActivityCode', 'NACEMainEconomicActivityName',
           'CompetentAuthorityName', 'CompetentAuthorityAddressStreetName',
           'CompetentAuthorityAddressBuildingNumber',
           'CompetentAuthorityAddressCity', 'CompetentAuthorityAddressPostalCode',
           'CompetentAuthorityAddressCountryCode',
           'CompetentAuthorityAddressCountryName',
           'CompetentAuthorityTelephoneCommunication',
           'CompetentAuthorityFaxCommunication',
           'CompetentAuthorityEmailCommunication',
           'CompetentAuthorityContactPersonName', 'ProductionVolumeProductName',
           'ProductionVolumeQuantity', 'ProductionVolumeUnitCode',
           'ProductionVolumeUnitName', 'TotalIPPCInstallationQuantity',
           'OperatingHours', 'TotalEmployeeQuantity', 'WebsiteCommunication',
           'PublicInformation', 'ConfidentialIndicator',
           'ConfidentialityReasonCode', 'ConfidentialityReasonName',
           'ProtectVoluntaryData', 'MainIASectorCode', 'MainIASectorName',
           'MainIAActivityCode', 'MainIAActivityName', 'MainIASubActivityCode',
           'MainIASubActivityName', 'ReportingYear', 'CoordinateSystemCode',
           'CoordinateSystemName', 'CdrReleased', 'Published',
           'PollutantReleaseID', 'ReleaseMediumCode', 'ReleaseMediumName',
           'PollutantCode', 'PollutantName', 'PollutantGroupCode',
           'PollutantGroupName', 'PollutantCAS', 'MethodBasisCode',
           'MethodBasisName', 'TotalQuantity', 'AccidentalQuantity', 'UnitCode',
           'UnitName'],
          dtype='object')


| If you are interested in e.g. the countries that occur in your database you can receive a list with the `get_columnname()` functions. For more information take a look at the :ref:`processdata module description <moduleprocessdata>`.

.. code-block:: python

    processdata.get_Countrylist(db)

.. parsed-literal::

    ['Austria',
     'Belgium',
     'Cyprus',
     'Czech Republic',
     'Germany',
     'Denmark',
     'Estonia',
     'Spain',
     'Finland',
     'France',
     'Greece',
     'Hungary',
     'Ireland',
     'Italy',
     'Lithuania',
     'Luxembourg',
     'Latvia',
     'Malta',
     'Netherlands',
     'Norway',
     'Poland',
     'Portugal',
     'Sweden',
     'Slovenia',
     'Slovakia',
     'United Kingdom',
     'Iceland',
     'Serbia',
     'Romania',
     'Bulgaria',
     'Switzerland',
     'Croatia']


| The actual filtering happens with the function `f_db()`. You have to specifiy the database that you want to filter and the column names and column values that you want to filter for.

.. note::

    The following lines only create the DataFrame and do not display it. To display the data table, execute e.g. `data1.head()`.

| Let's filter for pollution in Germany:

.. code-block:: python

    data1 = processdata.f_db(db, CountryName='Germany')

| If you want to filter for multiple values in one column you have to insert a list.


.. code-block:: python

    data2 = processdata.f_db(db, CountryName=['Germany', 'Switzerland', 'Austria'])

| You can filter for multiple columns at the same time:

.. code-block:: python

    CountryName = ['Germany', 'Austria', 'Switzerland']
    ReportingYear = [2014, 2015, 2016,2017]
    PollutantName = ['Carbon dioxide (CO2)', 'Methane (CH4)']

    data3 = processdata.f_db(db, CountryName=CountryName, ReportingYear=ReportingYear, PollutantName=PollutantName)

.. note::
    Take into account that numbers are not from type string and therefore do not need quote markers around them.

| For the precise values use the `get_xy()` function. You can also filter step by step. For this you would have to insert the filtered database into the filter function.
| 
| You can adjust two more arguments in `f_db()`.
| If you want to take a look at the continent Europe, you have to exclude Exclaves that belong to European countries, like French Guiana.

.. code-block:: python

    data4 = processdata.f_db(db, ExclaveExclude=True)

| If you put returnna on True the function returns a data table, which contains all entries that would be sorted out in the filter process but just do not possess enough information to pass the filter. If this table is empty, then it is a good sign.

.. code-block:: python

    data5 = processdata.f_db(db, returnna=True)

| Now you can generate your own data set of interest with a few lines of code. Since db is a DataFrame object, you can use all `pandas <https://pandas.pydata.org/docs/index.html>`_ functions as well, to personalize your data generation.
| 
| As a last step you might want to save your just created data tables. Depending on the storage data type, you can use different functions. These functions have the same arguments as the pandas export functions, but automatically store the data in the export file of your emipy project, if there is no path given.

.. code-block:: python

    processdata.export_db_topickle(data1, filename='Deutschland.pkl')
    processdata.export_db_tocsv(data2, filename='Germanspeakingarea.csv')
    processdata.export_db_toexcel(data3, filename='CO2andMethan.xlsx')


Visualize data sets
-------------------

| Let's start with generating a filtered data set:

.. code-block:: python

    from emipy import processdata
    from emipy import visualizedata

    db = processdata.read_db()

    CountryName = ['Germany', 'Austria', 'Switzerland']
    ReportingYear = [2014, 2015, 2016, 2017]
    PollutantName = ['Carbon dioxide (CO2)']

    data1 = processdata.f_db(db, CountryName=CountryName, ReportingYear=ReportingYear, PollutantName=PollutantName)

| Now we can plot the CO2 volume against the reporting years:

.. code-block:: python

    visualizedata.plot_PollutantVolume(data1, FirstOrder='ReportingYear')

.. image:: ./pictures/Tut2pic1.svg
    :width: 80%
    :align: center
    :alt: Tut2pic1isit?

| As you can see, the first order is equivalent to the x-axis of the plot and the first parameter that the data is sorted by.
| We can now take a deeper look into our data and sort it additionally by another order:

.. code-block:: python

    visualizedata.plot_PollutantVolume(data1, FirstOrder='ReportingYear', SecondOrder='CountryName')

.. image:: ./pictures/Tut2pic2.svg
    :width: 80%
    :align: center
    :height: 400px
    :alt: Tut2pic2

| Keep in mind, that the plot functions do not filter the data. If you would like to plot e.g. just the output from Austria you would have to create a new data set, and specifiy this as input in a new plot:

.. code-block:: python

    data2 = processdata.f_db(data1, CountryName='Austria')
    visualizedata.plot_PollutantVolume(data2, FirstOrder='ReportingYear')

.. image:: ./pictures/Tut2pic3.svg
    :width: 80%
    :align: center
    :height: 400px
    :alt: Tut2pic3

| Additionaly to the pollutant emmisions, you can analyse the change of the emmission over time. As this calculation needs information of the year before, the function can only provide this result for all but the first year in the data table.

.. code-block:: python

    visualizedata.plot_PollutantVolumeChange(data1, FirstOrder='ReportingYear', SecondOrder='CountryName')

.. image:: ./pictures/Tut2pic4.svg
    :width: 80%
    :align: center
    :height: 400px
    :alt: Tut2pic4

| As a third option, you can plot normalised values. With the parameter norm, you can specify the First Order value, that the data is normed to. For e good example we create a new data table:

.. code-block:: python

    CountryName = ['Germany', 'Austria', 'Switzerland']
    ReportingYear = [2014, 2015, 2016, 2017]
    PollutantName=['Zinc and compounds (as Zn)', 'Nickel and compounds (as Ni)']

    data2 = processdata.f_db(db,CountryName=CountryName, ReportingYear=ReportingYear, PollutantName=PollutantName)

    visualizedata.plot_PollutantVolume_rel(data2, FirstOrder='PollutantName', SecondOrder='ReportingYear')

.. image:: ./pictures/Tut2pic5.svg
    :width: 80%
    :align: center
    :height: 400px
    :alt: Tut2pic5

| If you want to customize the layout of the graphs, you can enter the known arguments of the `PyPlot package <https://matplotlib.org/3.1.1/tutorials/index.html>`_ into the functions. Since the functions return a matplotlib.axes object, you can access and modify the individual elements of the plots like in PyPlot.

.. code-block:: python

    import matplotlib.pyplot as plt

    fig1, fig1_axes = plt.subplots(2, 2)
    fig1_axes[0,0] = visualizedata.plot_PollutantVolume(data1, FirstOrder='ReportingYear', ax=fig1_axes[0,0])
    fig1_axes[1,0] = visualizedata.plot_PollutantVolume_rel(data1, FirstOrder='ReportingYear', ax=fig1_axes[1,0])
    fig1_axes[0,1] = visualizedata.plot_PollutantVolumeChange(data1, FirstOrder='ReportingYear', ax=fig1_axes[0,1])
    fig1_axes[1,1] = visualizedata.plot_PollutantVolume(data1, FirstOrder='ReportingYear', ax=fig1_axes[1,1], color='r')
    fig1_axes[0,0].set_xlabel('Year', fontsize=20)
    fig1.set_figheight(12)
    fig1.set_figwidth(15)
    fig1_axes[1,1].set(xlabel='Year', ylabel='Emission [kg]')
    plt.show()

.. image:: ./pictures/Tut2pic6.svg
    :width: 80%
    :align: center
    :height: 400px
    :alt: Tut2pic6

| As a last step you might want to save the plots you have created. This can be done with the `savefig()` function of PyPlot. Another method is to use the `export_fig()` function of emipy. This function will automatically save the function to the export folder of your emipy project. All selection arguments of the `savefig()` function are implemented.

.. code-block:: python

    visualizedata.export_fig(fig1, filename='CO2_Daten.png', dpi=80, bbox_inches=#tight')


Using map data
--------------

| The first thing that you will realise is, that there is not just one data set for the map like in the pollution data. There are different parameters that change the layout of the maps, therefore when reading the map data you can choose from these parameters. Nevertheless, there is a presetting, that gives you a map by the hand.  

.. code-block:: python

    from emipy import processdata
    from emipy import visualizedata
    mb = processdata.read_mb()
    mb.plot()

| Of special interest is the parameter "NUTS_LVL", which is the level of the NUTS-ID's which are the codes for categorized regions. See the `Eurostat <https://ec.europa.eu/eurostat/de/web/nuts/nuts-maps>`_ page for more information.  
| We start with the following set up:

.. code-block:: python

    NUTS_LVL = '1'
    Resolution = '01M'
    datatype = 'shp'
    projection = '4326'
    spatialtype = 'RG'
    m_year = '2021'

    mb = processdata.read_mb(Resolution=Resolution, spatialtype=spatialtype, NUTS_LVL=NUTS_LVL, m_year=m_year, projection=projection)
    mb.plot()

.. image:: ./pictures/Tut3pic1.svg
    :width: 80%
    :align: center
    :alt: Tut3pic1

| The filtering happens with the function f_mb(). Depending on the NUTS level, you can filter for countries or the corresponding NUTS-ID. Additionally, there is the argument ExclaveExclude which you can put on true to exclude the exclaves and map continental europe.  
| To map e.g. North Rhine-Westphalia you have to know, that the NUTS-ID is 'DEA' and can use it as a filter. You can look up the NUTS_ID' at the link above or take a look in the DataFrame mb.

.. code-block:: python

    mapdata1 = processdata.f_mb(mb, ExclaveExclude=True)
    mapdata1.plot()

.. image:: ./pictures/Tut3pic2.svg
    :width: 80%
    :align: center
    :alt: Tut3pic2

.. code-block:: python

    mapdata2 = processdata.f_mb(mb, CNTR_CODE='DE')
    mapdata2.plot()

.. image:: ./pictures/Tut3pic3.svg
    :width: 80%
    :align: center
    :alt: Tut3pic3

.. code-block:: python

    mapdata3 = processdata.f_mb(mb, NUTS_ID=['DEA'], CNTR_CODE='DE')
    mapdata3.plot(aspect='equal')

.. image:: ./pictures/Tut3pic4.svg
    :width: 80%
    :align: center
    :alt: Tut3pic4

| To combine map data and pollution data you have two options. You can plot the pollution sources on the map or create a colormap of the pollution in the regions.
| Let's start with mapping the CO2 sources in Germany and Austria in the year 2017.

.. code-block:: python

    import matplotlib.pyplot as plt

    CountryName = ['Germany', 'Austria']
    ReportingYear = [2017]
    PollutantName = ['Carbon dioxide (CO2)']

    data4 = processdata.f_db(db,CountryName=CountryName, ReportingYear=ReportingYear, PollutantName=PollutantName)
    mapdata4 = processdata.f_mb(mb, CNTR_CODE=['DE','AT'])

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1, 1, 1)
    #ax1 = mapdata1.plot(ax=ax1, color='lightgrey')
    ax1 = visualizedata.map_PollutantSource(data4, mapdata4, markersize=200, ax=ax1)
    fig1.set_figheight(10)
    fig1.set_figwidth(10)

.. image:: ./pictures/Tut3pic5.svg
    :width: 80%
    :align: center
    :alt: Tut3pic5

| If you uncomment everything, you'll get a complete map of Europe in light grey without emission sources, while Germany and Austria are highlighted and show their sources.
| For the `map_PollutantSource()` you have to insert the data and map set. You can choose the markersize, which is the size of the maximal output. The other sources are normalized to this value. If markersize is put on zero or is not given at all, all marker have the same size.  
| 
| `map_PollutantSource()` returns three objects, therefore you have to specifiy which one you want to return. [0] returns the axes-object, or the plot. [1] returns the DataFrame with all data that are plotted. [2] returns the DataFrame with all data that is not plotted. This might happen, when the coordinates of the data is bad and not inside the regions or not given at all.  
| You can also plot different pollutants and color them differently with the parameter 'category'.

.. code-block:: python

    CountryName = ['Germany', 'Austria']
    ReportingYear = [2017]
    PollutantName = ['Carbon dioxide (CO2)', 'Nitrogen oxides (NOx/NO2)']

    data5 = processdata.f_db(db,CountryName=CountryName, ReportingYear=ReportingYear, PollutantName=PollutantName)
    mapdata5 = processdata.f_mb(mb, CNTR_CODE=['DE','AT'])

    fig2 = plt.figure()
    ax1 = fig2.add_subplot(1, 1, 1)
    ax1 = visualizedata.map_PollutantSource(data5, mapdata5, markersize=200, category='PollutantName', ax=ax1)
    fig2.set_figheight(10)
    fig2.set_figwidth(10)

.. image:: ./pictures/Tut3pic6.svg
    :width: 80%
    :align: center
    :alt: Tut3pic6

| To plot the emission of specific regions you can use the `map_PollutantRegions()` function. In the following example we plot the emission of CO2 in Austria on NUTS-level 2.

.. code-block:: python

    NUTS_LVL = '2'
    Resolution = '01M'
    datatype = 'shp'
    projection = '4326'
    spatialtype = 'RG'
    m_year = '2021'

    mb = processdata.read_mb(Resolution=Resolution, spatialtype=spatialtype, NUTS_LVL=NUTS_LVL, m_year=m_year, projection=projection)

    CountryName = ['Austria']
    ReportingYear = [2017]
    PollutantName = ['Carbon dioxide (CO2)']

    data6 = processdata.f_db(db,CountryName=CountryName, ReportingYear=ReportingYear, PollutantName=PollutantName)
    mapdata6 = processdata.f_mb(mb, CNTR_CODE='AT')

    fig3 = plt.figure()
    ax1 = fig3.add_subplot(1, 1, 1)
    ax1 = visualizedata.map_PollutantRegions(data6, mapdata6, ax=ax1, legend=True)
    fig3.set_figheight(10)
    fig3.set_figwidth(10)

.. image:: ./pictures/Tut3pic7.svg
    :width: 80%
    :align: center
    :alt: Tut3pic7

| Since the returns of the functions are Axes-objects, you can use PyPlot functions and arguments to change the layout. You can also use `Geopandas <https://geopandas.org/>`_ to personalize the plot generation because the map data is stored as a GeoDataFrame.