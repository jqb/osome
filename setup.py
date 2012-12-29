# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

description = """
The bucket of python shell helpers, no dependencies, simple API.
"""

long_description = open(
    os.path.join(os.path.dirname(__file__), 'README.rst')
).read()

version = open(
    os.path.join(os.path.dirname(__file__), 'VERSION')
).read()

license = open(
    os.path.join(os.path.dirname(__file__), 'LICENSE')
).read()

from shelltools import run

setup(name='shelltools',
      version=version,
      packages=find_packages(),
      author='Sebastian Pawluś',
      author_email='sebastian.pawlus@gmail.com',
      url='https://github.com/xando/python-shelltools',
      description=description,
      keywords="shell tools shell path ",
      license=license,
      long_description=long_description,
      include_package_data=True,
      platforms=['any'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
      ],
)