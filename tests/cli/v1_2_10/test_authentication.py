import click
import pytest
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate
from tests.environment import (
    DNA_CENTER_USERNAME, DNA_CENTER_PASSWORD,
    DNA_CENTER_ENCODED_AUTH
)


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.authentication
def test_authentication_api(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'authentication', 'authentication-api', '''--username=DNA_CENTER_USERNAME''', '''--password=DNA_CENTER_PASSWORD''', '''--encoded_auth=DNA_CENTER_ENCODED_AUTH'''])
    assert not result.exception
