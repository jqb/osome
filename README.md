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

  * path(".")

  * path(".").is_dir() -> bool
  * path(".").is_file() -> bool
  * path(".").exists() -> bool

  * path(".").files() -> list
  * path(".").files_iter() -> generator

  * path(".").files("*.py") -> list
  * path(".").files_iter("*.py") -> generator

  * path(".").dirs() -> list
  * path(".").dirs_iter() -> generator

  * path(".").dirs("test*") -> list
  * path(".").dirs_iter("test*") -> generator

  * path(".").list("*.py", recursive=True)
  * path(".").list_iter("*.py", recursive=True)

  * path("/home") / path("seba") / path("test") -> path
  * path("/home") + path("seba") + path("test") -> path
  * path.join(['home','seba']) -> path

  * path("/home").append("test") -> path
  * path("/home").append(path('test')) -> path
  * path("/home/seba/test").split() -> list ? path?

  * path("/home/seba").open("w") -> file
  * path("/home/seba").touch() -> path
  * path("/home/seba").mkdir(p=False) -> path
  * path("/home/seba").rm(f=False, r=False) -> path | list?
  * path("/home/seba").ln(s=True, target=path|string) -> path | list?
  * path("/home/seba").cp(r=False, target=path|string) -> path | list?

  * for element in path(".")


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
