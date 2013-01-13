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

    def __call__(self, *args):
        return self / path(*args)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def run(self, *args, **kwargs):
        kwargs['cwd'] = self
        return run(*args, **kwargs)

    def __new__(cls, *args):
        if len(args) > 1:
            return super(path, cls).__new__(path, cls.join(*args))
        return super(path, cls).__new__(path, *args)

    def absolute(self):
        return path(os.path.abspath(self))

    def basename(self):
        return path(os.path.basename(self))

    def dir(self):
        return path(os.path.dirname(self))

    def a_time(self):
        return os.path.getatime(self)

    def m_time(self):
        return os.path.getmtime(self)

    def size(self):
        return os.path.size(self)

    def exists(self):
        return os.path.exists(self)

    def is_dir(self):
        return os.path.isdir(self)

    def is_file(self):
        return os.path.isfile(self)

    def is_link(self):
        return os.path.islink(self)

    def mkdir(self, p=False):
        if p:
            os.makedirs(self)
        else:
            os.mkdir(self)
        return self

    def rm(self, p=False):
        if os.path.isfile(self):
            os.remove(self)
        else:
            if p:
                shutil.rmtree(self)
            else:
                os.rmdir(self)
        return self

    def cp(self, target, r=False):
        if self.is_dir():
            shutil.copytree(self, target)
        else:
            shutil.copy(self, target)
        return path(target)

    def ln(self, target, s=True):
        if s:
            os.symlink(os.path.realpath(self), target)
        else:
            os.link(os.path.realpath(self), target)
        return path(target)

    def unlink(self):
        os.unlink(self)
        return self

    def touch(self):
        open(self, "a")
        return self

    def ls(self, pattern="*", sort=lambda e: (not e.is_dir(), e)):
        content = [
            path(e) for e in os.listdir(self) if fnmatch.fnmatch(e, pattern)
        ]
        return sorted(content, key=sort)

    def ls_files(self, patern="*"):
        return [e for e in self.ls(patern) if (self / e).is_file()]

    def ls_dirs(self, patern="*"):
        return [e for e in self.ls(patern) if (self / e).is_dir()]

    def walk(self, pattern="*", sort=lambda e: (e.is_dir(), e), r=False):
        content = self.ls(pattern=pattern, sort=sort)
        for element in content:

            if fnmatch.fnmatch(element, pattern):
                yield self / element
            if element.is_dir() and r:
                for item in element.walk(pattern="*", sort=sort):
                    yield item

    def chmod(self, mod):
        return self

    def open(self, *args, **kwargs):
        return open(self, *args, **kwargs)

    def __iter__(self):
        return self.walk()

    def __div__(self, other):
        return path(os.path.join(self, other))

    __truediv__ = __div__

    @classmethod
    def join(cls, *path_list):
        return path(os.path.join(*path_list))


if __name__ == "__main__":
    pass
