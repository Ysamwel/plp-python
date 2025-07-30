# Basic Calculator
# Create a simple Python program that asks the user to input
# two numbers and a mathematical operation (addition, subtraction, multiplication, or division)
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15
# Ask the user to enter the desired operation: +, -, *, or /

# user to enters the first number (input is taken as string)
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Enter the desired operation: +, -, *, or /
operation = input("enter operation (+, -, *, /): ")

# Convert the string inputs to floating point numbers
num1 = float(num1)
num2 = float(num2)

# Initialize the variable 'result' to hold the calculation outcome
# Perform the operation based on the user's input
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Check if division is valid
    if num2 != 0:
      result = num1 / num2
    else:
        result = "Error"
else:
    #if operation is invalid
    result = "Invalid operation"

if isinstance(result, float) or isinstance(result, int):
    print(f"{num1} {operation} {num2} = {result}")
else:
    print(result)

    

