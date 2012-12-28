python-shelltools (in development)
==================================

  The bucket of python shell helpers, no dependencies, simple API. 
  This lib is development, nothing interesting here yet. 
  
  Python2.7 only (for now).

  * shelltools: (shell)
	* path - path wraper around all methods related to path manipulation
	* run - subprocess wrapper
	* ui: - halper to create better text shell, let's steal from clint for now
	  * progress
	  * color
	  * indent
	* text: - helper function to manipulate
	  * text_list
	  * wrap

path
----
	
   ```bash
   $ ls -la 
   total 20
   drwxrwxr-x 3 seba seba 4096 Dec 20 22:37 .
   drwxrwxr-x 5 seba seba 4096 Dec 20 22:38 ..
   drwxrwxr-x 2 seba seba 4096 Dec 20 22:37 dir
   -rw-rw-r-- 1 seba seba    0 Dec 20 22:37 file
   ```

   
   ```python
   >>> path('.')
   .
   
   >>> path('.', 'dir', 'file')
   u'./dir/file'
   
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
   ```
   
   Not implemented
   
   * path('/home/seba/test').split() -> list ? path?
   * path('/home/seba').cp(r=False, target=path|string) -> path | list?
   * path('/home/seba').ln(s=True, target=path|string) -> path | list?

run
---

  ```python
  >>> from shelltools import run

  >>> print run('uname -r')
  3.7.0-7-generic

  >>> print run('uname -r').stdout
  3.7.0-7-generic

  >>> print run('rm not_existing_directory').stdout
  rm: cannot remove `not_existing_directory': No such file or directory

  >>> print run('ls -la', 'wc -l')
  14

  >>> print run('ls -la', 'wc -l', 'wc -c')
  3

  >>> run('ls -la', 'wc -l', 'wc -c')
  ls -la | wc -l | wc -c
  
  >>> print run('ls -la').stdout.lines
  [u'total 20',
   u'drwxrwxr-x 3 seba seba 4096 Dec 20 22:55 .',
   u'drwxrwxr-x 5 seba seba 4096 Dec 20 22:57 ..',
   u'drwxrwxr-x 2 seba seba 4096 Dec 20 22:37 dir',
   u'-rw-rw-r-- 1 seba seba    0 Dec 20 22:52 file']
  ```

text
----
   
   ```python
   >>> print wrap("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis sollicitudin ", 30)
   Lorem ipsum dolor sit amet,
   consectetur adipiscing elit.
   Duis sollicitudin 

   >>> print text_list(["black", "red", "blue", "green"])
   black, red, blue or green
   
   >>> print text_list(["black", "red", "blue", "green"], "and")
   black, red, blue and green
   ```

links
-----

  * http://www.ruby-doc.org/stdlib-1.9.3/libdoc/fileutils/rdoc/index.html
  * https://github.com/kennethreitz/clint
  * https://github.com/jaraco/path.py
