import click
import pytest
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.tag
def test_create_tag(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'create-tag', '''--description=None''', '''--dynamicRules=None''', '''--id=None''', '''--instanceTenantId=None''', '''--name='InterestingTool01'''', '''--systemTag=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_get_tag(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'get-tag', '''--additional_info_attributes=None''', '''--additional_info_name_space=None''', '''--field=None''', '''--level=None''', '''--limit=None''', '''--name=None''', '''--offset=None''', '''--order='des'''', '''--size=None''', '''--sort_by='name'''', '''--system_tag=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_get_tag_created(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'get-tag-created', '''--additional_info_attributes=None''', '''--additional_info_name_space=None''', '''--field=None''', '''--level=None''', '''--limit=None''', '''--name='InterestingTool01'''', '''--offset=None''', '''--order=None''', '''--size=None''', '''--sort_by=None''', '''--system_tag=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_get_tag_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'get-tag-by-id', '''--id=get_tag(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_get_tag_by_id_created(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'get-tag-by-id-created', '''--id=get_tag_created(api).response[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_get_tag_count(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'get-tag-count', '''--attribute_name=None''', '''--level=None''', '''--name=None''', '''--name_space=None''', '''--size=None''', '''--system_tag=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_get_tag_resource_types(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'get-tag-resource-types', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_get_tag_member_count(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'get-tag-member-count', '''--id=get_tag(api).response[0].id''', '''--member_type=get_tag_resource_types(api).response[0]''', '''--level='0'''', '''--member_association_type=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_updates_tag_membership(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'updates-tag-membership', '''--memberToTags={key: [tag]}''', '''--memberType='networkdevice'''', '''--payload=None''', '''--active_validation=False'''])
    assert not result.exception


@pytest.mark.tag
def test_add_members_to_the_tag(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'add-members-to-the-tag', '''--id=get_tag_created(api).response[0].id''', '''--payload={
            "networkdevice": [api.devices.get_device_list().response[0].id]
        }''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_get_tag_members_by_id(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'get-tag-members-by-id', '''--id=get_tag_created(api).response[0].id''', '''--member_type=get_tag_resource_types(api).response[0]''', '''--level='0'''', '''--limit=None''', '''--member_association_type=None''', '''--offset=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_update_tag(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'update-tag', '''--description=None''', '''--dynamicRules=None''', '''--id=tag.id''', '''--instanceTenantId=None''', '''--name='{} Updated'.format(tag.name)''', '''--systemTag=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_remove_tag_member(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'remove-tag-member', '''--id=tag.id''', '''--member_id=device.id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.tag
def test_delete_tag(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'tag', 'delete-tag', '''--id=tag.id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
