def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"The result of {num1} divided by {num2} is {result}."
    finally:
        print("code excecuted successfully")
output = divide_numbers(89, 0)
print(output)
