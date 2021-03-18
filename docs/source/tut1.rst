Generating data sets
====================

| At first import the package emipy and read the data base.
| The programm stored the path to the project initialisation and automatically searches for the data there and loads it. You can aswell read explicit databases. For this, give the function `read_db()` the path in form of a String as an argument.


.. code-block:: python

    import emipy as ep

    db = ep.read_db()
    db.head()

| 

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

| 

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


| If you are interested in e.g. the countries that occur in your database you can receive a list with the `get_Countrylist()` function. There are more `get_xy()` functions to access the information in your data base. For more information take a look at the :ref:`processdata module description <moduleprocessdata>`.


.. code-block:: python

    ep.get_CountryList(db)

| 

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

    | The following lines only create the DataFrame and do not display it. To display the data table, execute e.g. `data1.head()`.
    | For a better overview, you can use `data = ep.row_reduction(db)`. The new DataFrame is reduced to a list of columns. This list can be adjusted.

| Let's filter for pollution in Germany:

.. code-block:: python

    data1 = ep.f_db(db, CountryName='Germany')

| If you want to filter for multiple values in one column you have to insert a list.


.. code-block:: python

    data2 = ep.f_db(db, CountryName=['Germany', 'Switzerland', 'Austria'])

| You can filter for multiple columns at the same time:

.. code-block:: python

    CountryName = ['Germany', 'Austria', 'Switzerland']
    ReportingYear = [2014, 2015, 2016,2017]
    PollutantName = ['Carbon dioxide (CO2)', 'Methane (CH4)']

    data3 = ep.f_db(db, CountryName=CountryName, ReportingYear=ReportingYear, PollutantName=PollutantName)

.. note::
    Take into account that numbers are not from type string and therefore do not need quote markers around them.

| For the precise values use the `get_xy()` function or alternativley, you can take a look at the :ref:`parameter table <datainformation>`.
| You can also filter step by step. For this you would have to insert the filtered database into the filter function.
| 
| You can adjust two more arguments in `f_db()`.
| If you want to take a look at the continent Europe, you have to exclude Exclaves that belong to European countries, like French Guiana.

.. code-block:: python

    data4 = ep.f_db(db, ExclaveExclude=True)

| If you put *ReturnUnknown* on True the function returns a data table, which contains all entries that would be sorted out in the filter process but just do not possess enough information to pass the filter. If this table is empty, then it is a good sign.

.. code-block:: python

    data5 = ep.f_db(db, CountryName='Germany', ReturnUnknown=True)

| Now you can generate your own data set of interest with a few lines of code. Since db is a DataFrame object, you can use all `pandas <https://pandas.pydata.org/docs/index.html>`_ functions as well, to personalize your data generation.
