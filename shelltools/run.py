import os
import sys
import shlex
import subprocess

from shelltools import base_string_class


class std_output(base_string_class):
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

    __metaclass__ = runmeta

    @classmethod
    def create_process(cls, command, cwd, env, shell=False):
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

    def __new__(cls, *args, **kwargs):

        env = dict(os.environ)
        env.update(kwargs.get('env', {}))

        cwd = kwargs.get('cwd')
        data = kwargs.get('data')

        for command in args:
            process = cls.create_process(command, cwd, env)

            stdout, stderr = process.communicate(data)

            stdout = stdout.rstrip("\n")
            stderr = stderr.rstrip("\n")

            out = stdout if stdout else stderr

            obj = std_output.__new__(run, out)

            obj.stdout = std_output(stdout)
            obj.stderr = std_output(stderr)
            obj.status = process.returncode
            obj.command = command

            data = obj.stdout

        return obj


if __name__ == "__main__":
    pass
