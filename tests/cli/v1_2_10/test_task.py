import click
import pytest
from tests.environment import DNA_CENTER_VERSION


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.task
def test_get_tasks(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'task', 'get-tasks', '''--data=None''', '''--end_time=None''', '''--error_code=None''', '''--failure_reason=None''', '''--is_error=None''', '''--limit=None''', '''--offset=None''', '''--order=None''', '''--parent_id=None''', '''--progress=None''', '''--service_type=None''', '''--sort_by=None''', '''--start_time=None''', '''--username=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.task
def test_get_task_tree(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'task', 'get-task-tree', '''--task_id=get_tasks(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.task
def test_get_task_count(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'task', 'get-task-count', '''--data=None''', '''--end_time=None''', '''--error_code=None''', '''--failure_reason=None''', '''--is_error=None''', '''--parent_id=None''', '''--progress=None''', '''--service_type=None''', '''--start_time=None''', '''--username=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.task
def test_get_task_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'task', 'get-task-by-id', '''--task_id=get_tasks(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.task
def test_get_task_by_operationid(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'task', 'get-task-by-operationid', '''--limit=1''', '''--offset=0''', '''--operation_id=filtered_tasks[0].operationIdList[0]''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
