import click
import pytest
from json import loads
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate
from dnacentersdk import mydict_data_factory


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


# @pytest.mark.task
# def test_get_tasks(runner, cli, auth_options):
#     result = runner.invoke(cli, ['v1-2-10', *auth_options, 'task', 'get-tasks', '''--data=None''', '''--end_time=None''', '''--error_code=None''', '''--failure_reason=None''', '''--is_error=None''', '''--limit=None''', '''--offset=None''', '''--order=None''', '''--parent_id=None''', '''--progress=None''', '''--service_type=None''', '''--sort_by=None''', '''--start_time=None''', '''--username=None''', '''--payload=None''', '''--active_validation=True'''])
#     assert not result.exception
#     if result.output.strip():
#         obj = loads(result.output)
#         assert json_schema_validate('jsd_e78bb8a2449b9eed_v1_2_10').validate(obj) is None


# @pytest.mark.task
# def test_get_task_tree(runner, cli, auth_options):
#     result = runner.invoke(cli, ['v1-2-10', *auth_options, 'task', 'get-task-tree', '''--task_id=get_tasks(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
#     assert not result.exception
#     if result.output.strip():
#         obj = loads(result.output)
#         assert json_schema_validate('jsd_f5a269c44f2a95fa_v1_2_10').validate(obj) is None


# @pytest.mark.task
# def test_get_task_count(runner, cli, auth_options):
#     result = runner.invoke(cli, ['v1-2-10', *auth_options, 'task', 'get-task-count', '''--data=None''', '''--end_time=None''', '''--error_code=None''', '''--failure_reason=None''', '''--is_error=None''', '''--parent_id=None''', '''--progress=None''', '''--service_type=None''', '''--start_time=None''', '''--username=None''', '''--payload=None''', '''--active_validation=True'''])
#     assert not result.exception
#     if result.output.strip():
#         obj = loads(result.output)
#         assert json_schema_validate('jsd_26b44ab04649a183_v1_2_10').validate(obj) is None


# @pytest.mark.task
# def test_get_task_by_id(runner, cli, auth_options):
#     result = runner.invoke(cli, ['v1-2-10', *auth_options, 'task', 'get-task-by-id', '''--task_id=get_tasks(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
#     assert not result.exception
#     if result.output.strip():
#         obj = loads(result.output)
#         assert json_schema_validate('jsd_a1a9387346ba92b1_v1_2_10').validate(obj) is None


# @pytest.mark.task
# def test_get_task_by_operationid(runner, cli, auth_options):
#     result = runner.invoke(cli, ['v1-2-10', *auth_options, 'task', 'get-task-by-operationid', '''--limit=1''', '''--offset=0''', '''--operation_id=filtered_tasks[0].operationIdList[0]''', '''--payload=None''', '''--active_validation=True'''])
#     assert not result.exception
#     if result.output.strip():
#         obj = loads(result.output)
#         assert json_schema_validate('jsd_e487f8d3481b94f2_v1_2_10').validate(obj) is None
