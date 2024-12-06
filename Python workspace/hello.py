# print("Hello world!!")  #first program
# print(10+20)

# name = "Alex"
# print(name)

# print(30/10)

#tuples:

# sample_tuple = (10,20,30)
# print(sample_tuple)

# print(sample_tuple[1])

# # sample_tuple[1]=300
# # print(sample_tuple[1])

# for item in sample_tuple:
#     print(item)

# if 30 in sample_tuple:
#     print("Yes, 30 is present")


#string
# txt = "Hello"
# print(txt)
# # txt[0] = 'W'
# # print(txt)

# msg = '''hello, this
# is a multiline 
# string'''

# print(msg)

#Sets

# student_id1 = {101, 102, 103, 104, 101}
# student_id2 = {101, 107, 108, 102, 101}
# student_id3 = student_id1.intersection(student_id2)
# student_id3_ = student_id1 & student_id2
# student_id4 = student_id1.union(student_id2)
# print(student_id1)
# print(student_id2)
# print(student_id3)
# print(student_id3_)
# print(student_id4)
# print(student_id1.difference(student_id2))

#dictionary

# car= {
#     "model" : "mustang",
#     "brand" : "ford",
#     "seats" : 2,
#     "colors" :["red", "yellow", "white"]
# }

# print(car)
# print(car["brand"])

# car["year"] = 2005

# print(car)

# x  =car.keys()
# print(list(car.values()))

# for x in car.values():
#     print(x)

#switch case replacement in python
# def numbers_to_string(num):
#     swithcer = {
#         0 : "zero",
#         1 : "one",
#         2 : "two"
#     }

#     return swithcer.get(num, "nothing")

# print(numbers_to_string(4))

#classes and objects in python: 
# class Bike:
#     name = ""
#     gears = 0

# bikeObj = Bike()
# bikeObj.name = "Honda"
# bikeObj.gears = 4

# print(f"{bikeObj.name} has {bikeObj.gears} gears")



















# class Person:
#     name = ""
#     age = 0
#     city = ""
#     devices = []

# RamPerson = Person()
# RamPerson.name = "Ram Sharma"
# RamPerson.age = 25
# RamPerson.city = "Indore"
# RamPerson.devices = ["Laptop", "Mobile", "Monitor"]

# print(f"{RamPerson.name} lives in {RamPerson.city}. He is {RamPerson.age} years old and has {RamPerson.devices}")


# class Room:
#     length : 0.0
#     breadth : 0.0

#     def calculate_area(self):
#         print(f"Area of the room is: {self.length*self.breadth}")

# studyRoom = Room()
# studyRoom.length = 20.50
# studyRoom.breadth = 15.34

# studyRoom.calculate_area()

# class Person:
#     name = ""
#     age = 0

#     def __init__(self ,name="", age=0):
#         self.name = name
#         self.age = age

# PersonP1 = Person("Ram", 25)
# print(PersonP1.name, " ", PersonP1.age)


# class Person:

#     def __init__(self, emp_name, emp_id):
#         self.emp_name = emp_name
#         self.emp_id = emp_id
    
#     def getPerson(self):
#         print(f"name: {self.emp_name}, id: {self.emp_id}")

# personP1 = Person("Rahul", 1001)
# personP1.getPerson()

# class Employee(Person):
#     def __init__(self, emp_name, emp_id, emp_salary, emp_designation):
    
#         self.emp_salary = emp_salary
#         self.emp_designation = emp_designation

#         Person.__init__(self, emp_name, emp_id)

#     def getEmployee(self):
#         print("Employee name: ", self.emp_name)
#         print(f"Employee id: {self.emp_id}")
#         print(f"Employee salary: {self.emp_salary}")
#         print(f"Employee designation: {self.emp_designation}")

# Emp_e1 = Employee("Alex", 101, 23000, "HR")
# Emp_e1.getEmployee()

#Poly morphism

# class Bird:
#     def intro(self):
#         print('There are many types of birds')
#     def flight(self):
#         print('Most of the birds can fly but some cannot')

# class Sparrow(Bird):
#     def flight(self):
#         print('Sparrow can fly')

# class Ostrich(Bird):
#     def flight(self):
#         print('Ostrich can\'t fly')

# bird_obj = Bird()
# bird_obj.intro()
# bird_obj.flight()

# sparrow_obj = Sparrow()
# sparrow_obj.intro()
# sparrow_obj.flight()

