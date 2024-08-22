# main.py
from level_one import level_one
from level_two import level_two
from level_three import level_three

def authenticate():
    """Main authentication process combining all three levels."""
    print("Starting Three-Level Authentication")
    
    if level_one() and level_two() and level_three():
        print("Access Granted!")
    else:
        print("Access Denied!")

if __name__ == "__main__":
    authenticate()
