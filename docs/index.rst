.. osome documentation master file, created by
   sphinx-quickstart on Mon Jan 14 21:49:10 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====
osome
=====

The bucket of python shell wrappers around os library, no dependencies, simple API.

* :mod:`osome.run` subprocess wrapper
* :mod:`osome.path` wraper around methods related to path manipulation

**Supported platforms**

* Python2.6
* Python2.7
* Python3.3
* PyPy1.9

**Source Code**

https://github.com/xando/osome


-----


:mod:`osome.run` -- subprocess wrapper
-------------------------------------------
.. py:module:: osome.run

.. code-block:: python

   >>> from osome import run

   >>> run('uname -r').stdout
   3.7.0-7-generic

   >>> run('uname -r', 'wc -c')
   uname -r | wc -c

   >>> run('uname -r', 'wc -c').stdout
   16


.. py:attribute:: run.stdout

   Standard output from executed command

   .. code-block:: python

      >>> run('uname -r').stdout
      3.7.0-7-generic

      >>> run('ls -la').stdout.lines
      ['total 20',
       'drwxrwxr-x 3 user user 4096 Dec 20 22:55 .',
       'drwxrwxr-x 5 user user 4096 Dec 20 22:57 ..',
       'drwxrwxr-x 2 user user 4096 Dec 20 22:37 dir',
       '-rw-rw-r-- 1 user user    0 Dec 20 22:52 file']

      >>> run('ls -la').stdout.qlines
      [['total 20'],
       ['drwxrwxr-x, 3, user, user, 4096, Dec, 20, 22:55, .'],
       ['drwxrwxr-x, 5, user, user, 4096, Dec, 20, 22:57, ..'],
       ['drwxrwxr-x, 2, user, user, 4096, Dec, 20, 22:37, dir'],
       ['-rw-rw-r--, 1, user, user,    0, Dec, 20, 22:52, file']]


.. py:attribute:: run.stderr

   Standard error from executed command

   .. code-block:: python

      >>> run('rm not_existing_directory').stderr
      rm: cannot remove `not_existing_directory': No such file or directory


.. py:attribute:: run.status

   Status code of executed command

   .. code-block:: python

      >>> run('uname -r').status
      0

      >>> run('rm not_existing_directory').status
      1

.. py:attribute:: run.chain

   The full chain of command executed 

   .. code-block:: python

      >>> run('uname -r', 'wc -c').chain
      [uname -r | wc -c]

   To get statuses from all component commands

      >>> [e.status for e in run('uname -r', 'wc -c').chain]
      [0, 0]


.. py:attribute:: run.pipe

To pipe data in

.. code-block:: python

    from osome import run

    run('grep something', data=run.stdin)

.. code-block:: bash

      $ ps aux | python script.py


-----


:mod:`osome.path` -- path manipulation
-------------------------------------------
.. module:: osome.path

.. code-block:: python

    >>> from osome import path

    >>> path('/var/log')
    /var/log

    >>> path('/var', 'log')
    /var/log

    >>> path('/var', 'log', 'syslog')
    /var/log/syslog

    >>> [(element.user, element.group, element.mod) for element in path('.')]
    [('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0775'),
     ('user', 'user', '0664')]

Path is also a instance of basestring so all methods implemented for `string/unicode
<http://docs.python.org/2/library/stdtypes.html#string-methods>`_ should work as well.

.. code-block:: python

   >>> path('.').absolute().split('/')
   ['', 'home', 'user', 'Projects', 'osome']

   >>> path('/home/user/test_tmp_directory').replace('_', '-')
   '/home/user/test-tmp-directory'

   >>> location = path('/home/user/test_tmp_directory')
   >>> location.mv(location.replace('_', '-'))


.. autoattribute:: osome.path.user
.. autoattribute:: osome.path.group
.. autoattribute:: osome.path.mod
.. autoattribute:: osome.path.absolute
.. autoattribute:: osome.path.basename
.. autoattribute:: osome.path.dir
.. autoattribute:: osome.path.a_time
.. autoattribute:: osome.path.m_time
.. autoattribute:: osome.path.size
.. autoattribute:: osome.path.exists

.. automethod:: osome.path.is_dir
.. automethod:: osome.path.is_file
.. automethod:: osome.path.mkdir
.. automethod:: osome.path.rm
.. automethod:: osome.path.cp
.. automethod:: osome.path.ln
.. automethod:: osome.path.unlink
.. automethod:: osome.path.touch
.. automethod:: osome.path.ls
.. automethod:: osome.path.ls_files
.. automethod:: osome.path.ls_dirs
.. automethod:: osome.path.walk
.. automethod:: osome.path.chmod
.. automethod:: osome.path.open


-----
