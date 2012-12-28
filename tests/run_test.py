from shelltools import run


def test_run():
    output = run('ls -la')

    assert output.lines
    assert output

    assert isinstance(output, unicode)
    assert isinstance(output.lines, list)

    assert isinstance(output.q_lines, list)
    assert isinstance(output.q_lines[0], list)


def test_stdout():
    assert run('ls -la').stdout.lines
    assert run('ls -la').stdout


def test_stderr():
    assert run('rm not_existing_directory').stderr
    assert run('rm not_existing_directory').stderr.lines


def test_status():
    assert run('ls -la').status == 0
    assert run('rm not_existing_directory').status == 1


def test_pipe():
    assert run('ls -la', 'wc -l').status == 0
