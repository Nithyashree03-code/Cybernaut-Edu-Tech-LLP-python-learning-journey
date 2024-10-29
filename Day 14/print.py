def print_length(value):
    try:
        length = len(value)
        print(f"The length of {value} (type: {type(value).__name__}) is: {length}")
    except TypeError:
        print(f"Cannot determine the length of {value} (type: {type(value).__name__})")
data_types = [
    "Hello, World!",        
    [1, 2, 3, 4, 5],        
    (1, 2, 3),              
    {1, 2, 3},              
    {'a': 1, 'b': 2},      
    42,                     
    3.14                    
]
for item in data_types:
    print_length(item)
