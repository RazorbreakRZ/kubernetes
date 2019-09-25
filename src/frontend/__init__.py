#!/usr/bin/python
from flask import Flask
app = Flask(__name__)

service_status = { "status": "DOWN" }
service_info = {
    "group": "io.djmartinez",
    "name": __name__,
    "version": 1,
    "api_version": 1,
    "author": "djmartinez"
}

import frontend.views

print " ~ Service status is: %s" % service_status["status"]