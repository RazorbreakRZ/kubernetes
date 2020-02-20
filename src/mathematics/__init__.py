#!/usr/bin/python
from flask import Flask, escape, request
from flask_cors import CORS

service_status = { "status": "DOWN" }
service_info = {
    "group": "io.djmartinez",
    "name": __name__,
    "version": 2,
    "api_version": 1,
    "author": "djmartinez"
}

app = Flask(__name__)

import mathematics.views

print " ~ Service status is: %s" % service_status["status"]