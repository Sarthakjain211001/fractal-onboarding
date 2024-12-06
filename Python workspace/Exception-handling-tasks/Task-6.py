class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if(age<0 or age>120):
        raise InvalidAgeError
except InvalidAgeError:
    print('Error: Invalid age entered. Age must be between 0 and 120')
except ValueError:
    print("Enter a valid number")
else:
    print("Your age is: ",age)