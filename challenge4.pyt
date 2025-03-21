print("Hello, Welcome to the Paulo calculator!")

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: ')) 

sum = num1 + num2
product = num1 * num2
exponential = pow(num1, num2)

if num1 or num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

print("Results:")
print(f"Sum: {sum}")
print(f"Product: {product}")
print(f"Exponential: {exponential}")
print(f"Division: {division}")




