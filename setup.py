#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

requires = ['requests']

with open('README.md') as f:
    readme = f.read()

setup(
    name='supportbee',
    version='0.0.1',
    description='Python Library for SupportBee APIs',
    long_description=readme + '\n\n',
    author='Sivasubrmaniam Arunachalam, Kracekumar Ramaraju',
    author_email='siva@sivaa.in',
    url='https://github.com/sivaa/supportbee-python',
    package_dir={'supportbee': 'supportbee'},
    include_package_data=True,
    install_requires=requires,
    zip_safe=True,
)
