import os
from pathlib import Path
import pytoml
from shutil import copy
from testpath import assert_isfile

from flit import tomlify

samples_dir = Path(__file__).parent / 'samples'

def test_tomlify(copy_sample, monkeypatch):
    td = copy_sample('entrypoints_valid')
    monkeypatch.chdir(td)

    tomlify.main(argv=[])

    pyproject_toml = (td / 'pyproject.toml')
    assert_isfile(pyproject_toml)

    with pyproject_toml.open(encoding='utf-8') as f:
        content = pytoml.load(f)

    assert 'build-system' in content
    assert 'tool' in content
    assert 'flit' in content['tool']
    flit_table = content['tool']['flit']
    assert 'metadata' in flit_table
    assert 'scripts' in flit_table
    assert 'entrypoints' in flit_table
