import os
import shlex
import subprocess


class std_output(unicode):

    def __new__(cls, content):
        obj = unicode.__new__(std_output, content.rstrip("\n"))
        obj.raw = content
        return obj

    @property
    def lines(self):
        return self.split("\n")


class run(object):

    def _parse_args(self,command):
        splitter = shlex.shlex(command)
        splitter.whitespace = '|'
        splitter.whitespace_split = True
        command = []

        while True:
            token = splitter.get_token()
            if token:
                command.append(token)
            else:
                break

        command = list(map(shlex.split, command))
        return command


    def __init__(self, command, environment_variables=None, cwd=None, data=None, chain=None):
        self.command = command
        self.chain = chain or []
        self.chain.append(command)

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

        self.stdout = std_output(stdout)
        self.stderr = std_output(stderr)

        self.status = process.returncode

    def run(self, command):
        return run(command, data=self.stdout.raw, chain=self.chain)

    def __repr__(self):
        return " | ".join(self.chain)

    def __str__(self):
        return "%s" % self.stdout.rstrip("\n")


if __name__ == "__main__":
    import pprint
    print run('ls -la').stdout
    print run('ls -la').status
    pprint.pprint(run('ls -la').stdout.lines)
    print run('find .').run('xargs grep test')
    print run('rm not_existing_directory').stderr
