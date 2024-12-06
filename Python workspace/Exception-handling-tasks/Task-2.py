def my_fun():
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        my_fun()  #recursive call
    else:
        print(f"Your age is {age}.")

my_fun()