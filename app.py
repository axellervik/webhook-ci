from flask import Flask, jsonify, request
import json

app = Flask(__name__)

usersList = ['Aaron', 'Bianca', 'Cat', 'Danny', 'Elena']

@app.route('/users', methods=['GET'])
def users():
    return jsonify({ 'users': [user for user in usersList] })

@app.route('/user/<int:id>', methods=['GET'])
def userById(id):
    return jsonify({ 'username': usersList[id]  })

@app.route('/user/<string:name>', methods=['GET'])
def getUserByName(name):
    # Show some user information
    return "Some info"

@app.route('/user/<string:name>', methods=['POST'])
def addUserByName(name):
    usersList.append(name)
    return jsonify({ 'message': 'POST'})

# main driver function
if __name__ == '__main__':
    app.run()
