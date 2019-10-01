import click
import pytest
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.networks
def test_get_vlan_details(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'networks', 'get-vlan-details', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.networks
def test_get_site_topology(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'networks', 'get-site-topology', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.networks
def test_get_physical_topology(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'networks', 'get-physical-topology', '''--node_type=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.networks
def test_get_l3_topology_details(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'networks', 'get-l3-topology-details', '''--topology_type='OSPF'''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.networks
def test_get_topology_details(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'networks', 'get-topology-details', '''--vlan_id=get_vlan_details(api).response[0]''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.networks
def test_get_overall_network_health(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'networks', 'get-overall-network-health', '''--timestamp=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
