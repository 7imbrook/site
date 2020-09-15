#!/bin/bash

set -e;

# TODO: this needs set in deploy
export CONSUL_HTTP_SSL_VERIFY=false

echo "Performing pre startup tasks"
echo "Template bin:" $(which consul-template)
echo "Consul host:" $CONSUL_HTTP_ADDR
echo "Vault host:" $VAULT_ADDR
echo "DJANGO_SETTINGS_MODULE:" $DJANGO_SETTINGS_MODULE

export CONSUL_HTTP_TOKEN=$(cat /consul/token/consul-token);

echo "Just running uwsgi"
uwsgi --ini ./conf/uwsgi.ini

# # make migrations, only do this in prerelease
# consul-template -config /opt/deploy/consul-template.hcl -once -exec "python ./manage.py migrate"

# # TODO, make sure they we migrate correctly, 

# # Run
# consul-template -config /opt/deploy/consul-template.hcl 