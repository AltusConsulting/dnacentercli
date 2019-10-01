import click
import pytest
from tests.environment import DNA_CENTER_VERSION


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.skipif(not all([BORDER_DEVICE_SDA_FABRIC_PATH]) is True,
                    reason="tests.config values required not present")
@pytest.mark.fabric_wired
def test_adds_border_device_in_sda_fabric(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'fabric-wired', 'adds-border-device-in-sda-fabric', '''--sda_border_device=BORDER_DEVICE_SDA_FABRIC_PATH''', '''--payload=[{
            "deviceManagementIpAddress": device.managementIpAddress
        }]''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.skipif(not all([BORDER_DEVICE_SDA_FABRIC_PATH]) is True,
                    reason="tests.config values required not present")
@pytest.mark.fabric_wired
def test_gets_border_device_details_from_sda_fabric(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'fabric-wired', 'gets-border-device-details-from-sda-fabric', '''--device_ip_address=device.managementIpAddress''', '''--sda_border_device=BORDER_DEVICE_SDA_FABRIC_PATH''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.skipif(not all([BORDER_DEVICE_SDA_FABRIC_PATH]) is True,
                    reason="tests.config values required not present")
@pytest.mark.fabric_wired
def test_deletes_border_device_from_sda_fabric(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'fabric-wired', 'deletes-border-device-from-sda-fabric', '''--device_ip_address=device.managementIpAddress''', '''--sda_border_device=BORDER_DEVICE_SDA_FABRIC_PATH''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
