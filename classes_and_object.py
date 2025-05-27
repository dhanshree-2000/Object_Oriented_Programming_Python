class Book:
    # A class to represent a book
    # Attributes: title, author, year
    #__init__ is a constructor method that initializes the attributes of the class
    # It is called when an object of the class is created
    def __init__ (self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):  # String representation of the object
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

print(book1)
print(book2)
