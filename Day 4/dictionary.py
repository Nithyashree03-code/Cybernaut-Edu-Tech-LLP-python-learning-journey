keys = input("Enter values for the first list (keys) separated by commas: ").split(',')
values = input("Enter values for the second list (values) separated by commas: ").split(',')
keys = [key.strip() for key in keys]
values = [value.strip() for value in values]
if len(keys) != len(values):
    print("Error: The number of keys must match the number of values.")
else:
    dictionary = dict(zip(keys, values))
    print("The resulting dictionary is:", dictionary)
