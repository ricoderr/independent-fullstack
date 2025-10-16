from DB.models.User import CheckSessionId, GetSessionData


def handle_validation(sessionid : str) -> dict: 
    if not sessionid:
        return {
            "method": "POST",
            "status": "Failed",
            "error": f"Missing session ID, sessionid = {sessionid}"
        }
        
    validate = CheckSessionId(sessionid)
    print(validate) # Debug
    if validate:
        user_data = GetSessionData(sessionid)
        return {
            "method": "POST", 
            "status": "Success", 
            "user_data": user_data, 
        }
        
     
    return {
        "method": "POST", 
        "status": "Failed", 
    }
     
    