from flask import Flask
import json

cfg = {
    "external_services": {}
}

print " ~ Loading configuration file..."
with open('frontend/config.json') as json_data_file:
    cfg = json.load(json_data_file)

app = Flask(__name__)

service_status = { "status": "DOWN" }
service_info = {
    "group": "io.djmartinez",
    "name": __name__,
    "version": 2,
    "api_version": 1,
    "author": "djmartinez"
}

import frontend.views

print " ~ Service status is: %s" % service_status["status"]