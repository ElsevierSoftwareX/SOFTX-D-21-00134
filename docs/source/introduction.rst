Introduction and quick start guide
==================================

=============
Introduction
=============    
emipy is a python package to analyse industrial emission sources within Europe. <br>
The package accesses data from the European Environmental Agency and Eurostat, and allows to generate a desired data set with clearly structured filter functions. Furthermore, functions are provided that allow a quick visualization of the data.

=============
Installation    
=============

Requirements
------------

Emipy  requires: <br>
1. Python, (tested for version 3.7)    
2. Additional add-on modules:
    1. matplotlib
    2. requests
    3. configparser
    4. pandas
    5. geopandas
    6. descartes   
3. The emipy package itself    

Installation & initialisation
----------------------------- 

For beginners of the Python world, we provide a step by step installation guide: <br>
1. Download and install the Anaconda distribution from [here](https://www.anaconda.com/products/individual).
2. Create a new environment. For this:
    1. Download the environment.yml file from [here](https://gitlab-public.fz-juelich.de/s.morgenthaler/emipy/-/tree/UploadforPresentation).
    2. Start the console "Anaconda Prompt"
    3. Create the environment with the information from the just downloaded file via executing this line in the console (adapt the path to the file at the end!):
    	``>conda env create -f C:\Users\User1\Downloads\environment.yml``
    4. Enter 'y' when asked to install all required packages.
    5. Activate the environment with:
	``>conda activate emipy``
3. Initialize a new emipy project. For this:
    1. Open a Python skript in the Anaconda Prompt console via entering:
        ``>python``
    2. Execute the following lines to load the module rawdata and execute the init_emipy_project() function which will download all necessary data and create a folder structure to the given path. Replace 'path' with the path where you want to store all data.
        ``>>>from emipy import rawdata``
	``>>>rawdata.init_emipy_project('path')``
	``>>>exit()``
 

Experienced users can download the emipy package via the package manager pip:

``pip install emipy``

Keep in mind, that you have to install the list of packages given above. Execute point 3 from the step by step guide to initialize a new project.
    


=============
Quick start
=============

1. Start the IDE of your preference. If you are new, just execute ``>jupyter notebook`` in the Anaconda Prompt console. This should open a window in your browser. Click on "New" and select Python3.
2. Import the necessary modules:
    ``from emipy import processdata``
    ``from emipy import visualizedata``
3. Load the data into your current session with:
    ``db = processdata.read_db()``
    ``mb = processdata.read_mb()``
   and display it with:
    ``db.head()``
    ``mb.plot()``


