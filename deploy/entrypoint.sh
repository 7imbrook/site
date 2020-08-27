#!/bin/bash

# TODO: this needs set in deploy
export CONSUL_HTTP_SSL_VERIFY=false

echo "Performing pre startup tasks"
echo "Template bin:" $(which consul-template)
echo "Consul host:" $CONSUL_HTTP_ADDR
echo "Vault host:" $VAULT_ADDR
echo "Stage:" $RELEASE_STAGE

cleanup() {
    # Logout of consul here
    echo "Exiting and shutting down"
    consul logout -token-file ./token
}

trap cleanup EXIT;

consul login -method kubernetes -token-sink-file ./token -bearer-token-file /var/run/secrets/kubernetes.io/serviceaccount/token

# make migrations, only do this in prerelease
consul-template -config /opt/deploy/consul-template.hcl -once -exec "python ./manage.py migrate" -consul-token=$(cat ./token)

# TODO, make sure they we migrate correctly, 

# Run
consul-template -config /opt/deploy/consul-template.hcl -consul-token=$(cat ./token)