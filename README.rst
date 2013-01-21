python-shelltools (in development)
==================================

The bucket of python shell helpers, no dependencies, simple API.
**This lib is in development**, nothing interesting here yet.

* Python2.6
* Python2.7
* Python3.3
* PyPy1.9


Documentation
-------------
https://shelltools.readthedocs.org/en/latest/

Code
----
https://github.com/xando/python-shelltools


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


path
----

.. code-block:: python

   >>> from shelltools import path

   >>> path('/var/log')
   /var/log

   >>> path('/var', 'log')
   /var/log

   >>> path('/var/log').own
   '766'

   >>> path('/var/log').is_dir()
   True

   >>> for e in path('/var/log'):
   ...     print e
   /var/log/boot.log
   /var/log/dmesg
   /var/log/faillog
   /var/log/kern.log
   /var/log/gdm

   >>> path('/var/log/').ls('*log')
   [/var/log/boot.log, /var/log/faillog, /var/log/kern.log]

   >>> path('/var/log') / 'syslog'
   /var/log/syslog

   >>> (path('/var/log') / 'syslog').exists

   >>> path('/var/log','syslog').open('r')
   <open file '/var/log/syslog', mode 'r' at 0x294c5d0>
   
   >>> path('/var/log').cp('copy', r=True)
   copy

   >>> path('/home/user/test_tmp_directory').replace('_', '-')
   '/home/user/test-tmp-directory'

   >>> location = path('/home/user/test_tmp_directory')
   >>> location.mv( location.replace('_', '-') )

run
---

.. code-block:: python

  >>> from shelltools import run

  >>> print run('uname -r').stdout
  3.7.0-7-generic

  >>> run('uname -a').status
  0

  >>> print run('rm not_existing_directory').stderr
  rm: cannot remove `not_existing_directory': No such file or directory

  >>> print run('ls -la', 'wc -l', 'wc -c')
  3

  >>> print run('ls -la').stdout.lines
  ['total 20',
   'drwxrwxr-x 3 user user 4096 Dec 20 22:55 .',
   'drwxrwxr-x 5 user user 4096 Dec 20 22:57 ..',
   'drwxrwxr-x 2 user user 4096 Dec 20 22:37 dir',
   '-rw-rw-r-- 1 user user    0 Dec 20 22:52 file']


.. code-block:: python

  from shelltools import run

  run('grep something', data=run.stdin)

.. code-block:: bash

  $ ps aux | python script.py


context
-------

.. code-block:: python

  with path('/tmp') as p:
      print p.run('ls -la')

      p('new_directory1').mkdir()

      (p / 'new_directory2').mkdir()

      (p / 'empty_file').touch()


text
----

.. code-block:: python

   >>> print wrap("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis sollicitudin ", 30)
   Lorem ipsum dolor sit amet,
   consectetur adipiscing elit.
   Duis sollicitudin

   >>> print text_list(["black", "red", "blue", "green"])
   black, red, blue or green

   >>> print text_list(["black", "red", "blue", "green"], "and")
   black, red, blue and green


.. code-block:: python

   from shelltools.text import progress

   for i in progress(range(100)):
       sleep( 0.2)

.. code-block:: none

   [                                ] 0/5 - 00:00:00
   [######                          ] 1/5 - 00:00:00
   [############                    ] 2/5 - 00:00:00
   [###################             ] 3/5 - 00:00:00
   [#########################       ] 4/5 - 00:00:00
   [################################] 5/5 - 00:00:00

tests
-----

.. image:: https://api.travis-ci.org/xando/python-shelltools.png?branch=master

Travis CI, https://travis-ci.org/xando/python-shelltools


Tests are implemented with `py.tests
<http://pytest.org/>`_, to run:

.. code-block:: bash

   python runtests.py


based on/inspired by
--------------------

* http://www.ruby-doc.org/stdlib-1.9.3/libdoc/fileutils/rdoc/index.html
* https://github.com/kennethreitz/clint
* https://github.com/jaraco/path.py


author
------

* Sebastina Pawluś (sebastian.pawlus@gmail.com)


contributors
------------

* Jakub (kuba.janoszek@gmail.com)
* Angel Ezquerra
