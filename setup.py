#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyalgs",
    version="0.0.1",
    author="AlephTaw",
    author_email="example@example.com",
    description="Data structures and algorithms implemented in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/workbench-a/pyalgs",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)