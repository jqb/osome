import os
import shutil
import fnmatch

from shelltools import run, base_string_class


class pathmeta(type):

    @classmethod
    def str_to_path(cls, func):

        def decorator(*args, **kwargs):
            value = func(*args, **kwargs)

            if isinstance(value, base_string_class):
                return path(value)

            return value
        return decorator

    def __new__(cls, name, bases, local):
        _unicode = bases[0]

        for method_name in _unicode.__dict__:
            value = getattr(_unicode, method_name)

            if all([callable(value),
                    not method_name.startswith('__'),
                    method_name not in local]):

                local[method_name] = cls.str_to_path(value)

        return type.__new__(cls, name, bases, local)


class path(pathmeta('base_path', (base_string_class, ), {})):
    """

    .. code-block:: bash

       $ ls -la /var/log
       total 20
       drwxrwxr-x 3 root root  4096 Dec 20 22:37 .
       drwxrwxr-x 5 root root  4096 Dec 20 22:38 ..
       drwxrwxr-x 2 root root  4096 Dec 20 22:37 gdm
       -rw-rw-r-- 1 root root 11561 Dec 20 22:37 boot.log
       -rw-rw-r-- 1 root root 11562 Dec 20 22:37 dmesg
       -rw-rw-r-- 1 root root 11563 Dec 20 22:37 faillog
       -rw-rw-r-- 1 root root 11564 Dec 20 22:37 kern.log


    .. code-block:: python

        >>> from shelltools import path

        >>> path('/var/log')
        /var/log

        >>> path('/var', 'log')
        /var/log

        >>> path('/var', 'log', 'syslog')
        /var/log/syslog


    Path is also a instance of basestring so all methods implemented for `string/unicode
    <http://docs.python.org/2/library/stdtypes.html#string-methods>`_ should work as well.

    .. code-block:: python

       >>> path('.').absolute().split('/')
       ['', 'home', 'user', 'Projects', 'python-shelltools']

       >>> path('/home/user/test_tmp_directory').replace('_', '-')
       '/home/user/test-tmp-directory'

       >>> location = path('/home/user/test_tmp_directory')
       >>> location.mv(location.replace('_', '-'))


    """

    def __call__(self, *args):
        return self / path(*args)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __repr__(self):
        return self

    def run(self, *args, **kwargs):
        kwargs['cwd'] = self
        return run(*args, **kwargs)

    def __new__(cls, *args):
        if len(args) > 1:
            return super(path, cls).__new__(path, cls.join(*args))
        return super(path, cls).__new__(path, *args)

    def absolute(self):
        """
        """
        return path(os.path.abspath(self))

    def basename(self):
        """
        """
        return path(os.path.basename(self))

    def dir(self):
        """
        >>> path('/var/log/syslog').dir()
        /var/log
        """
        return path(os.path.dirname(self))

    def a_time(self):
        """
        """
        return os.path.getatime(self)

    def m_time(self):
        """
        """
        return os.path.getmtime(self)

    def size(self):
        """
        """
        return os.path.size(self)

    def exists(self):
        """
        >>> path('/var/log').exists()
        True
        """
        return os.path.exists(self)

    def is_dir(self):
        """
        >>> path('/var/log').is_dir()
        True
        """
        return os.path.isdir(self)

    def is_file(self):
        """
        >>> path('/var/log/syslog').is_file()
        False
        """
        return os.path.isfile(self)

    def is_link(self):
        """
        """
        return os.path.islink(self)

    def mkdir(self, p=False):
        """
        >>> path('dir').mkdir().exists()
        True
        """
        if p:
            os.makedirs(self)
        else:
            os.mkdir(self)
        return self

    def rm(self, p=False):
        """
        >>> path('file').rm().exists()
        False
        """
        if os.path.isfile(self):
            os.remove(self)
        else:
            if p:
                shutil.rmtree(self)
            else:
                os.rmdir(self)
        return self

    def cp(self, target, r=False):
        """
        >>> path('dir').cp('dir_copy')
        dir_copy

        >>> path('file1').cp('file_copy')
        file_copy

        >>> path('file1').cp('file_copy').exists()
        True
        """
        if self.is_dir():
            shutil.copytree(self, target)
        else:
            shutil.copy(self, target)
        return path(target)

    def ln(self, target, s=True):
        """
        """
        if s:
            os.symlink(os.path.realpath(self), target)
        else:
            os.link(os.path.realpath(self), target)
        return path(target)

    def unlink(self):
        """
        """
        os.unlink(self)
        return self

    def touch(self):
        """
        >>> path('file').touch().exists()
        True
        """
        open(self, "a")
        return self

    def ls(self, pattern="*", sort=None):
        """
        >>> path('/var/log').ls()
        [/var/log/boot.log, /var/log/dmesg, /var/log/faillog, /var/log/kern.log, /var/log/gdm]

        >>> path('/var/log/').ls('*log')
        [/var/log/boot.log, /var/log/faillog, /var/log/kern.log]
        """
        sort = sort or (lambda e: (not e.is_dir(), e))
        content = [
            path(e) for e in os.listdir(self) if fnmatch.fnmatch(e, pattern)
        ]
        return sorted(content, key=sort)

    def ls_files(self, patern="*", sort=None):
        """
        >>> path('.').ls_files()
        [/var/log/boot.log, /var/log/dmesg, /var/log/faillog, /var/log/kern.log]
        """
        return [e for e in self.ls(patern, sort) if (self / e).is_file()]

    def ls_dirs(self, patern="*", sort=None):
        """
        >>> path('.').ls_dirs()
        [/var/log/gdm]]
        """
        return [e for e in self.ls(patern, sort) if (self / e).is_dir()]

    def walk(self, pattern="*", r=False, sort=None):
        """
        >>> path('.').walk()
        <generator object walk at 0x7f7ff6f3c960>
        """
        sort = sort or (lambda e: (e.is_dir(), e))
        content = self.ls(pattern=pattern, sort=sort)
        for element in content:

            if fnmatch.fnmatch(element, pattern):
                yield self / element
            if element.is_dir() and r:
                for item in element.walk(pattern="*", sort=sort):
                    yield item

    def chmod(self, mod):
        """
        """
        return self

    def open(self, *args, **kwargs):
        """
        """
        return open(self, *args, **kwargs)

    def __iter__(self):
        """
        >>> for e in path('/var/log'):
        ...     print e
        /var/log/boot.log
        /var/log/dmesg
        /var/log/faillog
        /var/log/kern.log
        /var/log/gdm
        """
        return self.walk()

    def __div__(self, other):
        """
        >>> path('/var/log') / path('syslog')
        /var/log/syslog
        >>> path('/var/log') / 'syslog'
        /var/log/syslog
        >>> (path('/var/log') / 'syslog').exists()
        """

        return path(os.path.join(self, other))

    __truediv__ = __div__

    @classmethod
    def join(cls, *path_list):
        return path(os.path.join(*path_list))


if __name__ == "__main__":
    pass
