from flask import render_template
from frontend import app
from frontend.services import mathematics

@app.route('/maths/random')
def random():
    randomNumber = mathematics.getRandomValue()
    return render_template('maths-random.html', value=randomNumber)
print " - Mapped endpoint: /maths/random"
