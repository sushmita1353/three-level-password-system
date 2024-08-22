# level_three.py
import random
import time

def level_three():
    """Level 3: Behavioral Verification (CAPTCHA)"""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    start_time = time.time()

    answer = int(input(f"What is {num1} + {num2}? "))

    # Simple behavioral check: answer correctly and within 10 seconds
    if answer == num1 + num2 and (time.time() - start_time) < 10:
        print("Level 3 authentication successful.")
        return True
    else:
        print("Level 3 authentication failed.")
        return False
