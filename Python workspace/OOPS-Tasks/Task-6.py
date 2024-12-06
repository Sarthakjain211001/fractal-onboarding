class Book:
    is_borrowed = False

    def __init__(self, title, author):
        self.title = title
        self.author = author
    def borrow(self):
        self.is_borrowed = True
    def return_book(self):
        self.is_borrowed = False

class Library:
    books = []
    def add_book(self, book):
        self.books.append(book)
    
    def borrow_book(self, title):
        for i in range(0,len(self.books)):
            if self.books[i].title == title:
                if self.books[i].is_borrowed == False:
                    self.books[i].is_borrowed = True
                else:
                    print(f'{title} is already borrowed by someone.')
                return
        print(f'{title} is not in the library.')

    def return_book(self, title):
        for i in range(0,len(self.books)):
            if self.books[i].title == title:
                if self.books[i].is_borrowed == True:
                    self.books[i].is_borrowed = False
                else:
                    print(f'{title} was not borrowed.')
                return        
        print(f'{title} is not of this library.')
    
    def display_library(self):
        print('-----------------------------')
        print("Title ,isBorrowed")
        for i in range(0, len(self.books)):
            print(f'{self.books[i].title},{self.books[i].is_borrowed}')
        print('----------------------------')
bookB1 = Book("title1", "auth1")
bookB2 = Book("title2", "auth2")
bookB3 = Book("title3", "auth3")
bookB4 = Book("title4", "auth4")
bookB5 = Book("title5", "auth5")
bookB6 = Book("title6", "auth6")
bookB7 = Book("title7", "auth7")
bookB8 = Book("title8", "auth8")

LibL1 = Library()
LibL1.add_book(bookB1)
LibL1.add_book(bookB2)
LibL1.add_book(bookB3)
LibL1.add_book(bookB4)
LibL1.add_book(bookB5)
LibL1.add_book(bookB6)
LibL1.add_book(bookB7)
LibL1.add_book(bookB8)
LibL1.display_library()

LibL1.borrow_book("title1")
LibL1.borrow_book("title2")
LibL1.borrow_book("title3")
LibL1.display_library()
LibL1.borrow_book("title1")
LibL1.return_book("title1")
LibL1.display_library()
LibL1.borrow_book("title1")
LibL1.display_library()
LibL1.borrow_book("title1")
LibL1.return_book("title1")
LibL1.return_book("title2")
LibL1.return_book("title4")
LibL1.return_book("title3")
LibL1.display_library()

