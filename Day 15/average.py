def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
def calculate_average(numbers):
    if not numbers:  
        return 0
    total_sum = calculate_sum(numbers)  
    average = total_sum / len(numbers)
    return average
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"The average of {numbers} is: {average}")  