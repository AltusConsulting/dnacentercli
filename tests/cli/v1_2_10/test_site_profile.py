import click
import pytest
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate
from tests.config import SITE_PROFILE_DEVICE_IP


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.skipif(not all([SITE_PROFILE_DEVICE_IP]) is True,
                    reason="tests.config values required not present")
@pytest.mark.site_profile
def test_get_device_details_by_ip(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'site-profile', 'get-device-details-by-ip', '''--device_ip=SITE_PROFILE_DEVICE_IP''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.site_profile
def test_provision_nfv(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'site-profile', 'provision-nfv', '''--callbackUrl=None''', '''--provisioning=None''', '''--siteProfile=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
