#!/bin/bash

docker build -t 7imbrook/site:canary .
docker push 7imbrook/site:canary | tee ./push.log
consul kv put site/deployment/tag $(tail -n 1 ./push.log | awk '{print $3}')

sleep 5
kubectl rollout status deploy personal-site-prerelease