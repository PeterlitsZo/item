#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='item',
      version='0.0',
      description='run and build item auto and easy',
      author='Peterlits Zo',
      author_email='peterlitszo@outlook.com',

      packages=find_packages('src'),
      package_dir={'': 'src'},
      package_data={
        '': ['global_item_config.yaml'],
      },

      install_requires=['ruamel.yaml', 'colored'],
      entry_points = {
        'console_scripts': [
            'item = item.item:main',
        ]}
     )