from DB.models.User import CheckSessionId, GetSessionData


def handle_validation(sessionid : str) -> dict: 
    if not sessionid:
        return {
            "method": "POST",
            "status": "Failed",
            "error": "Missing session ID"
        }
        
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
        
    