num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

try:
    num3 = num1/num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
else:
    print(f'The result is: {num3}')
# print(num1/num2)
