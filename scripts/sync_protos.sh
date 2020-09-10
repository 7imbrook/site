#!/bin/bash

REPO_LOCATION=/Users/timbrook/Projects/twilio-sender

mkdir -p protos

for file in $(git -C $REPO_LOCATION ls-files protos); do
    # TODO: check that version is commited?
    cp $REPO_LOCATION/$file ./protos
done;
