Introduction and quick start guide
==================================

=============
Introduction
=============    
Emipy is a python package to analyse industrial emission sources within Europe.
The package accesses data from the European Environmental Agency and Eurostat, and allows to generate a desired data set with clearly structured filter functions. Furthermore, functions are provided that allow a quick visualization of the data.

=============
Installation    
=============

Requirements
------------

Emipy  requires:
1. Python, version 3.7 or higher
2. Additional add-on modules (see below for the complete list)
3. The emipy package itself

Recommended installation
------------------------
The easiest way to

Emipy can be installed using the following command:

``pip install emipy``    

We recommend to set up a fresh environment using the following command:

``conda create -n emipy python=3.7 pandas matplotlib``

``activate emipy``

``pip install emipy``


=============
Quick start
=============

=============
Initialize
=============

Once the environment is set up you have to run the initialize command.
This will ensure that all the necessary data is downloaded, extracted and pickled.
It is only necessary to run this command once. 

``import emipy``
        
``emipy.init()``

=============
Load data
=============
Bla blub can be done with

``db = emipy.load_db()``