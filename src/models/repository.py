import hashlib
from .user import User
from .database import session, engine

# Register a user
def register_user(username, password):
    hashed_password = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
    user = User(username=username, password=hashed_password)
    session.add(user)
    session.commit()

# Login
def login(username, password):
    # hash the password using
    hashed_password = hashlib.sha3_256(password.encode('utf-8')).hexdigest() 
    
    # get user and check checked hashed password
    user = find_user(username)
    if user and user.password == hashed_password:
        return True
    return False

# Logout
def logout():
    print("Logout !")

# ---------------------------------------------------------------------------- #
# ------------------------------------ DEV ----------------------------------- #
# ---------------------------------------------------------------------------- #

# Database path and name information information
def get_db_path_and_name():
    return  engine.url.database

def get_users ():
    users = session.query(User)
    return users

# Find a user by username
def find_user(username):
    return session.query(User).filter_by(username=username).first()

# Update a user's password
def update_password(user, new_password):
    hashed_password = hashlib.sha3_256(new_password.encode('utf-8')).hexdigest()
    user.password = hashed_password
    session.commit()

# Delete a user
def delete_user(user):
    session.delete(user)
    session.commit()

