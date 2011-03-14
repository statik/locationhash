#!/usr/bin/env python
"""Distutils installer for locationhash."""

from distutils.core import setup


setup(name='locationhash',
      author='Elliot Murphy',
      author_email='elliot.murphy+locationhash@gmail.com',
      url='https://github.com/greyspot/locationhash',
      description=('Primitive location hashing'),
      version='0.1',
      classifiers=["License :: OSI Approved :: Apache Software License",
          "Development Status :: 2 - Pre-Alpha",
          "Topic :: Scientific/Engineering :: GIS"],
      packages=['locationhash', 'locationhash.tests'])
