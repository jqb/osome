import sys

if sys.version.startswith('3'):
    base_string_class = str
else:
    base_string_class = unicode

from shelltools.run import run
from shelltools.path import path
from shelltools.text import progress, wrap, text_list

