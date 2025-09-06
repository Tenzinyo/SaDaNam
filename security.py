def authenticate_user(username, password, usersdb):
    if usersdb.get(username) == password:
        return True
    else:
        return False
    
def detect_fraudulent_activity(transaction_data):
    if transaction_data.get('amount',0)>1000:
        return True
    else:
        return False
    
    

    