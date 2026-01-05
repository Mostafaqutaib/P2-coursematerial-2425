# Exam Question: Library Management System

* Place all code for this exercise in `library.py`.
* In these instructions, we always omit mentioning `self`.
  It is up to you to know when to add this extra parameter.
* Make sure you get the names exactly right, including the parameter names.

## Util

* Define a class `Util`.
* Define a static method `is_valid_book_id(book_id)` that returns `True` if the `book_id` is valid, otherwise `False`. Check this using a regular expression.
  * A `book_id` consists of exactly 10 characters.
  * A `book_id` always starts with BOOK.
  * This is followed by a 5-digit number between 10000 and 99999.
  * Examples: "BOOK12345" and "BOOK67890" are valid `book_id`s, but "BOOK01234" and "BOOK56789X" are not.

## Book

* Define a class `Book`.
* Define the constructor of `Book`.
  * The constructor takes three parameters: `book_id` (a string), `title` (a string), and `price` (a float).
  * When an instance of `Book` is created with an invalid `book_id`, a `ValueError` should be raised.
* Store `title` and `price` in public fields.
* Store `book_id` in a private field and make it accessible via a property.
  * Define a getter and a setter for `book_id`.
* Add the `dunder method` to provide a readable string representation of the `Book` object.
  * When this function is called, it should produce the following output:
    `Book: "title", Price: "price", Book ID: "book_id"`
  * Example:
    `"Book: Introduction to Python, Price: 45.99, Book ID: BOOK12345"`

## Library

A `Library` represents a collection of books. There are different types of libraries, but all libraries share some common features. Therefore, we will define an abstract class `Library` to store the common features of different types of libraries.

* Define an abstract class `Library`.
* Define a constructor for `Library`.
  * It has two parameters: `name` (a string), `max_books` (an int).
  * Store these in *public* fields.
  * Add a *private* field `books` to store a dictionary of all the books in the library.
    * The keys of this dictionary are the `book_id`s.
    * The values of this dictionary are the `Book` objects.
  * When created, a `Library` has no books.
* Define a read-only property `total_books` that returns the number of books in the library.
* Define a read-only property `available_capacity` that returns the remaining capacity for books in the library.
  * The remaining capacity is obtained by subtracting `total_books` from `max_books`.
* Define a method `add_book(book)` to add a `Book` to the `books` dictionary.
  * When the number of books exceeds the available capacity, this method raises a `Error`.
* Define a method `remove_book(book_id)` to remove a `Book` from the `books` dictionary.
  * When the book to be removed is not in the dictionary, this method raises a `Error`.
* Define a property `book_prices` that returns a list of prices (floats) of all the books in the library.
  * Use List Comprehension for this.
* Define a method `sort_books_by_price` that returns a list of books sorted by price (high to low) using a lambda function.
* Define an abstract method `create_library_summary()`.

## Types of Libraries

As previously mentioned, there are different types of libraries: Public, University, Research, etc. Common functionality has already been implemented in `Library`. Below, we will define two such subclasses to distinguish between types of libraries. To prevent this exam from becoming too long, we will only implement `PublicLibrary` and `UniversityLibrary`.

### `PublicLibrary`

A `PublicLibrary` inherits from `Library`.

* Define a constructor for `PublicLibrary`.
  * It has three parameters, two inherited from the constructor of `Library` and a paramter `members`.
  * `members` is a public field (a list of strings representing member names).
* Define a method add_member(member) to add a member to the `members` list.
* Implement `create_library_summary`
  * This function returns a string representing the library summary.
  * The string is composed of:
    * The name of the PublicLibrary
    * The members of the library
    * The books in the library (one line per book), sorted on the price of the book (high to low)
      * Each line is constructed with the `book_id` followed by the price of the book and the title.
    * See example usage below.

### `UniversityLibrary`

A `UniversityLibrary` inherits from `Library`.

* Define a constructor for `UniversityLibrary`.
  * It has one parameter: `name`, inherited from the constructor of `Library`.
  * The `max_books` of a `UniversityLibrary` is always equal to 1000.
* Implement `create_library_summary`
  * This function returns a string representing the library summary.
  * The string is composed of:
    * The name of the UniversityLibrary
    * The books in the library (one line per book), sorted on the price of the book (high to low)
      * Each line is constructed with the `book_id` followed by the price of the book and the title.
    * See example usage below
* Implement the method `add_book(book)`:
  * Due to the nature of a UniversityLibrary, only books with a price less than or equal to 100.00 can be added.
  * If a book with a higher price is added, this method raises a `RunTimeError`.

## Example Usage

```python
# Create some books
>>> python_book = Book("BOOK12345", "Introduction to Python", 45.99)
>>> java_book = Book("BOOK67890", "Java Essentials", 39.99)
>>> data_science_book = Book("BOOK23456", "Data Science Basics", 189.99)
>>> expensive_book = Book("BOOK3", "Advanced Algorithms", 120.00)
ValueError: Invalid Book ID provided

# Print Python Book
>>> print(python_book)
Book: Introduction to Python, Price: 45.99, Book ID: BOOK12345

# Create a public library
>>> city_library = PublicLibrary("City Library", 200, ["Alice", "Bob", "Charlie"])

# Adding books to our library
>>> city_library.add_book(python_book)
>>> city_library.add_book(java_book)

# Print book prices
>>> print(city_library.book_prices)
[45.99, 39.99]

# Print Library Summary
>>> print(city_library.create_library_summary())
Library: City Library
Members: Alice, Bob, Charlie
BOOK12345 - 45.99 (Introduction to Python)
BOOK67890 - 39.99 (Java Essentials)

# Create a university library
>>> university_library = UniversityLibrary("Tech University")

# Adding books to the university library
>>> university_library.add_book(data_science_book)
RuntimeError: Books priced above 100.00 cannot be added to a UniversityLibrary

```

# Testing
Write tests to thoroughly check the `create_library_summary` method and ensure it works as intended. Include these tests in the `test-library.py` file.
Follow the conventions from the Testing chapter.