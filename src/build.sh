#!/bin/bash
REPO=djmartinez.io
IMAGE=$1
VERSION=$2

if [ -z "${IMAGE}" ]; then
    IMAGE=frontend
fi

if [ -z "${VERSION}" ]; then
    VERSION=1.0
fi

sudo docker rmi -f $REPO/$IMAGE:$VERSION
sudo docker build -t $REPO/$IMAGE:$VERSION $IMAGE