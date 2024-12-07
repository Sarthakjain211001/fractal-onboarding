#class Book containing title, author and copies available
class Book:
    #constructor function for initializing the object
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

#some custom exceptions to handle the edge cases
class limitException(Exception):
    pass
class InvalidBook(Exception):
    pass
class InvalidMember(Exception):
    pass
class BookAlreadyBorrowed(Exception):
    pass

#Member class
class Member:
    def __init__(self, name, max_allowed_books=3):
        self.name = name
        self.borrowed_books=[] #list of borrowed books
        self.max_allowed_books=max_allowed_books
    #function to borrow a book
    def borrow_book(self, bookTitle, libraryObj):
        try:
            #Edge case 1: If member has already borrowed this book
            if bookTitle in self.borrowed_books:
                raise BookAlreadyBorrowed
            #Edge case 2: Member trying to borrow more books than allowed
            elif len(self.borrowed_books) == self.max_allowed_books:
                raise limitException
            #Edge case 3: Book trying to be borrowed is not available in library
            #a.) either not in collection
            #b.) or all the copies have been borrowed
            elif bookTitle not in libraryObj.collection or libraryObj.collection[bookTitle].copies_available == 0:
                raise ValueError
            #Successful borrow:
            else:
                #reduce it's copy from collection
                libraryObj.collection[bookTitle].copies_available -= 1
                #and add the book to the member's borrowed books list
                self.borrowed_books.append(bookTitle)
        #exceptions for edge cases:
        except BookAlreadyBorrowed:
            print(f'BookAlreadyBorrowed: {bookTitle} is already borrowed by {self.name}')
        except limitException:
            print(f'Limit reached: {self.name} has already borrowed the maximum allowed.')
        except ValueError:
            print(f'ValueError: {bookTitle} not available in this library')
    #function for returning a book
    def return_book(self, bookTitle, libraryObj):
        try:
            #Edge case 1: The book came for return is not of this library
            if bookTitle not in libraryObj.collection:
                raise InvalidBook
            #Edge case 2: The book came for return was not borrowed by
            #the member who is returning this book
            elif bookTitle not in self.borrowed_books:
                raise InvalidMember
            #successful return
            else:
                #increase the copy in collection and remove this book
                #from member's borrowed books list
                libraryObj.collection[bookTitle].copies_available += 1
                self.borrowed_books.remove(bookTitle)
        except InvalidBook:
            print(f'Invalid Book: {bookTitle} does not belongs to this library')
        except InvalidMember:
            print(f'Invalid Member: {bookTitle} was not borrowed by {self.name}')

#library class
class Library:
    def __init__(self):
        #initialize the collection by empty dixtionary
        self.collection={}
    #add a book to the library
    def add_book(self, title, author, copies_available):
        #create an object of book class and add the object to collection dict
        bookObj = Book(title, author, copies_available)
        self.collection[title] = bookObj

#creaing a library object
libraryL1 = Library()

#add some books to the library
libraryL1.add_book("Python Basics", "John Doe", 2)
libraryL1.add_book("Advanced Python", "Jane Smith", 1)
libraryL1.add_book("Introduction to C++", "Marcus", 5)
libraryL1.add_book("Indian History", "Vivek P.", 2)
#create 2 members
memberM1 = Member("Alice")
memberM2 = Member("Bob")

#member 1 borrowed some books
memberM1.borrow_book("Python Basics", libraryL1)
memberM1.borrow_book("Advanced Python", libraryL1)
memberM1.borrow_book("Introduction to C++", libraryL1)

#member 1 trying to borrow a book which he already borrowed
memberM1.borrow_book("Introduction to C++", libraryL1)

#member 1 trying to borrow more than his limit
memberM1.borrow_book("Indian History", libraryL1)

#display books borrowed by member 1
print(f'Books borrowed by {memberM1.name} = {memberM1.borrowed_books}')


memberM2.borrow_book("Introduction to C++", libraryL1)

#member 2 trying to borrow a not availabe book
memberM2.borrow_book("Advanced Python", libraryL1)
print(f'Books borrowed by {memberM2.name} = {memberM2.borrowed_books}')

#member 1 returing a book
memberM1.return_book("Advanced Python", libraryL1)
#member 2 borrowing a book returned by member 1
memberM2.borrow_book("Advanced Python", libraryL1)

print(f'Books borrowed by {memberM1.name} = {memberM1.borrowed_books}')

print(f'Books borrowed by {memberM2.name} = {memberM2.borrowed_books}')

#member 2 trying to return a book which he never borrowed
memberM2.return_book("Python Basics", libraryL1)
#member 2 trying to return a book which does not belongs to this library
memberM2.return_book("English communication", libraryL1)
#member 2 trying to borrow a book which is not of this library
memberM2.borrow_book("English communication", libraryL1)
 
