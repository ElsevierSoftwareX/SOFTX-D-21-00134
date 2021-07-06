# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:25:20 2020

@author: f-ove
"""

import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emipy",
    version="0.0.78",
    author="Florian Overberg, Philipp C. Böttcher, Simon Morgenthaler",
    author_email="p.boettcher@fz-juelich.de",
    description="Python package for emission data analysis based on the E-PRTR database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://jugit.fz-juelich.de/network-science-group/emipy",
    packages=setuptools.find_packages(),
    package_data={"emipy": ["configuration/*.ini"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Documentation': 'https://emipy.readthedocs.io/en/latest/',
        'Source': 'https://jugit.fz-juelich.de/network-science-group/emipy'
    },
    python_requires='>=3.6',
    install_requires=[
        'matplotlib>=3.3.1',
        'requests>=2.24.0',
        'configparser>=5.0.0',
        'pandas>=1.1.1',
        'ruamel.yaml>=0.16.12',
        'descartes>=1.1.0',
        'openpyxl>=3.0.6'
    ]
)
