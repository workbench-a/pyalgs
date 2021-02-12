# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# import io
# import os
# from pathlib import Path

# from setuptools import find_packages, setup


# # Package meta-data
# NAME = 'pyalgs'
# DESCRIPTION = 'Data structures and algorithms implemented in python.'
# URL = 'https://github.com/workbench-a/pyalgs'
# EMAIL = 'email@example.com'
# AUTHOR = 'AlephTaw'
# REQUIRES_PYTHON = '>=3.8.0'


# # Packages that are required for this module to be executed
# def list_reqs(fname='requirements.txt'):
#     with open(fname) as fd:
#         return fd.read().splitlines()



# here = os.path.abspath(os.path.dirname(__file__))

# # Import the README, and use it as the long-description.
# # Note: this will only work if 'README.md' is present in your MANIFEST.in file!
# try:
#     with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
#         long_description = '\n' + f.read()
# except FileNotFoundError:
#     long_description = DESCRIPTION


# # Load the package's __version__.py module as a dictionary.
# ROOT_DIR = Path(__file__).resolve().parent
# PACKAGE_DIR = ROOT_DIR / 'simple_regression_demo'
# about = {}
# with open(PACKAGE_DIR / 'VERSION') as f:
#     _version = f.read().strip()
#     about['__version__'] = _version

# setup(
#     name=NAME,
#     version=about['__version__'],
#     description=DESCRIPTION,
#     long_description=long_description,
#     long_description_content_type='text/markdown',
#     author=AUTHOR,
#     author_email=EMAIL,
#     python_requires=REQUIRES_PYTHON,
#     url=URL,
#     packages=find_packages(exclude=('tests',)),
#     package_data={'simple_regression_demo': ['VERSION']},
#     install_requires=list_reqs(),
#     extras_require={},
#     include_package_data=True,
#     license='BSD 3',
#     classifiers=[
#         # Trove classifiers
#         # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
#         'License :: OSI Approved :: MIT License',
#         'Programming Language :: Python :: 3.8',
#     ],
# )