import os
import shutil
import fnmatch


class path(unicode):

    def __new__(cls, *args):
        if len(args) > 1:
            return unicode.__new__(path, cls.join(*args))
        return unicode.__new__(path, *args)

    def exists(self):
        return os.path.exists(self)

    def absolute(self):
        return path(os.path.abspath(self))

    def is_dir(self):
        return os.path.isdir(self)

    def is_file(self):
        return os.path.isfile(self)

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
        # len(self.ls)
        # if not r:
        shutil.copy(self, target)

    def touch(self):
        open(self, "a")
        return self

    def ls(self, pattern="*", sort=lambda e: (not e.is_dir(), e)):
        content = [path(e) for e in os.listdir(self) if fnmatch.fnmatch(e, pattern)]
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

    @classmethod
    def join(cls, *path_list):
        return path(os.path.join(*path_list))


if __name__ == "__main__":
    pass
