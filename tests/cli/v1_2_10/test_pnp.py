import click
import pytest
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate
from tests.config import (NEW_VIRTUAL_ACCOUNT_PAYLOAD)


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.pnp
def test_get_smart_account_list(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'get-smart-account-list', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_get_virtual_account_list(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'get-virtual-account-list', '''--domain=get_smart_account_list(api)[0]''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.skipif(not all([NEW_VIRTUAL_ACCOUNT_PAYLOAD]) is True,
                    reason="tests.config values required not present")
@pytest.mark.pnp
def test_add_virtual_account(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'add-virtual-account', '''--autoSyncPeriod=None''', '''--ccoUser=None''', '''--expiry=None''', '''--lastSync=None''', '''--profile=None''', '''--smartAccountId=None''', '''--syncResult=None''', '''--syncResultStr=None''', '''--syncStartTime=None''', '''--syncStatus=None''', '''--tenantId=None''', '''--token=None''', '''--virtualAccountId=None''', '''--payload=NEW_VIRTUAL_ACCOUNT_PAYLOAD''', '''--active_validation=False'''])
    assert not result.exception


@pytest.mark.pnp
def test_get_sync_result_for_virtual_account(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'get-sync-result-for-virtual-account', '''--domain=get_smart_account_list(api)[0]''', '''--name=get_virtual_account_list(api)[0]''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_update_pnp_server_profile(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'update-pnp-server-profile', '''--autoSyncPeriod=None''', '''--ccoUser=None''', '''--expiry=None''', '''--lastSync=None''', '''--profile=None''', '''--smartAccountId=None''', '''--syncResult=None''', '''--syncResultStr=None''', '''--syncStartTime=None''', '''--syncStatus=None''', '''--tenantId=None''', '''--token=None''', '''--virtualAccountId=None''', '''--payload=get_sync_result_for_virtual_account(api)''', '''--active_validation=False'''])
    assert not result.exception


@pytest.mark.pnp
def test_sync_virtual_account_devices(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'sync-virtual-account-devices', '''--autoSyncPeriod=None''', '''--ccoUser=None''', '''--expiry=None''', '''--lastSync=None''', '''--profile=None''', '''--smartAccountId=None''', '''--syncResult=None''', '''--syncResultStr=None''', '''--syncStartTime=None''', '''--syncStatus=None''', '''--tenantId=None''', '''--token=None''', '''--virtualAccountId=None''', '''--payload=get_sync_result_for_virtual_account(api)''', '''--active_validation=False'''])
    assert not result.exception


