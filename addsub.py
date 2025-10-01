# program-4
# calc.py
# Program for addition and subtraction of two numbers

# Taking input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Addition
print("\nAddition:", num1 + num2)

# Subtraction
print("Subtraction:", num1 - num2)

# Multiplication
print("Multiplication:", num1 * num2)

# Division (with check to avoid division by zero)
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Not possible (divisor is 0)")
