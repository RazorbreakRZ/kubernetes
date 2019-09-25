from flask import render_template
from frontend import app

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
print " - Mapped endpoint: /hello/"
print " - Mapped endpoint: /hello/<name>"
