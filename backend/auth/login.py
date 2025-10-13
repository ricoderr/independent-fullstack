from DB.models.User import CheckUser, SelectUser
def handle_login(data): 
    email = data["email"]
    password = data["password"]
    
    
    
