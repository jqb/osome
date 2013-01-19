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


-----


:mod:`shelltools.run` -- subprocess wrapper
-------------------------------------------
.. module:: shelltools.run


.. code-block:: python

   >>> from shelltools import run

   >>> print run('uname -r')
   3.7.0-7-generic

   >>> print run('uname -r').stdout
   3.7.0-7-generic

   >>> run('uname -a').status
   0

   >>> print run('rm not_existing_directory').stderr
   rm: cannot remove `not_existing_directory': No such file or directory

   >>> print run('ls -la', 'wc -l')
   14

   >>> print run('ls -la', 'wc -l', 'wc -c')
   3

   >>> run('ls -la', 'wc -l', 'wc -c')
   ls -la | wc -l | wc -c

   >>> print run('ls -la').stdout.lines
   ['total 20',
    'drwxrwxr-x 3 user user 4096 Dec 20 22:55 .',
    'drwxrwxr-x 5 user user 4096 Dec 20 22:57 ..',
    'drwxrwxr-x 2 user user 4096 Dec 20 22:37 dir',
    '-rw-rw-r-- 1 user user    0 Dec 20 22:52 file']

To use pipe from the shell.

.. code-block:: python

    from shelltools import run
    run('grep something', data=run.stdin)

.. code-block:: bash

      $ ps aux | python script.py


-----


:mod:`shelltools.path` -- path manipulation
-------------------------------------------
.. module:: shelltools.path

.. automethod:: shelltools.path.absolute
.. automethod:: shelltools.path.basename
.. automethod:: shelltools.path.dir
.. automethod:: shelltools.path.a_time
.. automethod:: shelltools.path.m_time
.. automethod:: shelltools.path.size
.. automethod:: shelltools.path.exists
.. automethod:: shelltools.path.is_dir
.. automethod:: shelltools.path.is_file
.. automethod:: shelltools.path.mkdir
.. automethod:: shelltools.path.rm
.. automethod:: shelltools.path.cp
.. automethod:: shelltools.path.ln
.. automethod:: shelltools.path.unlink
.. automethod:: shelltools.path.touch
.. automethod:: shelltools.path.ls
.. automethod:: shelltools.path.ls_files
.. automethod:: shelltools.path.walk
.. automethod:: shelltools.path.chmod
.. automethod:: shelltools.path.open


-----


:mod:`shelltools.text` -- text helpers
--------------------------------------
.. module:: shelltools.text

.. automethod:: shelltools.text.wrap
.. automethod:: shelltools.text.text_list
