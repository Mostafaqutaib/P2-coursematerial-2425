from abc import ABC, abstractmethod
import re
class Util:
    @abstractmethod
    def is_valid_book_id( book_id):
        if len(book_id) != 10:
            return False
        return re.fullmatch(r"BOOK[1-9][0-9]{5}", book_id)

class Book:
    def __init__(self, book_id, title, price):
        if not Util.is_valid_book_id(book_id):
            raise ValueError("Invalid Book ID provided")        
        self.__book_id = book_id
        self.title = title
        self.price = price 
    
    @property
    def book_id(self):
        return self.__book_id
    @book_id.setter
    def book_id(self, value):
        if not Util.is_valid_book_id(value):
            raise ValueError("Invalid Book ID provided")
        self.__book_id = value

    def __str__(self):
        return f'Book: {self.title}, Price: {self.price}, Book ID: {self.book_id}'

class Library:
    def __init__(self, name, max_books):
        self.name = name
        self.max_books = max_books
        self.__books = {}
    @property
    def total_books(self):
        return len(self.__books)
    @property
    def available_capacity(self):
        return self.max_books - self.total_books
    def add_book(self, Book):
        if self.total_books == self.max_books:
            raise RuntimeError("Sorry Library is full")
        return self.__books.append(Book)
    def remove_book(self, book_id):
        return self.__books.pop()
    