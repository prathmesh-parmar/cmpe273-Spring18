from flask import Flask
from flask import request
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

dicto = {}

@app.route('/users', methods=['POST'])
def login():
    req_data = request.get_json()
    user_id = req_data['user_id']
    name = req_data['name']
    dicto[user_id] = name
    temp = {user_id : name}
    string = "{"+'"id"' + ":" + str(user_id) + ", " + '"name"' + ":" +'"' + name + '"'+ "}"
    return string, 201

@app.route("/users/<user_id>")
def get_users(user_id):
    #print(dicto)
    name = dicto[int(user_id)]
    temp = {user_id : name}
    string = "{"+'"id"' + ":" + user_id + ", " + '"name"' + ":" +'"' + name + '"'+ "}"
    return string

@app.route("/users/<user_id>", methods=['DELETE'])
def delete_entry(user_id):
    dicto.pop(user_id, None)
    return "...",204