import click
import pytest
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.template_programmer
def test_gets_the_templates_available(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'gets-the-templates-available', '''--filter_conflicting_templates=None''', '''--product_family=None''', '''--product_series=None''', '''--product_type=None''', '''--project_id=None''', '''--software_type=None''', '''--software_version=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_get_projects(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'get-projects', '''--name=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_get_template_details(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'get-template-details', '''--template_id=templateID''', '''--latest_version=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_get_template_versions(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'get-template-versions', '''--template_id=templateID''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_create_project(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'create-project', '''--createTime=None''', '''--description=None''', '''--id=None''', '''--lastUpdateTime=None''', '''--name='test_project'''', '''--tags=None''', '''--templates=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_create_template(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'create-template', '''--project_id=filtered_project[0].id''', '''--author=None''', '''--composite=False''', '''--containingTemplates=[]''', '''--createTime=None''', '''--description=None''', '''--deviceTypes=[
            {
                "productFamily": "Switches and Hubs",
                # "productSeries": "Cisco Catalyst 9300 Series Switches",
                # "productType": "Cisco Catalyst 9300 Switch"
            }
        ]''', '''--failurePolicy=None''', '''--id=None''', '''--lastUpdateTime=None''', '''--name='test_template'''', '''--parentTemplateId=None''', '''--projectId=None''', '''--projectName=None''', '''--rollbackTemplateContent=''''', '''--rollbackTemplateParams=[]''', '''--softwareType='IOS-XE'''', '''--softwareVariant='XE'''', '''--softwareVersion=None''', '''--tags=None''', '''--templateContent='show version\n'''', '''--templateParams=[]''', '''--version=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_update_template(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'update-template', '''--author=None''', '''--composite=template.composite''', '''--containingTemplates=template.containingTemplates''', '''--createTime=None''', '''--description=None''', '''--deviceTypes=template.deviceTypes''', '''--failurePolicy=None''', '''--id=template.id''', '''--lastUpdateTime=None''', '''--name=template.name + '_updated'''', '''--parentTemplateId=None''', '''--projectId=template.projectId''', '''--projectName=None''', '''--rollbackTemplateContent=template.rollbackTemplateContent''', '''--rollbackTemplateParams=template.rollbackTemplateParams''', '''--softwareType=template.softwareType''', '''--softwareVariant=template.softwareVariant''', '''--softwareVersion=None''', '''--tags=None''', '''--templateContent=template.templateContent''', '''--templateParams=template.templateParams''', '''--version=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_update_project(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'update-project', '''--createTime=None''', '''--description=None''', '''--id=filtered_project[0].id''', '''--lastUpdateTime=None''', '''--name=filtered_project[0].name + '_updated'''', '''--tags=None''', '''--templates=None''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_version_template(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'version-template', '''--comments=None''', '''--templateId=template.id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_preview_template(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'preview-template', '''--params=None''', '''--templateId=template.id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_deploy_template(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'deploy-template', '''--forcePushTemplate=True''', '''--isComposite=template.composite''', '''--mainTemplateId=template.parentTemplateId''', '''--memberTemplateDeploymentInfo=None''', '''--targetInfo=[{'id': t.managementIpAddress,
                    'type': 'MANAGED_DEVICE_IP'''', '''--'params': {}} for t in target]''', '''--templateId=template.id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_get_template_deployment_status(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'get-template-deployment-status', '''--deployment_id=deploymentID''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_delete_template(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'delete-template', '''--template_id=template.id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception


@pytest.mark.template_programmer
def test_delete_project(runner, main):
    result = runner.invoke(main, ['v1-2-10', 'template-programmer', 'delete-project', '''--project_id=filtered_project[0].id''', '''--payload=None''', '''--active_validation=True'''])
    assert not result.exception
