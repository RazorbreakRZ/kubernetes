from mathematics import app, CORS, request
cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})

database = {

}

@app.route('/v1/configuration/getproperty',methods=['POST'])
def getProperty():
    print request.get_json()
    response = "<html><body><p><b>NS_NOTIFICATION</b></p><p>%MAIL_CONTENT%</p></body></html>"
    return response, 200
print " - Mapped endpoint: /v1/configuration/getproperty"

@app.route('/v1/configuration/getproperties',methods=['POST'])
def getProperties():
    print request.get_json()
    response = response = {
        "NS_NOTIFICATION": "<html><body><p><b>NS_NOTIFICATION</b></p><p>%MAIL_CONTENT%</p></body></html>",
        "NS_EXTERNAL_SIGN": "<html><body><p><b>NS_EXTERNAL_SIGN</b></p><p>%MAIL_CONTENT%</p></body></html>"
    }
    return response, 200
print " - Mapped endpoint: /v1/configuration/getproperties"

@app.route('/v1/configuration/postproperty',methods=['POST'])
def postProperty():
    print request.get_json()
    response = {}
    return response, 201
print " - Mapped endpoint: /v1/configuration/postproperty"

@app.route('/v1/configuration/postproperties',methods=['POST'])
def postProperties():
    print request.get_json()
    response = {}
    return response, 201
print " - Mapped endpoint: /v1/configuration/postproperties"

@app.route('/v1/configuration/gettemplate',methods=['POST'])
def getTemplate():
    requestJson = request.get_json()
    print requestJson
    nameTemplate = requestJson["nameTemplate"]
    response = ""
    responseCode = 404
    if database.has_key(nameTemplate):
        response = database.get(nameTemplate)
        responseCode = 200
    return response, responseCode
print " - Mapped endpoint: /v1/configuration/gettemplate"

@app.route('/v1/configuration/gettemplates',methods=['POST'])
def getTemplates():
    requestJson = request.get_json()
    print requestJson
    response = {
        "templates": list(database.keys())
    }
    responseCode = 200
    return response, responseCode
print " - Mapped endpoint: /v1/configuration/gettemplates"

@app.route('/v1/configuration/posttemplate',methods=['POST'])
def postTemplate():
    requestJson = request.get_json()
    print requestJson
    database[requestJson["nameTemplate"]] = requestJson["template"]
    response = {}
    return response, 201
print " - Mapped endpoint: /v1/configuration/posttemplate"

@app.route('/v1/configuration/generatepdf',methods=['POST'])
def generatePdf():
    requestJson = request.get_json()
    print requestJson
    response = "MA=="
    return response, 200
print " - Mapped endpoint: /v1/configuration/generatepdf"