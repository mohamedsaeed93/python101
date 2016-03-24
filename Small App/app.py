from flask import Flask, request, render_template, jsonify
import os
import json
app = Flask(__name__)
indir = 'Users/'

#view all users
@app.route('/users/')
def index():
    files = list()
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            files.append(json.load(open(indir + f)))
    return jsonify(users = files)

#show user based on username
@app.route('/users/<username>')
def show(username):
    file = indir + username +'.json'
    if(os.path.exists(file)): 
       with open(file) as obj:
            return jsonify(json.load(obj))
    else:
        return "User not found!"

#create user
@app.route('/users/', methods=['POST'])
def create():
    username = request.form.get("username",str)
    email = request.form.get("email",str)
    age = request.form.get("age",int)
    file = indir + username + '.json'
    data = { 'username' : username, 'email' : email, 'age' : age }
    if(not os.path.exists(file)): 
        with open(file, 'w') as obj:
            json.dump(data,obj)
            return "User created successfully"
    return "User already exists!"

#delete user
@app.route('/users/', methods =['DELETE'])
def delete():
    username = request.form.get("username",str)
    file = indir + username +".json"
    if(os.path.exists(file)): 
        os.remove(file)
        return "User deleted successfully"
    else:
        return "User is not found"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
