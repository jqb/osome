In Development
==============

  Nothing interesting here.

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
   >>> path(".")
   .
   
   >>> path('.').is_dir()
   True
   
   >>> path(".").is_file()
   False
   
   >>> path('.').exists()
   True
   
   >>> path('.').ls()
   [u'dir', u'file']
   
   >>> path('.').ls_files()
   [u'file']

   >>> path('.').ls_dirs()
   [u'dir']
   
   >>> path('.') / path('file')
   u'./file'

   >>> (path('.') / path('file')).exists()
   True
   
   >>> path.join('.','file')
   u'./file'
   
   >>> path.join('.','file').exists()
   True
   
   >>> path.join('.','file').open("w")
   <open file u'./file', mode 'w' at 0x1b23660>
   
   >>> path("file2").touch().exists()
   True
   
   >>> path("dir2").mkdir().exists()
   True
   
   >>> path("file2").rm().exists()
   False
   
   >>> path("dir2").rm().exists()
   False 
   ```
   
   Not implemented
   
   * path(".").ls_iter("*.py")
   * path(".").ls_files_iter("*.py") -> generator
   * path(".").ls_dirs_iter() -> generator
   * path("/home") + path("seba") + path("test") -> path
   * path("/home").append("test") -> path
   * path("/home").append(path('test')) -> path
   * path("/home/seba/test").split() -> list ? path?
   * for element in path(".")
   * path("/home/seba").cp(r=False, target=path|string) -> path | list?
   * path("/home/seba").ln(s=True, target=path|string) -> path | list?

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

  >>> print run('ls -la').run('wc -l')
  14

  >>> print run('ls -la').run('wc -l').run('wc -c')
  3

  >>> run('ls -la').run('wc -l').run('wc -c')
  ls -la | wc -l | wc -c
  ```


links
-----

  * http://www.ruby-doc.org/stdlib-1.9.3/libdoc/fileutils/rdoc/index.html
