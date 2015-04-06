'''
Basic ``setup.py``, intended for::

    $ python setup.py develop

Incomplete, does not specify dependencies etc.

After: 
http://packages.python.org/distribute/setuptools.html#basic-use


Created on Feb 20, 2015

@author: Teon Brooks
'''
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "free",
    version = "0.1dev",
    packages = find_packages(),
)