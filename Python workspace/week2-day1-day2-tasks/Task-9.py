



#handling zero division error and input error
try:
    x = float(input("Enter a number: "))
    y= 10/x
except:
    print("Some error occured")
else:
    print(f"10/{x}: {y}")