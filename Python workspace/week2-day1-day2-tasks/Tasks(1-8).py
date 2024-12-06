#Task 1

# a = 10    #integer
# print(a)

# b= "Hello"   #string
# print(b)
# b = "World"  #changing the value
# print(b)
# b = 32     #changing the value of string to int
# print(b)

# c = 12.89    #float
# print(c)
# c = 13.42  #changing the value
# print(c)

# d = True    
# print(d)

#Yes changing the value of a variable which has been assigned a string
#previously to int is allowed


#Task 2
# num1 = 10
# num2 = 20
# val1 = "Apple"
# val2 = "Mango"

# sum1 = num1+num2  # integer + integer
# print(sum1)
# diff1 = num1-num2 # integer - integer
# print(diff1)
# mul1 = num1*num2 # integer * integer
# print(mul1)
# div1 = num1/num2 # integer / integer
# print(div1)

# sum2 = val1+num1  # integer + string
# print(sum2)
# diff2 = num1-val1  # integer - string
# print(diff2)
# mul2 = num1*val1  # integer * string
# print(mul2)
# div2 = num1/val1  # integer / string
# print(div2)

# sum3 = val1+val2  # string + string
# print(sum3)
# diff3 = val1-val2  # string - string
# print(diff3)
# mul3 = val1*val2  # string * string
# print(mul3)
# div3 = val1/val2  # string / string
# print(diff3)



#Task-3

# num = (input("Enter a number: "))

# if(num>0):
#     print("Number entered is positive")
# elif(num<0):
#     print("Number entered is negative")
# else:
#     print("Number entered is zero")


#Task4

# marks = int(input("Enter marks: "))

# if(marks>100 or marks<0):
#     print("Invalid score")
# else:
#     if(marks >90):
#         print("Grade: A")
#     elif(marks >80):
#         print("Grade: A-")
#     elif(marks >70):
#         print("Grade: B")
#     elif(marks >60):
#         print("Grade: B-")
#     elif(marks >50):
#         print("Grade: C")
#     elif(marks >40):
#         print("Grade: C-")
#     elif(marks >30):
#         print("Grade: D")
#     else:
#         print("Grade: Fail")

#Task 5

# x = 1
# while(x<=10):   #specify the condition when to stop while loop
#     if(x%2 == 0):  #condition for checking if x is even
#         print(x)
#     x+=1   #increment the value of x by 1


#Task 6

# devices = ["Laptop", "Monitor", "Keyboard", "Mouse"]
# # a list of devices

# for item in devices:  #looping over the list
#     print(item)

# for item in devices:
#     print(len(item))

# sample_dictionary = {    # python dictionary
#     "Name" : "Rahul",
#     "Age" : 23,
#     "City" : "Delhi",
#     "Salary" : 40000
# }

# for item in sample_dictionary:   #looping over the dictionary
#     print(sample_dictionary[item])  #printing the value corresponding
#                                     # to each key


#Task 7

# for i in range(1,11): #to iterate from 1 to 10. 11 is excluded.
    
#     if(i == 7):  # if i is 7 then break the loop. This condition needs
#         break    # to be checked before 2nd one. Because 7 is also odd
#                 # if we continue at odd first then at 7 continue will
#                 # execute. and control will never reach to this condition


#     if(i%2!=0):  # if i is odd then continue
#         continue
    
#     print(i)  # else print


# Task 8

int_num = 10  #int value
float_num = 20.35  #float value

sum1 = int_num+float_num   #Here implicit type conversion occurs
print(sum1)

type_cast_int = int(float_num) #explicit type conversion
print(type_cast_int)
