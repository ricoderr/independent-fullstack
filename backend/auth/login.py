from DB.models.User import CheckUser, SelectUser
from passlib.hash import argon2
def handle_login(data): 
    email = data["email"]
    password = data["password"] 
    
    if CheckUser(email=email): 
        try: 
            user_data = SelectUser(email=email)
            user_pass = user_data["password"]
            authenticated = argon2.verify(password, user_pass)
            if authenticated: 
                return {
                    "method": "POST", 
                    "status": "Success",
                    "message": "LoggedIn Successfully!", 
                    "user_data": {
                        "username": user_data["username"],
                        "email": user_data["email"],
                        "sessionid": user_data["sessionid"]
                    }
                }
            else: 
                return {
                    "method": "POST", 
                    "status": "Failed",
                    "message": "Wrong Password!", 
                }
        except Exception as e: 
            return{
                "method": "POST", 
                "status": "Failed",
                "message": f"Error occured while authenticating. {e}", 
            }
    
    else : 
        return {
            "method": "POST", 
            "status": "Failed", 
            "message": "User with this email doesn't exists."
        }
    
