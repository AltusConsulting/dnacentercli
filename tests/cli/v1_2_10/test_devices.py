import click
import pytest
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate
from tests.config import MERAKI_ORG_ID


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.devices
def test_get_device_interface_count(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-interface-count', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_list(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-list', '''--associated_wlc_ip=None''', '''--collection_interval=None''', '''--collection_status=None''', '''--error_code=None''', '''--error_description=None''', '''--family=None''', '''--hostname=None''', '''--id=None''', '''--license_name=None''', '''--license_status=None''', '''--license_type=None''', '''--location=None''', '''--location_name=None''', '''--mac_address=None''', '''--management_ip_address=None''', '''--module_equpimenttype=None''', '''--module_name=None''', '''--module_operationstatecode=None''', '''--module_partnumber=None''', '''--module_servicestate=None''', '''--module_vendorequipmenttype=None''', '''--not_synced_for_minutes=None''', '''--platform_id=None''', '''--reachability_status=None''', '''--role=None''', '''--serial_number=None''', '''--series=None''', '''--software_type=None''', '''--software_version=None''', '''--type=None''', '''--up_time=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_sync_devices_using_forcesync(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'sync-devices-using-forcesync', '''--force_sync=None''', '''--payload=['get_device_list(api).response[0].id']''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_polling_interval_for_all_devices(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-polling-interval-for-all-devices', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_count(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-count', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_interface_vlans(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-interface-vlans', '''--id=devices_filtered[0].id''', '''--interface_type=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_interfaces_by_specified_range(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-interfaces-by-specified-range', '''--device_id=get_device_list(api).response[0].id''', '''--records_to_return=1''', '''--start_index=3''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_config_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-config-by-id', '''--network_device_id=get_device_list(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_config_count(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-config-count', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_all_interfaces(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-all-interfaces', '''--limit=500''', '''--offset=1''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_interface_details(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-interface-details', '''--device_id=get_device_list(api).response[0].id''', '''--name=get_device_interface_vlans(api).response[0].interfaceName''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_polling_interval_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-polling-interval-by-id', '''--id=get_device_list(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_module_count(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-module-count', '''--device_id=get_device_list(api).response[0].id''', '''--name_list=None''', '''--operational_state_code_list=None''', '''--part_number_list=None''', '''--vendor_equipment_type_list=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_interface_info_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-interface-info-by-id', '''--device_id=get_device_list(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_summary(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-summary', '''--id=get_device_list(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_functional_capability_for_devices(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-functional-capability-for-devices', '''--device_id=get_device_list(api).response[0].id''', '''--function_name=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_interface_count_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-interface-count-by-id', '''--device_id=get_device_list(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_modules(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-modules', '''--device_id=get_device_list(api).response[0].id''', '''--limit=None''', '''--name_list=None''', '''--offset=None''', '''--operational_state_code_list=None''', '''--part_number_list=None''', '''--vendor_equipment_type_list=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_wireless_lan_controller_details_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-wireless-lan-controller-details-by-id', '''--id=get_device_list(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.skipif(not all([MERAKI_ORG_ID]) is True,
                    reason="tests.config values required not present")
@pytest.mark.devices
def test_get_organization_list_for_meraki(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-organization-list-for-meraki', '''--id=filtered_device_list[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_ospf_interfaces(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-ospf-interfaces', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_functional_capability_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-functional-capability-by-id', '''--id=functional_capability.id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_isis_interfaces(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-isis-interfaces', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_config_for_all_devices(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-config-for-all-devices', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_interface_by_ip(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-interface-by-ip', '''--ip_address=filtered_interfaces[0].ipv4Address''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_network_device_by_ip(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-network-device-by-ip', '''--ip_address=get_device_list(api).response[0].managementIpAddress''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-by-id', '''--id=get_device_list(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_sync_devices(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'sync-devices', '''--cliTransport=None''', '''--computeDevice=None''', '''--enablePassword=None''', '''--extendedDiscoveryInfo=None''', '''--httpPassword=None''', '''--httpPort=None''', '''--httpSecure=None''', '''--httpUserName=None''', '''--ipAddress=None''', '''--merakiOrgId=None''', '''--netconfPort=None''', '''--password=None''', '''--serialNumber=None''', '''--snmpAuthPassphrase=None''', '''--snmpAuthProtocol=None''', '''--snmpMode=None''', '''--snmpPrivPassphrase=None''', '''--snmpPrivProtocol=None''', '''--snmpROCommunity=None''', '''--snmpRWCommunity=None''', '''--snmpRetry=None''', '''--snmpTimeout=None''', '''--snmpUserName=None''', '''--snmpVersion=None''', '''--type=None''', '''--updateMgmtIPaddressList=None''', '''--userName=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_interface_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-interface-by-id', '''--id=get_all_interfaces(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_by_serial_number(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-by-serial-number', '''--serial_number=filtered_device_list[0].serialNumber''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_network_device_by_pagination_range(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-network-device-by-pagination-range', '''--records_to_return=4''', '''--start_index=1''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_retrieves_all_network_devices(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'retrieves-all-network-devices', '''--associated_wlc_ip=None''', '''--collection_interval=None''', '''--collection_status=None''', '''--error_code=None''', '''--family=None''', '''--hostname=get_device_list(api).response[0].hostname''', '''--limit=None''', '''--mac_address=None''', '''--management_ip_address=None''', '''--offset=None''', '''--platform_id=None''', '''--reachability_failure_reason=None''', '''--reachability_status=None''', '''--role=None''', '''--role_source=None''', '''--serial_number=None''', '''--series=None''', '''--software_type=None''', '''--software_version=None''', '''--type=None''', '''--up_time=None''', '''--vrf_name=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_detail(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-detail', '''--identifier='macAddress'''', '''--search_by=get_device_list(api).response[0].macAddress''', '''--timestamp=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_module_info_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-module-info-by-id', '''--id=get_device_list(api).response[0].lineCardId.split(',')[0]''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_add_device(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'add-device', '''--cliTransport=None''', '''--computeDevice=None''', '''--enablePassword=None''', '''--extendedDiscoveryInfo=None''', '''--httpPassword=None''', '''--httpPort=None''', '''--httpSecure=None''', '''--httpUserName=None''', '''--ipAddress=[new_ipAddress]''', '''--merakiOrgId=None''', '''--netconfPort=None''', '''--password=None''', '''--serialNumber=None''', '''--snmpAuthPassphrase=None''', '''--snmpAuthProtocol=None''', '''--snmpMode=None''', '''--snmpPrivPassphrase=None''', '''--snmpPrivProtocol=None''', '''--snmpROCommunity=None''', '''--snmpRWCommunity=None''', '''--snmpRetry=None''', '''--snmpTimeout=None''', '''--snmpUserName=None''', '''--snmpVersion=None''', '''--type=None''', '''--updateMgmtIPaddressList=None''', '''--userName=None''', '''--payload={
            "cliTransport": "ssh",
            "enablePassword": "false",
            "snmpMode": "NOAUTHNOPRIV",
            "snmpROCommunity": credentials[0].id,
            "snmpRWCommunity": "",
            "snmpRetry": 0,
            "snmpTimeout": 0,
            "snmpUserName": "test_user_devnet",
            "snmpVersion": "v2",
            "type": "NETWORK_DEVICE",
            "userName": "test_user_devnet",
            "password": "W.~&KV9ha"
        }''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_get_device_by_id_last(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'get-device-by-id-last', '''--id=get_device_list(api).response[-1].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_update_device_role(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'update-device-role', '''--id=get_device_list(api).response[0].id''', '''--role=get_device_list(api).response[0].role''', '''--roleSource=get_device_list(api).response[0].roleSource''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_register_device_for_wsa(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'register-device-for-wsa', '''--macaddress=get_device_list(api).response[0].macAddress''', '''--serial_number=get_device_list(api).response[0].serialNumber''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_export_device_list(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'export-device-list', '''--deviceUuids=[get_device_list(api).response[0].id]''', '''--id=get_device_list(api).response[0].id''', '''--operationEnum='CREDENTIALDETAILS'''', '''--parameters=None''', '''--password=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.devices
def test_delete_device_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'devices', 'delete-device-by-id', '''--id=filtered_device_list[0].id''', '''--is_force_delete=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
