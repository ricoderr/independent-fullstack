from DB.models.User import InsertUser
from passlib.hash import argon2


def handle_signup(data): 
    
    username = data["username"]
    email = data["email"]
    password = data["password"]
    hashed_password = argon2.hash(password) # My boy does salting too with hashing.

    resp = InsertUser(username=username, email=email, password=hashed_password)
    
    return resp

