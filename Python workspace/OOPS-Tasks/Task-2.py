#Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print("The animal is eating.")

#child class dog inheriting the parent class Animal
#all the attributes and methods present in animal
#class will also come in the child class
class Dog(Animal):
    def bark(self):
        print("woof!")

#child class cat
class Cat(Animal):
    def meow(self):
        print("Meow!")

#objects of dog and cat class
dogD1 = Dog("Max", 3)
catC1 = Cat("Tom", 2)

dogD1.eat()  #calling the method from parent class
dogD1.bark() #dog class method
catC1.eat()  #parent class method
catC1.meow() #cat class method