from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

d = {'key_1': 'value_1', 'key_2': 'value_2'}

@app.route('/', methods=['GET', 'POST'])
def testing():
    return jsonify(d)
