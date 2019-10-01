import click
import pytest
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.file
def test_get_list_of_available_namespaces(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'file', 'get-list-of-available-namespaces', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.file
def test_get_list_of_files(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'file', 'get-list-of-files', '''--name_space=get_list_of_available_namespaces(api).response[0]''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.file
def test_download_a_file_by_fileid(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'file', 'download-a-file-by-fileid', '''--file_id=get_list_of_files(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
