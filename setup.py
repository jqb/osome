# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from shelltools import path

description = "The bucket of python shell helpers, no dependencies, simple API."

project = path(__file__).dirname()

long_description = (project / 'README.rst').open("r").read()
version = (project / 'VERSION').open("r").read()
license = (project / 'LICENSE').open("r").read()


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