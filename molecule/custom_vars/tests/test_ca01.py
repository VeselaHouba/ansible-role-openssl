import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ca01')


def test_certs_exists(host):
    file1 = host.file("/opt/ssl/ca/ca.crt")
    file2 = host.file("/opt/ssl/certificates/node01.crt")
    assert file1.exists
    assert file2.exists
