from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/json/<int:id>')
def get_json(id):
    response = jsonify({'id': id, 'name': 'ben'})
    response.status_code = 201
    return response

app.run(host='localhost', port=3001)