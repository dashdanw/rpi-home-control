from flask import Flask
from flask import render_template
from flask import make_response

import json

from lib import powerswitch

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/on/')
def on():
    state = powerswitch.on()
    return json.dumps(state)

@app.route('/off/')
def off():
    state = powerswitch.off()
    return json.dumps(state)

@app.route('/toggle/')
def toggle():
    state = powerswitch.toggle()
    return json.dumps(state)

@app.route('/state/')
def state():
    state = powerswitch.state()
    return json.dumps(state)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8817, debug=True)
