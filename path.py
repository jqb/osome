import os
import shutil
import fnmatch


class path(unicode):

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

    def ls(self, patern="*"):
        return path_list([path(e) for e in os.listdir(self) if fnmatch.fnmatch(e, patern)])

    def ls_files(self, patern="*"):
        return [e for e in self.ls(patern) if (self / e).is_file()]

    def ls_dirs(self, patern="*"):
        return [e for e in self.ls(patern) if (self / e).is_dir()]

    def chmod(self, mod):
        return self

    def open(self, *args, **kwargs):
        return open(self, *args, **kwargs)

    def __div__(self, other):
        return path(os.path.join(self, other))

    @classmethod
    def join(cls, *path_list):
        return path(os.path.join(*path_list))


class path_list(list):
    pass



if __name__ == "__main__":
    pass
