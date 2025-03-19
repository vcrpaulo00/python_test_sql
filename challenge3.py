def nameAge():
    print("Hello, Welcome to the show!")

    num1 = input('Enter your first name: ')
    num2 = int(input('Enter your age: '))    

    print('Hey there, My name is', num1, "I'm", num2, "years old")
    print('Hello, {}! You have {} years old' .format(num1, num2))
    print(f"Hello, {num1}! You've {num2} years old")
    
    print (type(num1))
    print (type(num2))

nameAge ()


# how to identify the tipo of variable
"""
print (type(num1))
print (type(num2))
"""