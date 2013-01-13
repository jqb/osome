import os
import sys
import shlex
import locale
import subprocess


class CrossPlatform(object):
    def _process(self, command, cwd, env, shell=False):
        return subprocess.Popen(
            shlex.split(command),
            universal_newlines=True,
            shell=shell,
            cwd=cwd,
            env=env,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=0,
        )

    def posix_process(self, command, cwd, env, shell=False):
        return self._process(command, cwd, env, shell=shell)

    def nt_process(self, command, cwd, env, shell=True):
        return self._process(command, cwd, env, shell=shell)

    default_process = posix_process

    def process(self, *args, **kwargs):
        function = getattr(self, "%s_process" % os.name, self.default_process)
        return function(*args, **kwargs)

    @classmethod
    def system_encoding(cls):
        return locale.getdefaultlocale()[1]


class std_output(unicode):
    @property
    def lines(self):
        return self.split("\n")

    @property
    def qlines(self):
        return [line.split() for line in self.split("\n")]


class runmeta(type):
    @property
    def stdin(cls):
        return sys.stdin.read()


class run(std_output):
    _plaftorm = CrossPlatform()

    __metaclass__ = runmeta

    def __new__(cls, *args, **kwargs):

        env = dict(os.environ)
        env.update(kwargs.get('env', {}))

        cwd = kwargs.get('cwd')
        data = kwargs.get('data')
        system_encoding = cls._plaftorm.system_encoding()

        for command in args:
            process = cls._plaftorm.process(command, cwd, env)

            stdout, stderr = process.communicate(
                data
            )

            stdout = stdout.rstrip("\n")
            stderr = stderr.rstrip("\n")

            out = stdout if stdout else stderr

            obj = std_output.__new__(run, out, system_encoding)

            obj.stdout = std_output(stdout, system_encoding)
            obj.stderr = std_output(stderr, system_encoding)
            obj.status = process.returncode
            obj.command = command

            data = obj.stdout

        return obj


if __name__ == "__main__":
    pass
