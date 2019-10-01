import click
import pytest
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


@pytest.mark.authentication
def test_authentication_api(runner, cli, auth_options):
    result = runner.invoke(cli, ['v1-2-10', *auth_options, '--help'])
    assert not result.exception
    assert result.output.splitlines() == ['Usage: main v1-2-10 [OPTIONS] COMMAND [ARGS]...',
        '',
        '  DNA Center API v1.2.10',
        '',
        '',
        '',
        'Options:',
        '  -u, --username TEXT             HTTP Basic Auth username.',
        '  -p, --password TEXT             HTTP Basic Auth password.',
        '  -ea, --encoded_auth TEXT        HTTP Basic Auth base64 encoded string.',
        '  --base_url TEXT                 The base URL to be prefixed to the individual',
        '                                  API endpoint suffixes.  [default:',
        '                                  https://sandboxdnac2.cisco.com:443]',
        '  --single_request_timeout INTEGER',
        '                                  Timeout (in seconds) for RESTful HTTP',
        '                                  requests.  [default: 60]',
        '  --wait_on_rate_limit BOOLEAN    Enables or disables automatic rate-limit',
        '                                  handling.  [default: True]',
        "  --verify BOOLEAN                Controls whether to verify the server's TLS", 
        '                                  certificate.  [default: True]',
        '  -d, --debug BOOLEAN             Controls whether to log information about DNA',
        "                                  Center APIs' request and response process.",
        '                                  [default: False]',
        '  --help                          Show this message and exit.',
        '',
        'Commands:',
        '  clients              DNA Center Clients API (version: 1.2.10).',
        '  command-runner       DNA Center Command Runner API (version: 1.2.10).',
        '  devices              DNA Center Devices API (version: 1.2.10).',
        '  fabric-wired         DNA Center Fabric Wired API (version: 1.2.10).',
        '  file                 DNA Center File API (version: 1.2.10).',
        '  network-discovery    DNA Center Network Discovery API (version: 1.2.10).',
        '  networks             DNA Center Networks API (version: 1.2.10).',
        '  non-fabric-wireless  DNA Center Non-Fabric Wireless API (version: 1.2.10).',
        '  path-trace           DNA Center Path Trace API (version: 1.2.10).',
        '  pnp                  DNA Center PnP API (version: 1.2.10).',
        '  site-profile         DNA Center Site Profile API (version: 1.2.10).',
        '  sites                DNA Center Sites API (version: 1.2.10).',
        '  swim                 DNA Center SWIM API (version: 1.2.10).',
        '  tag                  DNA Center Tag API (version: 1.2.10).',
        '  task                 DNA Center Task API (version: 1.2.10).',
        '  template-programmer  DNA Center Template Programmer API (version: 1.2.10).']