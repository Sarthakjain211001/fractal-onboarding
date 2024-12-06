class Shape:

    def getInfo(self):
        print("I am a shape")
    def calculate_area(self):
        print('This method calcuates area')

class Circle(Shape):
    #overriding the calculate_area method
    def calcuate_area(self):
        print("This will calculate the area of circle")

circle_c1 = Circle() 
circle_c1.getInfo()   #This will execute the getInfo() from
                      #Shape class.     
circle_c1.calcuate_area() #calculate_area defined in circle
                          #class will execute