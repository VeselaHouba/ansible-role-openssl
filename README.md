# OpenSSL

Ansible role for managing simple self-signed SSL infrastructure.

## Dependencies
N/A

## Usage

### Install role

```
ansible-galaxy install veselahouba.openssl
```

Using requirements.yml is recommended.

### Configuration

Following variables makes sense to check:

- `openssl_ca_controller`: Put inventory hostname of your CA here
- `openssl_cert_group`: Put hosts which should have SSL cert generated into this group
- `openssl_cert_cn`: Override on host level, otherwise `ansible_fqdn` will be used as default


### Example

#### inventory

```
[ca]
ca01

[ssl_hosts]
node01
node02
```

#### playbook

```YAML
- name: Deploy OpenSSL infrastructure
  become: true
  hosts: all
  roles:
    - veselahouba.openssl
  vars:
    openssl_ca_controller: ca
    openssl_cert_group: ssl_hosts
```

Results in
- CA deployed to `/opt/ssl/` on `ca01` host
- Certs for `node01` and `node02` signed and saved on `ca` (including keys)
- Certs for `node01` and `node02` deployed to `/opt/ssl/certificates` on respective machines.
- CA public part deployed to `/opt/ssl/certificates/ca.crt` on node01/node02. So it's not best idea to call your CA host `ca` ;)


### More info
For more detailed info and options consult `defaults/main.yml` file
