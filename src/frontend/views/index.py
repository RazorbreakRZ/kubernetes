from flask import render_template
from frontend import app

@app.route('/')
def index():
    return render_template('index.html')
print " - Mapped endpoint: /"