@pytest.mark.pnp
def test_deregister_virtual_account(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'deregister-virtual-account', '''--domain=get_smart_account_list(api)[0]''', '''--name=get_virtual_account_list(api)[0]''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_get_workflow_count(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'get-workflow-count', '''--name=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_get_workflows(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'get-workflows', '''--limit=None''', '''--name=None''', '''--offset=None''', '''--sort='addedOn'''', '''--sort_order='des'''', '''--type=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_get_pnp_global_settings(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'get-pnp-global-settings', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_update_pnp_global_settings(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'update-pnp-global-settings', '''--_id=None''', '''--aaaCredentials=None''', '''--acceptEula=None''', '''--defaultProfile=None''', '''--savaMappingList=None''', '''--taskTimeOuts=None''', '''--tenantId=None''', '''--version=None''', '''--payload=get_pnp_global_settings(api)''', '''--active_validation=False'''])
    assert not result.exception


@pytest.mark.pnp
def test_get_device_count(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'get-device-count', '''--cm_state=None''', '''--last_contact=None''', '''--name=None''', '''--onb_state=None''', '''--pid=None''', '''--project_id=None''', '''--project_name=None''', '''--serial_number=None''', '''--smart_account_id=None''', '''--source=None''', '''--state=None''', '''--virtual_account_id=None''', '''--workflow_id=None''', '''--workflow_name=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_import_devices_in_bulk(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'import-devices-in-bulk', '''--payload=[{
            "deviceInfo": {
                "serialNumber": "c3160d2650",
                "name": "Test device c3160d2650"
            }
        }]''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_get_device_list(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'get-device-list', '''--cm_state=None''', '''--last_contact=None''', '''--limit=1''', '''--name=None''', '''--offset=None''', '''--onb_state=None''', '''--pid=None''', '''--project_id=None''', '''--project_name=None''', '''--serial_number=None''', '''--smart_account_id=None''', '''--sort=None''', '''--sort_order=None''', '''--source=None''', '''--state=None''', '''--virtual_account_id=None''', '''--workflow_id=None''', '''--workflow_name=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_get_device_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'get-device-by-id', '''--id=get_device_list(api)[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_get_device_history(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'get-device-history', '''--serial_number=get_device_list(api)[0].deviceInfo.serialNumber''', '''--sort=None''', '''--sort_order=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_add_device_2(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'add-device-2', '''--_id=None''', '''--deviceInfo={'serialNumber': 'FJC2048D0HX'''', '''--'name': 'catalyst_ap_test'''', '''--'pid': 'ISR4431-SEC/K9'}''', '''--runSummaryList=None''', '''--systemResetWorkflow=None''', '''--systemWorkflow=None''', '''--tenantId=None''', '''--version=None''', '''--workflow=None''', '''--workflowParameters=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_preview_config(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'preview-config', '''--deviceId=api.pnp.get_device_list(name='catalyst_ap_test')[0].id''', '''--siteId=siteId''', '''--type='Default'''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_claim_a_device_to_a_site(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'claim-a-device-to-a-site', '''--deviceId=None''', '''--siteId=None''', '''--type=None''', '''--payload={
            "siteId": siteId,
            "deviceId": deviceId,
            "type": "Default",
            "imageInfo": {"imageId": ""''', '''--"skip": False},
            "configInfo": {"configId": ""''', '''--"configParameters": []}
        }''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_delete_device_by_id_from_pnp_imported(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'delete-device-by-id-from-pnp-imported', '''--id=api.pnp.get_device_list(name='Test device c3160d2650')[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_add_device(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'add-device', '''--_id=None''', '''--deviceInfo={'serialNumber': 'd2650c3160'''', '''--'name': 'Test device d2650c3160'}''', '''--runSummaryList=None''', '''--systemResetWorkflow=None''', '''--systemWorkflow=None''', '''--tenantId=None''', '''--version=None''', '''--workflow=None''', '''--workflowParameters=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_update_device(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'update-device', '''--id=api.pnp.get_device_list(name='Test device d2650c3160')[0].id''', '''--_id=None''', '''--deviceInfo={'name': 'Test device d2650c3160-1'}''', '''--runSummaryList=None''', '''--systemResetWorkflow=None''', '''--systemWorkflow=None''', '''--tenantId=None''', '''--version=None''', '''--workflow=None''', '''--workflowParameters=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_add_a_workflow(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'add-a-workflow', '''--_id=None''', '''--addToInventory=None''', '''--addedOn=None''', '''--configId=None''', '''--currTaskIdx=None''', '''--description='test_devnet_1'''', '''--endTime=None''', '''--execTime=None''', '''--imageId=None''', '''--instanceType=None''', '''--lastupdateOn=None''', '''--name='test_devnet_1'''', '''--startTime=None''', '''--state=None''', '''--tasks=[{
            'taskSeqNo': 0,
            'name': 'Config Download',
            'type': 'Config',
            'startTime': 0,
            'endTime': 0,
            'timeTaken': 0,
            'currWorkItemIdx': 0,
            'configInfo': {
                'configId': template.id,
                'configFileUrl': None,
                'fileServiceId': None,
                'saveToStartUp': True,
                'connLossRollBack': True,
                'configParameters': None
            }
        }]''', '''--tenantId=None''', '''--type='Standard'''', '''--useState='Available'''', '''--version=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_get_workflow_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'get-workflow-by-id', '''--id=get_workflows(api)[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_update_workflow(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'update-workflow', '''--id=workflow.id''', '''--_id=None''', '''--addToInventory=None''', '''--addedOn=None''', '''--configId=None''', '''--currTaskIdx=None''', '''--description=workflow.description''', '''--endTime=None''', '''--execTime=None''', '''--imageId=None''', '''--instanceType=None''', '''--lastupdateOn=None''', '''--name=workflow.name''', '''--startTime=None''', '''--state=None''', '''--tasks=workflow.tasks''', '''--tenantId=None''', '''--type=workflow.type''', '''--useState=workflow.useState''', '''--version=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_claim_device(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'claim-device', '''--configFileUrl=None''', '''--configId=None''', '''--deviceClaimList=[
            {
                "configList": configList,
                "deviceId": deviceId
            }
        ]''', '''--fileServiceId=None''', '''--imageId=None''', '''--imageUrl=None''', '''--populateInventory=None''', '''--projectId=None''', '''--workflowId=workflow.id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_un_claim_device(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'un-claim-device', '''--deviceIdList=[deviceId]''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_reset_device(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'reset-device', '''--deviceResetList=[{"deviceId": deviceId''', '''--"configList": [workflow.tasks[0].configInfo]}]''', '''--projectId=None''', '''--workflowId=workflow.id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_delete_workflow_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'delete-workflow-by-id', '''--id=api.pnp.get_workflows(name='test_devnet_1')[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_delete_device_by_id_from_pnp_added(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'delete-device-by-id-from-pnp-added', '''--id=api.pnp.get_device_list(name='Test device d2650c3160-1')[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.pnp
def test_delete_device_by_id_from_pnp_added_2(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'pnp', 'delete-device-by-id-from-pnp-added-2', '''--id=api.pnp.get_device_list(name='catalyst_ap_test')[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
