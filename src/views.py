import uuid
from src import app
from flask import jsonify, request
import datetime

users = {}
categories = {}

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


@app.get("/category")
def categories_get():
    return list(categories.values())

@app.post("/category")
def create_category():
    category_name = request.args.get("name")
    category_id = uuid.uuid4().hex
    category = {
        "id": category_id,
        "category_name":category_name
    }
    categories[category_id] = category
    return category

@app.delete("/category/<category_id>")
def category_delete(category_id):
    if category_id in categories:
        del categories[category_id]
        return "", 204
    else:
        return "Category not found", 404

if __name__ == "__main__":
    app.run()