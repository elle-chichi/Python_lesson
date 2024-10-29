# library management system

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def display_info(self):
        return f"Title{self.title}, {self.author}, {self.year}"

# child class/derived class
class LibraryBook(Book):
    def __init__(self, title, author, year, isbn, copies_available):
        super().__init__(title, author, year)
        self.isbn = isbn
        self.copies_available = copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return f"{self.title} borrowed. Copies left: {self.copies_available}"
        else:
            return f"No of Title {self.title} available"
    def return_book(self):
        self.copies_available += 1
        return f"{self.title} returned. Copies left: {self.copies_available}"

# usage example
book1=LibraryBook("Blossoms", "Trish Babes", "2020", isbn=45988752265545, copies_available=18)
print(book1.display_info())
print(book1.borrow_book())
print(book1.return_book())