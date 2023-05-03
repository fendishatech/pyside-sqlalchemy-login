from src.models.repository import register_user, login, logout


def main():
    # Login test
    login_result = login("test", "12345")
    print("Login successful:", login_result)
    
    logout()

if __name__ == "__main__":
    main()