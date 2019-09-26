from frontend import app, service_info

@app.route('/info')
def info():
    return service_info
print " - Mapped endpoint: /info"