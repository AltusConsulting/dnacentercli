import click
import pytest
from tests.environment import DNA_CENTER_VERSION


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.api
def test_basic_help(runner, main):
    result = runner.invoke(main, ['--help'])
    assert not result.exception
    assert '[OPTIONS] COMMAND [ARGS]...' in result.output


@pytest.mark.api
@pytest.mark.clients
def test_get_client_detail(runner, main):
    result = runner.invoke(main, [ 'v1-2-10', 'clients', 'get-client-detail', '''--mac_address=devices.response[0].macAddress''',  '''--timestamp=None''',  '''--payload=None''',  '''--active_validation=True''' ])
    assert not result.exception


@pytest.mark.api
@pytest.mark.clients
def test_get_overall_client_health(runner, main):
    result = runner.invoke(main, [ 'v1-2-10', 'clients', 'get-overall-client-health', '''--timestamp=None''',  '''--payload=None''',  '''--active_validation=True''' ])
    assert not result.exception

