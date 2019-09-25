#!/bin/bash
ENVIRONMENT=development
SERVICE=$1
HOST=0.0.0.0
PORT=80

if [ -z "$SERVICE" ]; then
    SERVICE=frontend
fi

env FLASK_ENV=$ENVIRONMENT FLASK_APP=$SERVICE flask run --host=$HOST --port=$PORT