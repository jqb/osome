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


class run(runmeta('base_run', (std_output, ), {})):
    """
    .. code-block:: python

      >>> from shelltools import run

      >>> print run('uname -r')
      3.7.0-7-generic

      >>> print run('uname -r').stdout
      3.7.0-7-generic

      >>> print run('rm not_existing_directory').stderr
      rm: cannot remove `not_existing_directory': No such file or directory

      >>> print run('ls -la', 'wc -l')
      14

      >>> print run('ls -la', 'wc -l', 'wc -c')
      3

      >>> run('ls -la', 'wc -l', 'wc -c')
      ls -la | wc -l | wc -c

      >>> print run('ls -la').stdout.lines
      ['total 20',
       'drwxrwxr-x 3 user user 4096 Dec 20 22:55 .',
       'drwxrwxr-x 5 user user 4096 Dec 20 22:57 ..',
       'drwxrwxr-x 2 user user 4096 Dec 20 22:37 dir',
       '-rw-rw-r-- 1 user user    0 Dec 20 22:52 file']

    """

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
