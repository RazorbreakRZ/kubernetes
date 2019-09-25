from mathematics import app, service_status

@app.route('/health')
def health():
    return service_status
print " - Mapped endpoint: /health"
