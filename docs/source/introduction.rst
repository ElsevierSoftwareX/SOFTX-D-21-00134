Introduction and quick start guide
==================================

=============
Introduction
=============    
| Emipy is a python package to analyze industrial emission sources within Europe.
| The package accesses data from the `European Environmental Agency <https://www.eea.europa.eu/data-and-maps/data/member-states-reporting-art-7-under-the-european-pollutant-release-and-transfer-register-e-prtr-regulation-23>`_ and `Eurostat <https://ec.europa.eu/eurostat/de/web/gisco/geodata/reference-data/administrative-units-statistical-units/nuts#nuts21>`_  and allows to generate desired data sets. Data sets can be filtered with clearly structured build-in functions. Furthermore, functions are provided that allow a quick visualization of the data.

=============
Installation    
=============

Requirements
------------

Emipy  requires:

1. Python (tested for version 3.7)    
2. Additional add-on modules:
    1. matplotlib
    2. requests
    3. configparser
    4. pandas
    5. geopandas
    6. descartes
    7. openpyxl
    8. ruamel.yaml
3. The emipy package itself    

Installation & Initialisation
----------------------------- 

If you are not familiar with Python yet we suggest you follow our step by step installation guide:

1. Download and install the Anaconda distribution from the `Anaconda page <https://www.anaconda.com/products/individual>`_.
2. Create a new environment. For this:
    1. Start the console "Anaconda Prompt"
    2. Create the environment via executing the following line in "Anaconda Prompt":

    	``>conda create -n emipy python=3.7 matplotlib requests configparser pandas geopandas descartes ruamel.yaml openpyxl``
    3. Enter 'y' if asked to install all required packages.
    4. Activate the environment with:
	| ``>conda activate emipy``
	| The environment is active when your active code line starts with "(emipy)" instead of "(base)".
    5. install emipy via:
	  ``>pip install emipy``
3. Initialize a new emipy project. For this:
    1. Open a Python skript in the Anaconda Prompt console via entering:
        ``>python``
    2. Execute the following lines to load emipy and execute the function `init_emipy_project()` which will create a folder structure at the given path and download all necessary data.
        .. note::
	        You have to change the path to the location, where you want the data to be stored! The inialization process may take a few minutes as large amounts of data is downloaded. Please be patient and let it run until finished completely.

	.. note::
	    If you are using Windows, the path needs a special format. Python reads ``"\"`` as an escape,
	    like ``"\n"`` for new line. You can either use ``"\\"`` or "/" instead of a single ``"\"`` or, alternatively you
	    can put a "r" before the string to convert to a raw string.
	    Python needs the single mark quotes around the path to recognize it as a String.
	    Keep that in mind, for all further applications of the emipy functions!

	| ``>>>import emipy as ep``
	| ``>>>ep.init_emipy_project('<some_path>')``
	| ``>>>exit()``
    | Here, <some_path> is the name of the directory, where you want to put the data.
    | If the initialization function completed its task it prints the message 'The Initialization process is completed.'
    | If you do not receive this message check for typos and repeat executing the function.

You can also download the emipy package via the package manager pip:

    .. note::
        In principle you could also install emipy using only pip but it is advised to install the dependencies
        separately, since some packages (e.g. geopandas) don't install correctly in Windows when using only the version
        installed from pypi. In this case, you can install geopandas' dependency Fiona from the channel conda-forge.

    ``>pip install emipy``

Keep in mind that you have to install the list of packages given above. Execute point 3 from the step by step guide to initialize a new project.
    


=============
Quick start
=============

1. Start the IDE of your preference. If you are new, just execute ``>jupyter notebook`` in the Anaconda Prompt console. This should open a window in your browser. Click on "New" and select Python3.
   (`Here <https://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Running%20Code.ipynb>`_ is a short example for the Jupyter Notebook usage. You can also look at the `documentation <https://jupyter-notebook.readthedocs.io/en/latest/notebook.html>`_)
2. Import the emipy module:
    | ``import emipy as ep``
3. Load the data into your current session with:
    | ``db = ep.read_db()``
    | ``mb = ep.read_mb()``
4. and display it with:
    | ``db.head()``
    | ``mb.plot()``

.. note::
    Use one Notebook box for each display line (``db.head()`` and ``mb.plot()``). Jupyter Notebook displays just the last object of the box. Therefore it just shows the plot of mb but not the table db, if you write both into the same box.