# Ostrich_obj = Ostrich()
# Ostrich_obj.intro()
# Ostrich_obj.flight()

# class cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age  = age        
#     def intro(self):
#         print(f'Hi, I am a cat. My name is {self.name}. And age is {self.age}.')
#     def speak(self):
#         print('Meow')

# class dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age  = age        
#     def intro(self):
#         print(f'Hi, I am a dog. My name is {self.name}. And age is {self.age}.')
#     def speak(self):
#         print('Bark')

# cat_obj = cat("fluffy", 3)
# dog_obj = dog("Max",2)

# # cat_obj.intro()
# # cat_obj.speak()
# # dog_obj.intro()
# # dog_obj.speak()

# for animal in (cat_obj, dog_obj):
#     animal.intro()
#     animal.speak()

#multiple Inheritance: 

# class mammal:
#     def intro(self):
#         print('mammals can give direct birth.')

# class wingedAnimal:
#     def intro(self):
#         print('winged animal can fly.')

# class bat(mammal, wingedAnimal):
#     pass

# bat_obj = bat()
# bat_obj.intro()

#multilevel inheritance:
# class superClass:
#     def super_intro(self):
#         print("I am super class")

# class parentClass:
#     def parent_intro(self):
#         print("I am parent class")

# class childClass:
#     def child_intro(self):
#         print("I am child class")

# superObj = superClass()
# parentObj = parentClass()
# childObj = childClass()

# superObj.super_intro()
# parentObj.parent_intro()
# childObj.child_intro()


#Abstraction and encapsulation

# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width

#     def calculate_perimeter(self):
#         return 2*(self.__length+self.__width)
#     def calculate_area(self):
#         return self.__length*self.__width

# rect_Obj = Rectangle(3,4)
# # print(rect_Obj.__length)
# print("Area: ",rect_Obj.calculate_area())
# print("Perimeter: ", rect_Obj.calculate_perimeter())



# import os
# print(os.getcwd())
# os.mkdir('demo')
# os.chdir('demo')
# print(os.getcwd())

# newFile = open('newFiledemo.txt','w')
# newFile.write("This is a new file")
# newFile.write("Learning file handling")
# newFile.close()

# file = open("demo/newFiledemo.txt", 'r')
# print(file.read())

# print('-----------------------------------')

# with open("demo/newFiledemo.txt", "r") as file:
#     data = file.readlines()
#     # for line in data:
#     #     print(line)
#     #     print('----')
    
#     for line in data:
#         word = line.split()
#         print(word)
#     print(data)

# import csv
# with open('demo/employee.csv','r') as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# import csv
# with open('demo/employee.csv','a',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([1004,'Alex', 'Bangalore', 20000])
#     writer.writerow([1005, 'Alan', "hyderabad", 15000])


#exception handling:
# print(10)
# print(20)

# try:
#     res = 50/0
#     print(res)
# except:
#     print("Some error occured")

# print(30)
# print(40)
# print(50)


# def fun(a):
#     if (a<4):
#         b = a/(a-3)
#     print("Value of b is: ",b)

# try:
#     # fun(4)
#     # fun(3)
#     fun("hello")

# except ZeroDivisionError:
#     print("zero division error occured")
# except NameError:
#     print("Name error occured")
# except TypeError:
#     print("Tyoe error occured")

# try:
#     raise NameError("hi")
# except NameError:
#     print("A name error occured")
#     raise

# try:
#     ls = [1,2,3,4,5]
#     print(ls[10])
# except IndexError:
#     print("Index out of bound")

# try:
#     num = int(input("Enter a number: "))
#     assert num%2 == 0
# except:
#     print('Not an even number!')

# else:
#     reciprocal = 1/num
#     print(reciprocal)

# class InvalidAgeException(Exception):
#     pass

# number = 18
# try:
#     input_num= int(input("Enter a number: "))
#     if input_num<number:
#         raise InvalidAgeException("Invalid Age")
#     else:
#         print("Eligible to vote")

# except InvalidAgeException:
#     print("Exception occured: Invalid Age")

#exception handling in file handling
import os

