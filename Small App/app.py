from flask import Flask, request, render_template, jsonify
import os
import json

app = Flask(__name__)
directory = 'Users/'


# view all users
@app.route('/users/')
def index():
    files = list()
    for root, dirs, file_names in os.walk(directory):
        for f in file_names:
            files.append(json.load(open(directory + f)))
    return jsonify(users=files)


# show user based on username
@app.route('/users/<username>')
def show(username):
    filename = directory + username + '.json'
    if os.path.exists(filename):
        with open(filename) as obj:
            return jsonify(json.load(obj))
    else:
        return "User not found!"


# create user
@app.route('/users/', methods=['POST'])
def create():
    username = request.form.get("username", str)
    email = request.form.get("email", str)
    age = request.form.get("age", int)
    filename = directory + username + '.json'
    data = {'username': username, 'email': email, 'age': age}
    if not os.path.exists(filename):
        with open(filename, 'w') as obj:
            json.dump(data, obj)
            return "User created successfully"
    return "User already exists!"


# delete user
@app.route('/users/', methods=['DELETE'])
def delete():
    username = request.form.get("username", str)
    filename = directory + username + ".json"
    if os.path.exists(filename):
        os.remove(filename)
        return "User deleted successfully"
    else:
        return "User is not found"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
