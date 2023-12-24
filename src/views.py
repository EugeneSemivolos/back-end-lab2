import uuid
from src import app
from flask import jsonify, request
import datetime


users = {}

@app.get("/user/<user_id>")
def user_get(user_id):
    if(user_id in users):
        return users[user_id]
    else:
        return "User not found", 404

@app.get("/users")
def users_get():
    return list(users.values())

@app.post("/user")
def create_user():
    user_name = request.args.get("name")
    user_id = uuid.uuid4().hex
    user = {
        "id": user_id,
        "user_name":user_name
    }
    users[user_id] = user
    return user

@app.delete("/user/<user_id>")
def user_delete(user_id):
    if(user_id in users):
        del users[user_id]
        return "", 204
    else:
        return "User not found", 404

if __name__ == "__main__":
    app.run()