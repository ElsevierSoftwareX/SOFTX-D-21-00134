Introduction and quick start guide
==================================

=============
Introduction
=============    
emipy is a python module to analyse industrial emission sources within Europe.
It contains information about CO2 amounts, locations, industry, impurities and more.

=============
Installation    
=============
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