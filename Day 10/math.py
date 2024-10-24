import math
def calculate_square_root(number):
    return math.sqrt(number)
try:
    user_input = float(input("Enter a number to calculate its square root: ")) 
    if user_input < 0:
        print("Error: Cannot calculate the square root of a negative number.")
    else:
        result = calculate_square_root(user_input)
        print(f"The square root of {user_input} is {result}.")
except ValueError:
    print("Error: Please enter a valid number.")
