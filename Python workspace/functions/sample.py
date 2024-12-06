def myFun():
    num1 = 30
    num2 = 40
    Sum = num1+num2
    print("Sum of", num1, "and", num2,  "is:", Sum)

myFun()
myFun()

#Function with parameters
def myFun2(item, price):
    print("The cost of", item, "is:", price)

myFun2("Laptop", 50000)

#unknown number of arguments.    *args
def myFun3(*items):
    print("Second item is:", items[1])
myFun3("Laptop", "Keyboard", "Table", "Mouse")

#keyword arguments. key=value  . kwargs
def myFun4(item1, item2, item3):
    print("Third item is: ", item3)
myFun4(item2= "Mouse" ,item3 ="Keyboard", item1="Laptop")

#return statement:
def addition(num1, num2):
    Sum = num1+num2
    return Sum
addedValue = addition(40,76)
print(addedValue)

#implicit type conversion
int_num = 123
float_num = 23.67
new_num = int_num+float_num
print(new_num)
print(type(new_num))

#explicit type conversion
int_num = 123
str_val = "23"
new_num = int_num+ int(str_val)
print(new_num)
print(type(new_num))


#output formatting
x = 10
y = 20

print("The value of x is {} and y is {}".format(x,y))

#operators in python:
#arithmetic and comparison operators
a = 10
a = a+10
b=5
print(a)
print(a+b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)

#logical operators:
flag1 = True
flag2 = False
flag3 = True
print(flag1 and flag2)
print(flag1 and flag3)
print(flag1 or flag2)
print(flag1 or flag3)
print(not flag1)