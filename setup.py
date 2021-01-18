# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:25:20 2020

@author: f-ove
"""


import setuptools
import os

with open ("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emipy",
    version="0.0.63",
    author="Florian Overberg; Simon Morgenthaler",
    author_email="s.morgenthaler@fz-juelich.de",
    description="Python package for emission data analysis based on the E-PRTR database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab-public.fz-juelich.de/s.morgenthaler/emipy",
    packages=setuptools.find_packages(),
    package_data={"emipy": ["configuration/*.ini"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
	'Documentation': 'https://emipy.readthedocs.io/en/latest/',
	'Source': 'https://gitlab-public.fz-juelich.de/s.morgenthaler/emipy'
    },
    python_requires='>=3.6',
)






