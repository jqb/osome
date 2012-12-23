import os
import shlex
import subprocess


class std_output(unicode):

    @property
    def lines(self):
        return self.split("\n")

    @property
    def q_lines(self):
        return [line.split() for line in self.split("\n")]


class run(std_output):

    def __new__(cls, command, environment_variables=None, cwd=None, data=None):

        env = dict(os.environ)
        env.update(env or {})

        process = subprocess.Popen(
            shlex.split(command),
            universal_newlines=True,
            shell=False,
            cwd=cwd,
            env=env,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=0,
        )

        stdout, stderr = process.communicate(data)

        stdout = stdout.rstrip("\n")
        stderr = stderr.rstrip("\n")

        obj = std_output.__new__(run, stdout)

        obj.stdout = std_output(stdout)
        obj.stderr = std_output(stderr)
        obj.status = process.returncode
        obj.command = command

        return obj

    def run(self, command):
        return run(command, data=self)


if __name__ == "__main__":
    pass
