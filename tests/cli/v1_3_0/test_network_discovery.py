import click
import pytest
from tests.environment import DNA_CENTER_VERSION


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.0', reason='version does not match')


@pytest.mark.api
def test_basic_help(runner, main):
    result = runner.invoke(main, ['--help'])
    assert not result.exception
    assert '[OPTIONS] COMMAND [ARGS]...' in result.output

