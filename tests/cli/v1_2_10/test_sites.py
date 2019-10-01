import click
import pytest
from tests.environment import DNA_CENTER_VERSION


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.sites
def test_get_site_health(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'sites', 'get-site-health', '''--timestamp=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.sites
def test_create_site(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'sites', 'create-site', '''--site=None''', '''--type=None''', '''--payload={
            'type': 'building',
            'site': {
                'building': {
                    'name': 'Test_Building',
                    'address': '10.10.22.70'
                }
            }
        }''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.sites
def test_assign_device_to_site(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'sites', 'assign-device-to-site', '''--site_id=siteId''', '''--device=[{'ip': device.managementIpAddress}]''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
