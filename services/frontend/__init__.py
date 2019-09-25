#!/usr/bin/python
from flask import Flask, escape, request, render_template

service_status = { "status": "DOWN" }

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/health')
def health():
    return service_status

service_status["status"] = "UP"

print "Service status is: %s" % service_status["status"]