import random

def game():
    # Step 1: Ask the user to select a door
    door = input("Choose a door (red or yellow): ").strip().lower()

    if door == "red":
        # Step 2: Red door logic
        number = int(input("Select a number from 1 to 5: "))
        
        if number in [1, 4]:
            # If the user chooses 1 or 4, ask for 3 numbers
            numbers = []
            for _ in range(3):
                num = int(input("Enter a number from 1 to 100: "))
                numbers.append(num)
            
            # Check the win condition later
            total = sum(numbers)
            if 130 < total < 1079:
                print("You win!")
            else:
                print("You lost.")
        else:
            print("You lost.")
    
    elif door == "yellow":
        # Step 3: Yellow door logic
        number = int(input("Enter a number from 6 to 10: "))
        
        if number % 2 == 0:  # Check if the number is even
            numbers = []
            for _ in range(3):
                num = int(input("Enter a number from 1 to 100: "))
                numbers.append(num)
            
            # Check the win condition
            total = sum(numbers)
            if 130 < total < 1079:
                print("You win!")
            else:
                print("You lost.")
        else:
            print("You lost.")
    else:
        print("Invalid door choice.")

# Start the game
game()
