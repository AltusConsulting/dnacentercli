import click
import pytest
from tests.environment import DNA_CENTER_VERSION


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.path_trace
def test_initiate_a_new_pathtrace(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'path-trace', 'initiate-a-new-pathtrace', '''--controlPath=None''', '''--destIP=ipAddressList[-1] if len(ipAddressList) > 0 else "10.20.10.1"''', '''--destPort=None''', '''--inclusions=None''', '''--periodicRefresh=None''', '''--protocol=None''', '''--sourceIP=ipAddressList[0] if len(ipAddressList) > 0 else "10.20.10.1"''', '''--sourcePort=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.path_trace
def test_deletes_pathtrace_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'path-trace', 'deletes-pathtrace-by-id', '''--flow_analysis_id=retrives_all_previous_pathtraces_summary(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.path_trace
def test_retrieves_previous_pathtrace(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'path-trace', 'retrieves-previous-pathtrace', '''--flow_analysis_id=initiate_a_new_pathtrace(api).response.flowAnalysisId''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.path_trace
def test_retrives_all_previous_pathtraces_summary(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'path-trace', 'retrives-all-previous-pathtraces-summary', '''--dest_ip=None''', '''--dest_port=None''', '''--gt_create_time=None''', '''--last_update_time=None''', '''--limit=None''', '''--lt_create_time=None''', '''--offset=None''', '''--order=None''', '''--periodic_refresh=None''', '''--protocol=None''', '''--sort_by=None''', '''--source_ip=ipAddressList[0] if len(ipAddressList) > 0 else "10.20.10.1"''', '''--source_port=None''', '''--status=None''', '''--task_id=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
