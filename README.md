In Development
==============

  Nothing interesting here


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

  * path("/home/seba").open("","w") -> file
  * path("/home/seba").touch() -> path
  * path("/home/seba").mkdir(p=False) -> path
  * path("/home/seba").rm(f=False, r=False) -> path | list?
  * path("/home/seba").ln(s=True, target=path|string) -> path | list?
  * path("/home/seba").cp(r=False, target=path|string) -> path | list?
  
  * for element in path(".")

  * run('ls -la').pipe('')
  * run('ls -la').then('')
  * run('ls -la')
  * run('ls -la')
  * run('ls -la', path=path('.')).pipe(" ")
  * run('ls -la', path=path('.')).pipe.xargs(" ")
  
  * with path('.'):
       run("test")


Reference links
===============

  * http://www.ruby-doc.org/stdlib-1.9.3/libdoc/fileutils/rdoc/index.html
