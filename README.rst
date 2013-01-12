python-shelltools (in development)
==================================

https://github.com/xando/python-shelltools

The bucket of python shell helpers, no dependencies, simple API.
This lib is development, nothing interesting here yet.

Python2.7 only (for now).

- shelltools: (shell)

  - path - path wraper around all methods related to path manipulation
  - run - subprocess wrapper
  - text: - strings helper functions

    - text_list
    - wrap

  - ui: - halper to create better text shell, let's steal from clint for now

    - progress
    - color
    - indent


path
----

.. code-block:: bash

   $ ls -la
   total 20
   drwxrwxr-x 3 user user 4096 Dec 20 22:37 .
   drwxrwxr-x 5 user user 4096 Dec 20 22:38 ..
   drwxrwxr-x 2 user user 4096 Dec 20 22:37 dir
   -rw-rw-r-- 1 user user    0 Dec 20 22:37 file


.. code-block:: python

   >>> path('.')
   .

   u'./dir/file'
   >>> path('.', 'dir', 'file')

   >>> path('.').is_dir()
   True

   >>> path('.').is_file()
   False

   >>> path('.').exists()
   True

   >>> for e in path('.'):
   ...     print e
   'dir'
   'file'

   >>> path('.').ls()
   [u'dir', u'file']

   >>> path('.').ls_files()
   [u'file']

   >>> path('.').ls_dirs()
   [u'dir']

   >>> path('.').walk()
   <generator object walk at 0x7f7ff6f3c960>

   >>> path('.') / path('file')
   u'./file'

   >>> (path('.') / path('file')).exists()
   True

   >>> path.join('.', 'file')
   u'./file'

   >>> path.join('.', 'file').exists()
   True

   >>> path.join('.', 'file').open('w')
   <open file u'./file', mode 'w' at 0x1b23660>

   >>> path('file2').touch().exists()
   True

   >>> path('dir2').mkdir().exists()
   True

   >>> path('file2').rm().exists()
   False

   >>> path('dir2').rm().exists()
   False

   >>> path('dir2').cp('dir_copy')
   u'dir_copy'

   >>> path('file1').cp('file_copy')
   u'file_copy'

   >>> path('file1').cp('file_copy').exists()
   True

   Path is also a instance of basestring so all methods implemented on (string)[http://docs.python.org/2/library/stdtypes.html#string-methods] should work as well.

   >> path('.').absolute().split('/')
   [u'', u'home', u'user', u'Projects', u'python-shelltools']

   >> path('/home/user/test_tmp_directory').replace('_', '-')
   path('/home/user/test_tmp_directory').replace('_', '-')


run
---

.. code-block:: python

  >>> from shelltools import run

  >>> print run('uname -r')
  3.7.0-7-generic

  >>> print run('uname -r').stdout
  3.7.0-7-generic

  >>> print run('rm not_existing_directory').stderr
  rm: cannot remove `not_existing_directory': No such file or directory

  >>> print run('ls -la', 'wc -l')
  14

  >>> print run('ls -la', 'wc -l', 'wc -c')
  3

  >>> run('ls -la', 'wc -l', 'wc -c')
  ls -la | wc -l | wc -c

  >>> print run('ls -la').stdout.lines
  [u'total 20',
   u'drwxrwxr-x 3 user user 4096 Dec 20 22:55 .',
   u'drwxrwxr-x 5 user user 4096 Dec 20 22:57 ..',
   u'drwxrwxr-x 2 user user 4096 Dec 20 22:37 dir',
   u'-rw-rw-r-- 1 user user    0 Dec 20 22:52 file']


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


Tests
-----

.. image:: https://api.travis-ci.org/xando/python-shelltools.png

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
