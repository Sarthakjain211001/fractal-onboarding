name = "lenovo"
price = 2000
print(name, price)
print(type(price))

status = True
print(status)
print(type(status))

ch = 'A'
print(ch)
print(type(ch))   #string. Python does not have char data type. char is treated as string in python. 


x, y, z = "Orange", "Apple", 800  #assign multiple values to multiple variables in one line
print(x,y,z)

x = y=z = "Banana"   # assign same value to multiple variables
print(x,y,z)

fruits = ["Apple", "Banana", "Mango"]
x,y,z = fruits
print(x,y,z)
