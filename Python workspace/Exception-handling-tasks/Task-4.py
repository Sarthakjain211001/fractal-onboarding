try:
    num = float(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")
except OverflowError:
    print("Error: Very large number. Please enter a small value.")
else:
    print(f"The result of 100 divided by {num} is {result}.")