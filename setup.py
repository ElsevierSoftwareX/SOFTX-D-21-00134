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
    version="0.0.58",
    author="Flow2theryan; s.morgenthaler",
    author_email="f.overberg@web.de; s.morgenthaler@fz-juelich.de",
    description="A small package for emission data analysis",
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






