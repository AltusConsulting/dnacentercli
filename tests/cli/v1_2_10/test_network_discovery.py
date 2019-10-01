import click
import pytest
from tests.environment import DNA_CENTER_VERSION


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.network_discovery
def test_delete_all_discovery(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'delete-all-discovery', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_create_cli_credentials(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'create-cli-credentials', '''--payload=[{
            "username": "test_user_devnet",
            "password": "NO!$DATA!$"
        }]''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_create_netconf_credentials(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'create-netconf-credentials', '''--payload=[{
            "netconfPort": '65533'  # range of 1 to 65535
        }]''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_create_snmp_write_community(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'create-snmp-write-community', '''--payload=[{
            "writeCommunity": "NO!$DATA!$",
            "description": "created snmpv2"
        }]''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_create_snmp_read_community(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'create-snmp-read-community', '''--payload=[{
            "readCommunity": "NO!$DATA!$",
            "description": "created snmpv2"
        }]''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_create_http_write_credentials(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'create-http-write-credentials', '''--payload=[{
            "username": "test_user_devnet",
            "password": "W.~&KV9ha",
            "port": 8080
        }]''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_create_http_read_credentials(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'create-http-read-credentials', '''--payload=[{
            "username": "test_user_devnet",
            "password": "W.~&KV9ha",
            "port": 8080
        }]''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_create_update_snmp_properties(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'create-update-snmp-properties', '''--payload=[{
            "intValue": 1,
            "systemPropertyName": "version"
        }]''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_create_snmpv3_credentials(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'create-snmpv3-credentials', '''--payload=[{
            "snmpMode": "NOAUTHNOPRIV",
            "username": "test_user_devnet"
        }]''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_credential_sub_type_by_credential_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-credential-sub-type-by-credential-id', '''--id=get_global_credentials(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_snmp_properties(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-snmp-properties', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_start_discovery(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'start-discovery', '''--cdpLevel=16''', '''--discoveryType='CDP'''', '''--enablePasswordList=None''', '''--globalCredentialIdList=credentialIdList[0:5]''', '''--httpReadCredential=None''', '''--httpWriteCredential=None''', '''--ipAddressList='10.10.22.22'''', '''--ipFilterList=None''', '''--lldpLevel=None''', '''--name='start_discovery_test'''', '''--netconfPort='65535'''', '''--noAddNewDevice=None''', '''--parentDiscoveryId=None''', '''--passwordList=None''', '''--preferredMgmtIPMethod=None''', '''--protocolOrder='ssh'''', '''--reDiscovery=None''', '''--retry=None''', '''--snmpAuthPassphrase=None''', '''--snmpAuthProtocol=None''', '''--snmpMode=None''', '''--snmpPrivPassphrase=None''', '''--snmpPrivProtocol=None''', '''--snmpROCommunity=None''', '''--snmpROCommunityDesc=None''', '''--snmpRWCommunity=None''', '''--snmpRWCommunityDesc=None''', '''--snmpUserName=None''', '''--snmpVersion=None''', '''--timeout=None''', '''--updateMgmtIp=None''', '''--userNameList=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_count_of_all_discovery_jobs(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-count-of-all-discovery-jobs', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_discoveries_by_range(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-discoveries-by-range', '''--records_to_return=10''', '''--start_index=1''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_network_devices_from_discovery(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-network-devices-from-discovery', '''--id=get_discoveries_by_range(api).response[0].id''', '''--cli_status=None''', '''--http_status=None''', '''--ip_address=None''', '''--netconf_status=None''', '''--ping_status=None''', '''--snmp_status=None''', '''--sort_by=None''', '''--sort_order=None''', '''--task_id=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_discovery_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-discovery-by-id', '''--id=get_discoveries_by_range(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_list_of_discoveries_by_discovery_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-list-of-discoveries-by-discovery-id', '''--id=get_discoveries_by_range(api).response[0].id''', '''--ip_address=None''', '''--limit=None''', '''--offset=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_discovery_jobs_by_ip(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-discovery-jobs-by-ip', '''--ip_address=get_discoveries_by_range(api).response[0].ipAddressList.split('-')[0]''', '''--limit=None''', '''--name=None''', '''--offset=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_discovered_devices_by_range(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-discovered-devices-by-range', '''--id=filtered_discoveries[0].id''', '''--records_to_return=3''', '''--start_index=1''', '''--task_id=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_devices_discovered_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-devices-discovered-by-id', '''--id=get_discoveries_by_range(api).response[0].id''', '''--task_id=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_global_credentials(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-global-credentials', '''--credential_sub_type='CLI'''', '''--order=None''', '''--sort_by=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_get_discovered_network_devices_by_discovery_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'get-discovered-network-devices-by-discovery-id', '''--id=get_discoveries_by_range(api).response[0].id''', '''--task_id=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_delete_discovery_by_specified_range(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'delete-discovery-by-specified-range', '''--records_to_delete=3''', '''--start_index=800''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_update_netconf_credentials(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'update-netconf-credentials', '''--comments=None''', '''--credentialType=None''', '''--description=None''', '''--id=list(filter(lambda x: x.netconfPort == '65533'''', '''--credentials))[0].id''', '''--instanceTenantId=None''', '''--instanceUuid=None''', '''--netconfPort='65532'''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_update_global_credentials(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'update-global-credentials', '''--global_credential_id=list(filter(lambda x: x.netconfPort == '65532'''', '''--credentials))[0].id''', '''--siteUuids=[]''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_netconf(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'delete-global-credentials-by-id-netconf', '''--global_credential_id=list(filter(lambda x: x.netconfPort == '65532'''', '''--credentials))[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_update_snmp_write_community(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'update-snmp-write-community', '''--comments=None''', '''--credentialType=None''', '''--description='created snmpv2_write'''', '''--id=list(filter(lambda x: x.description == 'created snmpv2'''', '''--credentials))[0].id''', '''--instanceTenantId=None''', '''--instanceUuid=None''', '''--writeCommunity='NO!$DATA!$'''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_update_snmp_read_community(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'update-snmp-read-community', '''--comments=None''', '''--credentialType=None''', '''--description='created snmpv2_read'''', '''--id=list(filter(lambda x: x.description == 'created snmpv2'''', '''--credentials))[0].id''', '''--instanceTenantId=None''', '''--instanceUuid=None''', '''--readCommunity='NO!$DATA!$'''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_update_cli_credentials(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'update-cli-credentials', '''--comments=None''', '''--credentialType=None''', '''--description='test: user devnet credentials'''', '''--enablePassword=None''', '''--id=list(filter(lambda x: x.username == 'test_user_devnet'''', '''--credentials))[0].id''', '''--instanceTenantId=None''', '''--instanceUuid=None''', '''--password='NO!$DATA!$'''', '''--username='test_user_devnet'''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_snmp_write(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'delete-global-credentials-by-id-snmp-write', '''--global_credential_id=list(filter(lambda x: x.description == 'created snmpv2_write'''', '''--credentials))[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_snmp_read(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'delete-global-credentials-by-id-snmp-read', '''--global_credential_id=list(filter(lambda x: x.description == 'created snmpv2_read'''', '''--credentials))[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_cli(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'delete-global-credentials-by-id-cli', '''--global_credential_id=list(filter(lambda x: x.username == 'test_user_devnet'''', '''--credentials))[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_update_http_write_credentials(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'update-http-write-credentials', '''--comments=None''', '''--credentialType=None''', '''--description='created http_write'''', '''--id=list(filter(lambda x: x.username == 'test_user_devnet'''', '''--credentials))[0].id''', '''--instanceTenantId=None''', '''--instanceUuid=None''', '''--password='W.~&KV9ha'''', '''--port=8080''', '''--secure=None''', '''--username='test_user_devnet'''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_update_http_read_credential(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'update-http-read-credential', '''--comments=None''', '''--credentialType=None''', '''--description='created http_write'''', '''--id=list(filter(lambda x: x.username == 'test_user_devnet'''', '''--credentials))[0].id''', '''--instanceTenantId=None''', '''--instanceUuid=None''', '''--password='W.~&KV9ha'''', '''--port=8080''', '''--secure=None''', '''--username='test_user_devnet'''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_update_snmpv3_credentials(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'update-snmpv3-credentials', '''--authPassword=None''', '''--authType=None''', '''--comments=None''', '''--credentialType=None''', '''--description='created snmpv3'''', '''--id=list(filter(lambda x: x.username == 'test_user_devnet'''', '''--credentials))[0].id''', '''--instanceTenantId=None''', '''--instanceUuid=None''', '''--privacyPassword=None''', '''--privacyType=None''', '''--snmpMode='NOAUTHNOPRIV'''', '''--username='test_user_devnet'''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_http_write(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'delete-global-credentials-by-id-http-write', '''--global_credential_id=list(filter(lambda x: x.username == 'test_user_devnet'''', '''--credentials))[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_http_read(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'delete-global-credentials-by-id-http-read', '''--global_credential_id=list(filter(lambda x: x.username == 'test_user_devnet'''', '''--credentials))[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_snmpv3(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'delete-global-credentials-by-id-snmpv3', '''--global_credential_id=list(filter(lambda x: x.username == 'test_user_devnet'''', '''--credentials))[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_updates_discovery_by_id_active(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'updates-discovery-by-id-active', '''--attributeInfo=None''', '''--cdpLevel=None''', '''--deviceIds=None''', '''--discoveryCondition=None''', '''--discoveryStatus=discovery.discoveryStatus''', '''--discoveryType=None''', '''--enablePasswordList=None''', '''--globalCredentialIdList=None''', '''--httpReadCredential=None''', '''--httpWriteCredential=None''', '''--id=discovery.id''', '''--ipAddressList=None''', '''--ipFilterList=None''', '''--isAutoCdp=None''', '''--lldpLevel=None''', '''--name=None''', '''--netconfPort=None''', '''--numDevices=None''', '''--parentDiscoveryId=None''', '''--passwordList=None''', '''--preferredMgmtIPMethod=None''', '''--protocolOrder=None''', '''--retryCount=None''', '''--snmpAuthPassphrase=None''', '''--snmpAuthProtocol=None''', '''--snmpMode=None''', '''--snmpPrivPassphrase=None''', '''--snmpPrivProtocol=None''', '''--snmpRoCommunity=None''', '''--snmpRoCommunityDesc=None''', '''--snmpRwCommunity=None''', '''--snmpRwCommunityDesc=None''', '''--snmpUserName=None''', '''--timeOut=None''', '''--updateMgmtIp=None''', '''--userNameList=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_updates_discovery_by_id_inactive(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'updates-discovery-by-id-inactive', '''--attributeInfo=None''', '''--cdpLevel=None''', '''--deviceIds=None''', '''--discoveryCondition=None''', '''--discoveryStatus=discovery.discoveryStatus''', '''--discoveryType=None''', '''--enablePasswordList=None''', '''--globalCredentialIdList=None''', '''--httpReadCredential=None''', '''--httpWriteCredential=None''', '''--id=discovery.id''', '''--ipAddressList=None''', '''--ipFilterList=None''', '''--isAutoCdp=None''', '''--lldpLevel=None''', '''--name=None''', '''--netconfPort=None''', '''--numDevices=None''', '''--parentDiscoveryId=None''', '''--passwordList=None''', '''--preferredMgmtIPMethod=None''', '''--protocolOrder=None''', '''--retryCount=None''', '''--snmpAuthPassphrase=None''', '''--snmpAuthProtocol=None''', '''--snmpMode=None''', '''--snmpPrivPassphrase=None''', '''--snmpPrivProtocol=None''', '''--snmpRoCommunity=None''', '''--snmpRoCommunityDesc=None''', '''--snmpRwCommunity=None''', '''--snmpRwCommunityDesc=None''', '''--snmpUserName=None''', '''--timeOut=None''', '''--updateMgmtIp=None''', '''--userNameList=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.network_discovery
def test_delete_discovery_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'network-discovery', 'delete-discovery-by-id', '''--id=discovery_to_delete[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
