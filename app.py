from flask import Flask, jsonify, request
import json

app = Flask(__name__)

list = ['AAAAAAAAAAAAAa', 'Bunny', 'Cat', 'Duck', 'E']

@app.route('/', methods=['GET'])
def status():
    return jsonify({'GET': [item for item in list]})

@app.route('/', methods=['POST'])
def status():
    return jsonify({'POST': [item for item in list]})

# main driver function
if __name__ == '__main__':
    app.run(debug=True, port=8017)
