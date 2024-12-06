class Book:
    #__init__ constructor. Runs as soon as an object
    #is initialized
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    #function to get the book details
    def getInfo(self):
        print(f"{self.title} is written by {self.author} and costs {self.price}")

#object of Book class:
obj_b1 = Book('Malgudi days', 'R.K. Narayan', 'Rs 200')
obj_b1.getInfo()
