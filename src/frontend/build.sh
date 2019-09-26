#!/bin/bash
REPO=djmartinez.io
IMAGE=frontend
VERSION=$1

sudo docker rmi -f $REPO/$IMAGE:$VERSION
sudo docker build -t $REPO/$IMAGE:$VERSION .