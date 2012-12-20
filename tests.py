import os
import shutil

import pytest

from path import path


root = 'xxx'

dir_1 = 'dir_1'
dir_2 = 'dir_2'
dir_1_path = os.path.join(root, dir_1)
dir_2_path = os.path.join(root, dir_2)
dir_list = [dir_1, dir_2]

file_1 = 'file_1'
file_2 = 'file_2'
file_1_path = os.path.join(root, file_1)
file_2_path = os.path.join(root, file_2)
file_list = [file_1, file_2]


def setup_function(function):
    os.mkdir(root)

    for dir in dir_list:
        os.mkdir(os.path.join(root, dir))

    for file in file_list:
        open(os.path.join(root, file), "w").write("")


def teardown_function(function):
    shutil.rmtree(root)


def test_exists():
    assert path(dir_1_path).exists()
    assert path(file_1_path).exists()


def test_absolute():
    assert os.path.abspath(file_1_path) == path(file_1_path).absolute()


def test_is_dir():
    assert path(dir_1_path).is_dir()
    assert path(dir_2_path).is_dir()

    assert not path(file_1_path).is_dir()
    assert not path(file_2_path).is_dir()


def test_is_file():
    assert path(file_1_path).is_file()
    assert path(file_2_path).is_file()

    assert not path(dir_1_path).is_file()
    assert not path(dir_2_path).is_file()


def test_mkdir():
    path_string = os.path.join(root, "test")
    path(path_string).mkdir()

    assert os.path.exists(path_string)
    assert os.path.isdir(path_string)


def test_mkdir_p():
    path_string = os.path.join(root, "level1", "level2")
    path(path_string).mkdir(p=True)

    assert os.path.exists(path_string)
    assert os.path.isdir(path_string)


def test_rm():
    path(file_1_path).rm()
    assert not os.path.exists(file_1_path)

    path(dir_1_path).rm()
    assert not os.path.exists(dir_1_path)

    file_location = os.path.join(dir_2_path, 'xxx')
    open(file_location, "w")

    with pytest.raises(OSError):
        path(dir_2_path).rm()
    assert os.path.exists(dir_2_path)

    path(dir_2_path).rm(p=True)
    assert not os.path.exists(dir_2_path)


# def test_cp():
#     dir_location = os.path.join(dir_2_path, 'xxx')
#     os.mkdir(dir_location)

#     # with pytest.raises(IOError):
#     path(dir_2_path).cp(dir_1_path)


def test_touch():
    path_string = os.path.join(root, "test")
    path(path_string).touch()

    assert os.path.exists(path_string)
    assert os.path.isfile(path_string)

def test_ls():
    dir_content = path(root).ls()
    assert len(dir_content) == len(dir_list + file_list)
    assert set(dir_list).issubset(dir_content)
    assert set(file_list).issubset(dir_content)


def test_ls_files():
    dir_content = path(root).ls_files()
    assert len(dir_content) == len(file_list)

    assert not set(dir_list).issubset(dir_content)
    assert set(file_list).issubset(dir_content)


def test_ls_dirs():
    dir_content = path(root).ls_dirs()

    assert len(dir_content) == len(dir_list)

    assert set(dir_list).issubset(dir_content)
    assert not set(file_list).issubset(dir_content)


def test__div__():
    joined_path = path(root) / path(file_1)
    assert joined_path.exists()

    joined_path = path(root) / file_1
    assert joined_path.exists()

    joined_path = path(root) / path(file_1) / path("xxx")
    assert not joined_path.exists()

    joined_path = path(root) / path(file_1) / "xxx"
    assert not joined_path.exists()


def test_join():
    assert path.join(root, file_1).exists()
    assert not path.join(root, file_1, 'xxx').exists()

