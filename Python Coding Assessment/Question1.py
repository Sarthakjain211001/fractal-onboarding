#function to calculate the area
def area_fun(length, width):
    return length*width
#function for perimeter
def perimeter_fun(length, width):
    return 2*(length+width)

#custom exception for handling negative values
class NegativeValueException(Exception):
    pass

try:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    #raise custom exception when either of length or width is negative
    if length<0 or width<0:
        raise NegativeValueException
    else:
        print(f'Area: {area_fun(length, width)}')
        print(f'Perimeter: {perimeter_fun(length, width)}')
#exception if user entered character values
except ValueError:
    print("Invalid input: Length and width must be numeric values.")
#This will run when custom exception will be raised
except NegativeValueException:
    print("Invalid input: Length and width must be positive numbers.")
