import sys
from shelltools import run


# dafault commands
class commands:
    ls = 'ls -la'
    rm = 'rm -r'
    more = 'more'


# override commands for windows plaftorm
if sys.platform.startswith('win'):
    class commands:
        ls = 'dir'
        rm = 'rmdir'
        more = 'more'


def test_run():
    output = run(commands.ls)

    assert output.lines
    assert output

    assert isinstance(output, unicode)
    assert isinstance(output.lines, list)

    assert isinstance(output.qlines, list)
    assert isinstance(output.qlines[0], list)


def test_stdout():
    assert run(commands.ls).stdout.lines
    assert run(commands.ls).stdout


def test_stderr():
    assert run('%s not_existing_directory' % commands.rm).stderr
    assert run('%s not_existing_directory' % commands.rm).stderr.lines


def test_status():
    assert run(commands.ls).status == 0
    assert run('%s not_existing_directory' % commands.rm).status != 0  # win workaround


def test_pipe():
    assert run(commands.ls, commands.more).status == 0

