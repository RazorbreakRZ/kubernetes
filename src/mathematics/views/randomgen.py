from mathematics import app
from mathematics.services import randomgen

@app.route('/api/v1/random')
def random():
    return {"value": randomgen.generateRandom()}
print " - Mapped endpoint: /api/v1/random"