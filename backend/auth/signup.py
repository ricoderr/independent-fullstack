from DB.User import InsertUser
from passlib.hash import argon2


def handle_signup(data): 
    
    username = data["username"]
    email = data["email"]
    password = data["password"]
    hashed_password = argon2.hash(password)

    resp = InsertUser(username=username, email=email, password=hashed_password)
    
    return resp

