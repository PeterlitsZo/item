#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='item',
      version='0.0',
      description='run and build item auto and easy',
      author='Peterlits Zo',
      author_email='peterlitszo@outlook.com',
      packages=find_packages(),
      data_files=[('src', ['src/global_item.yaml'])],
      install_requires=['pyyaml', 'colored'],
      entry_points = {
        'console_scripts': [
            'item = src.item:main',
        ]}
     )