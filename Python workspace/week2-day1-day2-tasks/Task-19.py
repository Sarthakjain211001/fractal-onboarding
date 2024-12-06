#Base class Animal:
class Animal:
    def speak(self):
        print('Animals produce sounds')

#derived class dog:
class Dog(Animal):
    def bark(self):
        print("Hi, I am dog. I bark.")
    #overriding the speak method of parent animal
    #class.
    def speak(self):
        print("I speak by barking.")

#object of dog class:
dog_obj1 = Dog()
dog_obj1.speak()
dog_obj1.bark()