#creating a file
# def create_file(filename):
#     try:
#         with open(filename, 'w') as f:
#             f.write('Hello World!!! \n')
#         print('file ', filename,' created successfully!')
#     except IOError:
#         print("Error: Could not read file " + filename)
# #reading a file
# def read_file(filename):
#     try:
#         with open(filename,'r') as f:
#             contents = f.read()
#             print(contents)
#     except IOError:
#         print("Error: Could not read file ",filename)
# #appending to a file
# def append_file(filename, text):
#     try:
#         with open(filename,'a') as f:
#             f.write(text)
#         print("Text appended successfully in ", filename)
#     except IOError:
#         print("Error: Could not append text in file ", filename)
# #renaming a file
# def rename_file(filename, newFilename):
#     try:
#         os.rename(filename, newFilename)
#         print('rename successful')
#     except IOError:
#         print("rename failed")
# #deleting a file
# def delete_file(filename):
#     try:
#         os.remove(filename)
#         print(filename, " deleted successfully")
#     except IOError:
#         print("Error:delete failed ", filename)



# if __name__ == '__main__' :
#     filename = 'data.txt'
#     newFilename = 'new-data.txt'
#     text = 'New text appended.'

#     create_file(filename)
#     read_file(filename)
#     append_file(filename,text)
#     read_file(filename)
#     rename_file(filename,newFilename)
#     read_file(newFilename)
#     delete_file(newFilename)


#list comprehension
# numbers = [1,2,3,4]
# sq_numbers = [num*num for num in numbers]
# print(sq_numbers)

# lambda function
# greet = lambda : print("Welcome!!!")
# greet()

# greet_user = lambda user: print('Welcome, ',user)
# greet_user('Alex')

# my_list = [2,4, 21, 10, 32]
# new_list = list(map(lambda x : x*x, my_list))
# print(new_list)

# new_list2 = list(filter(lambda x: x%2==0, my_list))
# print(new_list2)

# myList = [1,2,3,4,5]
# iterator = iter(myList)

# for element in iterator:
#     print(element)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# class PowTwo:
#     def __init__(self, max = 0):
#         self.max=max
#     def __iter__(self):
#         self.n=0
#         return self
#     def __next__(self):
#         if self.n <= self.max:
#             result = 2**self.n
#             self.n+=1
#             return result
#         else:
#             raise StopIteration

# for i in PowTwo(3):
#     print(i)

# def my_generator(n):
#     value = 0
#     while value<n:
#         yield value
#         value+=1
# for value in my_generator(3):
#     print(value)

# gen = my_generator(3)
# print(next(gen))
# print(next(gen))
# print(next(gen))


# globl_var = 10

# def outer_function():
#     outer_var = 20

#     def inner_function():
#         inner_var = 30

#         print(inner_var)
    
#     print(outer_var)
#     inner_function()

# print(globl_var)
# outer_function()
# print(outer_var)

# def greet():
#     name = "john"
#     return lambda : "hi, "+ name

# print(greet()())

# def calculate():
#     num = 1
#     def inner_func():
#         global num
#         num+=2
#         return num
#     return inner_func
# odd = calculate()
# print(odd())
# print(odd())
# print(odd())


# def add(x,y):
#     return x+y
# def calculate(func,x,y):
#     return func(x,y)
# result = calculate(add, 4,3)
# print(result) 

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# def i_m_preety(func):
#     def inner():
#         print("Second fun")
#         func()
#     return inner

# @make_pretty
# @i_m_preety
# def ordinary():
#     print("I am ordinary")

# decorated_func = make_pretty(ordinary)
# decorated_func()

# ordinary()

# def smart_divide(func):
#     def inner(a,b):
#         print("I am dividing ", a ,"and",b)
#         if(b == 0):
#             print("cannot divide")
#             return
#         return func(a,b)
#     return inner

# @smart_divide
# def divide(a,b):
#     print(a/b)

# divide(2,5)
# divide(2,0)

#Python regular expression (regEx)
# import re
# pattern = '^a...s$'
# test_string = 'abyewss'

# result = re.match(pattern, test_string)
# if result:
#     print('search successful')
# else:
#     print('search unsuccessful')

# import re
# string = 'Twelve:12 Eighty nine:89.'
# pattern = '\d+'
# result = re.findall(pattern, string)
# res2 = re.split(pattern, string)
# print(result)
# print(res2)

# import re
# pattern = 'Python'
# string = 'Python is fun.'
# res = re.findall(pattern, string)
# print(res)

import datetime
current_date = datetime.date.today()
print(current_date)
from datetime import datetime
now = datetime.now()
print(now)