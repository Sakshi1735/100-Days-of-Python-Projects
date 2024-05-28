#Write a library class with no_of_books and books as two instance variables. 

''' 
Write a program to create a library from this library class and show how you can print all books, add book and get the number
of books using different methods. Show that your program doesnt persist thye books after the program is stopped!
'''

class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def addBooks(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"The number of books available in the library are {self.no_of_books}")
        print(f"The list of books are {self.books}")



l1 = Library()
a=int(input("Enter the number of books you want to add to the library: \t"))
for i in range (0,a):
    b_name = input("Enter the name of the book: \t")
    l1.addBooks({b_name})

l1.showInfo()
