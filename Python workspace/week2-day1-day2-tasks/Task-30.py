try:
    number = int(input("Enter a number: "))
    res = 50/number
    print(res)
except ValueError:
    print("Value error occured")
except ZeroDivisionError:
    print("zero division error occured")