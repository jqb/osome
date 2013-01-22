.. shelltools documentation master file, created by
   sphinx-quickstart on Mon Jan 14 21:49:10 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-shelltools
=================

The bucket of python shell helpers, no dependencies, simple API.


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

https://github.com/xando/python-shelltools

-----


:mod:`shelltools.run` -- subprocess wrapper
-------------------------------------------
.. module:: shelltools.run


.. code-block:: python

   >>> from shelltools import run

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
      [uname -r, uname -r | wc -c]

   To get statuses from all component commands

      >>> [e.status for e in run('uname -r', 'wc -c').chain]
      [0, 0]


.. py:attribute:: run.pipe

To pipe data in

.. code-block:: python

    from shelltools import run

    run('grep something', data=run.stdin)

.. code-block:: bash

      $ ps aux | python script.py


-----


:mod:`shelltools.path` -- path manipulation
-------------------------------------------
.. module:: shelltools.path

.. code-block:: python

    >>> from shelltools import path

    >>> path('/var/log')
    /var/log

    >>> path('/var', 'log')
    /var/log

    >>> path('/var', 'log', 'syslog')
    /var/log/syslog

    >>> [(element.user, element.group, element.permissions) for element in path('.')]
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
   ['', 'home', 'user', 'Projects', 'python-shelltools']

   >>> path('/home/user/test_tmp_directory').replace('_', '-')
   '/home/user/test-tmp-directory'

   >>> location = path('/home/user/test_tmp_directory')
   >>> location.mv(location.replace('_', '-'))


.. autoattribute:: shelltools.path.user
.. autoattribute:: shelltools.path.group
.. autoattribute:: shelltools.path.mod
.. autoattribute:: shelltools.path.absolute
.. autoattribute:: shelltools.path.basename
.. autoattribute:: shelltools.path.dir
.. autoattribute:: shelltools.path.a_time
.. autoattribute:: shelltools.path.m_time
.. autoattribute:: shelltools.path.size
.. autoattribute:: shelltools.path.exists

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
.. automethod:: shelltools.path.ls_dirs
.. automethod:: shelltools.path.walk
.. automethod:: shelltools.path.chmod
.. automethod:: shelltools.path.open


-----


:mod:`shelltools.text` -- text helpers
--------------------------------------
.. module:: shelltools.text

.. automethod:: shelltools.text.text_list
.. automethod:: shelltools.text.wrap

.. automethod:: shelltools.text.progress

.. code-block:: python

   from shelltools.text import progress

   for i in progress(range(10)):
       sleep(0.2)


.. code-block:: python

   [                                ] 0/5 - 00:00:00
   [######                          ] 1/5 - 00:00:00
   [############                    ] 2/5 - 00:00:00
   [###################             ] 3/5 - 00:00:00
   [#########################       ] 4/5 - 00:00:00
   [################################] 5/5 - 00:00:00

.. automethod:: shelltools.text.progress.dots

.. code-block:: python

   for i in progress.dots(range(10)):
       sleep(0.2)

.. code-block:: python

   .
   ..
   ...
   ....
   .....

.. automethod:: shelltools.text.progress.mill

.. code-block:: python

   for i in progress.mill(range(10)):
       sleep(0.2)

.. code-block:: python
       
   | 0/5
   / 1/5
   - 2/5
   \ 3/5
   | 4/5
   / 5/5

