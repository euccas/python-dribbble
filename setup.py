import os
from setuptools import setup, find_packages

install_requires = []
try:
    import json
except ImportError, e:
    install_requires.append('simplejson')

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.markdown')

description = 'A Python interface to the dribbble.com API.'

if os.path.exists(README_PATH):
    long_description = open(README_PATH).read()
else:
    long_description = description

setup(
    name='dribbble',
    version='0.0.1',
    install_requires=install_requires,
    description=description,
    long_description=long_description,
    author='Steve Losh',
    author_email='steve@stevelosh.com',
    url='http://bitbucket.org/sjl/python-dribbble/',
    packages=['dribbble'],
)
