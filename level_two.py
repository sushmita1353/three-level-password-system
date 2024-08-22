# level_two.py

# Predefined graphical password (sequence of numbers, could be images)
GRAPHICAL_PASSWORD = [3, 1, 4]

def level_two():
    """Level 2: Graphical Password Authentication"""
    print("Select the correct sequence for graphical password:")
    choices = [1, 2, 3, 4]
    input_sequence = []

    for i in range(3):
        choice = int(input(f"Select number {i+1}: "))
        if choice in choices:
            input_sequence.append(choice)
        else:
            print("Invalid choice.")
            return False

    if input_sequence == GRAPHICAL_PASSWORD:
        print("Level 2 authentication successful.")
        return True
    else:
        print("Level 2 authentication failed.")
        return False
