#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="tweepy",
      version="2.0",
      description="Twitter API Library",
      license="MIT",
      author="Joshua Roesslein",
      author_email="tweepy@googlegroups.com",
      url="http://github.com/tweepy/tweepy",
      packages = find_packages(),
      requires = [
          'requests',
          'oauth >= 1.0.1',
      ],
      keywords= "twitter library",
      zip_safe = True)
