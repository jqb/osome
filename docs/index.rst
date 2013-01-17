.. shelltools documentation master file, created by
   sphinx-quickstart on Mon Jan 14 21:49:10 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-shelltools
=================

https://github.com/xando/python-shelltools

The bucket of python shell helpers, no dependencies, simple API.
This lib is in development, nothing interesting here yet.

* Python2.6
* Python2.7
* Python3.3
* PyPy1.9

- shelltools: (shell)

  - path - path wraper around all methods related to path manipulation
  - run - subprocess wrapper
  - text: - strings helper functions

    - text_list
    - wrap
    - progress

  - ui: - halper to create better text shell, let's steal from clint for now

    - progress
    - color
    - indent

  - args: - helper to handle shell arguments (missing)


.. autoclass:: shelltools.path
   :members: 
   :special-members:

.. autoclass:: shelltools.run
   :members: 
   :special-members:



