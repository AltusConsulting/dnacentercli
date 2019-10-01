import click
import pytest
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate
from tests.config import (NEW_ENTERPRISE_SSID_NAME,
                          NEW_MANAGED_APLOCATIONS)


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.non_fabric_wireless
def test_create_enterprise_ssid(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'non-fabric-wireless', 'create-enterprise-ssid', '''--enableBroadcastSSID=None''', '''--enableFastLane=None''', '''--enableMACFiltering=None''', '''--fastTransition=None''', '''--name=None''', '''--passphrase=None''', '''--radioPolicy=None''', '''--securityLevel=None''', '''--trafficType=None''', '''--payload={}''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.skipif(not all([NEW_ENTERPRISE_SSID_NAME]) is True,
                    reason="tests.config values required not present")
@pytest.mark.non_fabric_wireless
def test_get_enterprise_ssid(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'non-fabric-wireless', 'get-enterprise-ssid', '''--ssid_name=NEW_ENTERPRISE_SSID_NAME''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.non_fabric_wireless
def test_create_and_provision_ssid(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'non-fabric-wireless', 'create-and-provision-ssid', '''--enableFabric=None''', '''--flexConnect=None''', '''--managedAPLocations=None''', '''--ssidDetails=None''', '''--ssidType=None''', '''--vlanAndDynamicInterfaceDetails=None''', '''--payload={}''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.skipif(not all([NEW_MANAGED_APLOCATIONS, NEW_ENTERPRISE_SSID_NAME]) is True,
                    reason="tests.config values required not present")
@pytest.mark.non_fabric_wireless
def test_delete_and_provision_ssid(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'non-fabric-wireless', 'delete-and-provision-ssid', '''--managed_aplocations=NEW_MANAGED_APLOCATIONS''', '''--ssid_name=NEW_ENTERPRISE_SSID_NAME''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.skipif(not all([NEW_ENTERPRISE_SSID_NAME]) is True,
                    reason="tests.config values required not present")
@pytest.mark.non_fabric_wireless
def test_delete_enterprise_ssid(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'non-fabric-wireless', 'delete-enterprise-ssid', '''--ssid_name=NEW_ENTERPRISE_SSID_NAME''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
