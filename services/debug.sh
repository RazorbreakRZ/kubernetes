#!/bin/bash
ENVIRONMENT=development
SERVICE=frontend
HOST=0.0.0.0
PORT=80

env FLASK_ENV=$ENVIRONMENT FLASK_APP=$SERVICE flask run --host=$HOST --port=$PORT