from codecs import open
from os.path import join, abspath, dirname
from setuptools import setup, find_packages
import os

requirementPath = 'requirements.txt'
install_requires = []

if os.path.isfile(requirementPath):
      with open(requirementPath) as f:
            install_requires = f.read().splitlines()

setup(
      name="drawing1",
      version="0.1",
      description="Drawing Distribution Package",
      packages=find_packages(include=['drawing1']),
      include_package_data=True,
      install_requires=install_requires
)









