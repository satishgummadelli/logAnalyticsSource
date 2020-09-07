#!/bin/bash
USER_NAME=satishgummadelli
REPO_NAME=loganalytics

docker build . --tag $REPO_NAME:$1
docker tag $REPO_NAME:$1 $USER_NAME/$REPO_NAME:$1
docker push $USER_NAME/$REPO_NAME:$1
