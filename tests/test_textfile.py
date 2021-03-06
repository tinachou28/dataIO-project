#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest
from dataIO import textfile

path = os.path.abspath(__file__)

with open(path, "rb") as f:
    f_lines = [line.decode("utf-8") for line in f]

with open(path, "rb") as f:
    content = f.read().decode("utf-8")


def teardown_module():
    try:
        os.remove("test_textfile.zip")
    except:
        pass


def test_write_zip():
    textfile.write(content, "test_textfile.zip")


def test_read_zip():
    assert content == textfile.read("test_textfile.zip")


def test_readlines():
    result = list(textfile.readlines(path, strip=None))
    assert result == f_lines

    result = list(textfile.readlines(path, skiplines=3, strip=None))
    assert result == f_lines[3:]

    result = list(textfile.readlines(path, nlines=3, strip=None))
    assert result == f_lines[:3]

    result = list(textfile.readlines(path, skiplines=3, nlines=3, strip=None))
    assert result == f_lines[3:3 + 3]


def test_readchunks():
    result = list(textfile.readchunks(path, strip=None))
    assert result[0] == f_lines[0:1]

    result = list(textfile.readchunks(path, skiplines=3, strip=None))
    assert result[0] == f_lines[3:4]

    result = list(textfile.readchunks(path, chunksize=3, strip=None))
    assert result[0] == f_lines[0:3]

    result = list(textfile.readchunks(
        path, skiplines=3, chunksize=3, strip=None))
    assert result[0] == f_lines[3:6]


# def tear_down()
if __name__ == "__main__":
    import os

    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])
