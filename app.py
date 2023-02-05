from flask import Flask, jsonify, request
import json

app = Flask(__name__)

usersList = ['Apa', 'Banana', 'Cat', 'Bunny', 'Lion']

@app.route('/', methods=['GET'])
def users():
    return jsonify({'users': [user for user in usersList]})

@app.route('/', methods=['POST'])
def status():
    return jsonify({'users': [user for user in usersList]})

# main driver function
if __name__ == '__main__':
    app.run()
