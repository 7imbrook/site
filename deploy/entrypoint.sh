#!/bin/bash

echo "Performing pre startup tasks"
echo "Template bin:" $(which consul-template)
echo "Consul host:" $CONSUL_HTTP_ADDR
echo "Vault host:" $VAULT_ADDR

consul-template -config /opt/deploy/consul-template.hcl