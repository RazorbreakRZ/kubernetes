from flask import request
from mathematics import app
from mathematics.services import arithmeticOperators

@app.route('/api/v1/sum')
def sum():
    a = request.args.get('a', default = 0, type = int)
    b = request.args.get('b', default = 0, type = int)
    return {"value": arithmeticOperators.sumAPlusB(a, b)}
print " - Mapped endpoint: /api/v1/sum"

@app.route('/api/v1/multiply')
def multiplication():
    a = request.args.get('a', default = 0, type = int)
    b = request.args.get('b', default = 0, type = int)
    return {"value": arithmeticOperators.multiplyAByB(a, b)}
print " - Mapped endpoint: /api/v1/multiply"

@app.route('/api/v1/divide')
def division():
    a = request.args.get('a', default = 0, type = int)
    b = request.args.get('b', default = 0, type = int)
    return {"value": arithmeticOperators.divideAByB(a, b)}
print " - Mapped endpoint: /api/v1/divide"

@app.route('/api/v1/pow')
def pow():
    a = request.args.get('a', default = 0, type = int)
    b = request.args.get('b', default = 0, type = int)
    return {"value": arithmeticOperators.powAToB(a, b)}
print " - Mapped endpoint: /api/v1/pow"