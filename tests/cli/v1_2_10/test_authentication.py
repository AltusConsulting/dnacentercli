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
@pytest.mark.authentication
def test_authentication_api(runner, main):
    result = runner.invoke(main, [ 'v1-2-10', 'authentication', 'authentication-api', '''--username=DNA_CENTER_USERNAME''',  '''--password=DNA_CENTER_PASSWORD''',  '''--encoded_auth=DNA_CENTER_ENCODED_AUTH''' ])
    assert not result.exception

