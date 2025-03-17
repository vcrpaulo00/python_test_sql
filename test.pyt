def calculator():
    print("Hello, Welcome to the Python Calculator!")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "undefined (cannot divide by zero)"
    
    print("\nResults:")
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Division: {division}")

calculator()
