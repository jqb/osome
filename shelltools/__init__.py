import sys

if sys.version.startswith('3'):
    base_string_class = unicode
else:
    base_string_class = str

from shelltools.run import run
from shelltools.path import path
