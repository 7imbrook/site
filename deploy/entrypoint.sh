#!/bin/bash

# TODO: this needs set in deploy
export RELEASE_STAGE=prerelease

echo "Performing pre startup tasks"
echo "Template bin:" $(which consul-template)
echo "Consul host:" $CONSUL_HTTP_ADDR
echo "Vault host:" $VAULT_ADDR
echo "Stage:" $RELEASE_STAGE

cleanup() {
    # Logout of consul here
    echo "Exiting and shutting down"
}

trap cleanup EXIT;

# make migrations, only do this in prerelease
consul-template -config /opt/deploy/consul-template.hcl -once -exec "python ./manage.py migrate"

# TODO, make sure they we migrate correctly, 

# Run
consul-template -config /opt/deploy/consul-template.hcl