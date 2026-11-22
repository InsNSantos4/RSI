# slide 12 da aula REST-API:

# !/usr/bin/env python
# encoding: utf-8

import json
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})

app.run()



# slide 13 da aula REST-API:

# !/usr/bin/env python
# encoding: utf-8
from flask import jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'alice',
                       'email': 'alice@outlook.com'})

app.run()