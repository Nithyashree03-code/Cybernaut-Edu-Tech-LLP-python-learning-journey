import random
def assign_random_value(name):
    random_value = random.randint(1, 50)
    print(f"The value assigned to {name} is {random_value}")
user_name = input("Please enter a name: ")
assign_random_value(user_name)
