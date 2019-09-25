#!/bin/bash

IMAGE=$1
VERSION=$2

if [ -z "${IMAGE}" ]; then
    IMAGE=frontend
fi

if [ -z "${VERSION}" ]; then
    VERSION=1.0
fi

echo sudo docker build -t io/djmartinez/$IMAGE:$VERSION $IMAGE