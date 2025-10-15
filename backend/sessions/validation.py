from DB.models.User import CheckSessionId, GetSessionData


def handle_validation(data : dict) -> dict: 
    sessionid = data["sessionid"]
    validate = CheckSessionId(sessionid)
    
    if validate:
        user_data = GetSessionData(sessionid)
        return {
            "method": "POST", 
            "status": "Success", 
            "user_data": user_data, 
        }
        
    else: 
        return {
            "method": "POST", 
            "status": "Failed", 
        }
        
    