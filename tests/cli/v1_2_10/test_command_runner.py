import click
import pytest
from tests.environment import DNA_CENTER_VERSION


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.command_runner
def test_get_all_keywords_of_clis_accepted(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'command-runner', 'get-all-keywords-of-clis-accepted', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.command_runner
def test_run_read_only_commands_on_devices(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'command-runner', 'run-read-only-commands-on-devices', '''--commands=['show']''', '''--description=None''', '''--deviceUuids=[get_device_list(api).response[0].id]''', '''--name=None''', '''--timeout=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
