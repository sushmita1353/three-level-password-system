import hashlib

# Correct username and password hash
USERNAME = "sushmita"
PASSWORD_HASH = hashlib.sha256("Surya1234@".encode()).hexdigest()

def level_one():
    """Level 1: Textual Password Authentication"""
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    if username == USERNAME and password_hash == PASSWORD_HASH:
        print("Level 1 authentication successful.")
        return True
    else:
        print("Level 1 authentication failed.")
        return False

if __name__ == "__main__":
    # Run level_one to test it
    if level_one():
        print("Proceeding to the next level...")
    else:
        print("Access Denied!")
