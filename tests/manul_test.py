import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import register_user, get_users, find_user, update_password, delete_user, login, logout, get_db_path_and_name

def test_repository ():
    print("Started testing")
    # Test the functionalities

    # Get database name.
    print(get_db_path_and_name())

    # Get table information.

    # Register user.
    # register_user("test1", "12345")

    # Find user by username.
    user = find_user("test1")

    # Update password.
    user = find_user("test1")
    update_password(user,"test1")

    # Delete user.
    user = find_user("test1")
    update_password(user,"test1")

    # Login test
    login_result = login("test", "12345")
    print("Login successful:", login_result)

    users = get_users()
    for user in users :
        print(f"Username : {user.username} && Password : {user.password}")
    
    logout()

if __name__ == "__main__":
    test_repository()