#!/bin/bash

echo "Performing pre startup tasks"
echo "Template bin:" $(which consul-template)
echo "Consul host:" $CONSUL_HTTP_ADDR
echo "Vault host:" $VAULT_ADDR

# make migrations
consul-template -config /opt/deploy/consul-template.hcl -once -exec "python ./manage.py migrate"

# Run
consul-template -config /opt/deploy/consul-template.hcl