
# Exam Question 1: Events

* Place all code for this exercise in `event.py`.
* In these instructions, we always omit mentioning `self`. It is up to you to know when to add this extra parameter.
* Ensure you have the names exactly right, including parameter names.
* You have received a file `basic_tests.py` containing basic tests, such as whether certain classes exist and whether you have used the correct names.
  * Run these tests with the command:

    ```bash
    $ pytest basic_tests.py
    ```

  * A missing class will cause tests targeting that class to be skipped. Skipped tests still count as failed.
  * The tests only perform high-level checks. Failing/skipped tests mean your code is certainly incomplete or incorrect. But passing tests do not mean your code is entirely correct!
* You must also create some tests yourself in the file `test-event.py`.
  * All tests you need to write yourself are indicated in this assignment file.
  * You can add additional tests here if you want to check your code more thoroughly. Only the tests requested in the assignment will be assessed.
  * This test file must be able to run correctly to earn points.

## Util

* Define a class `Util`.
* Define a static method `is_valid_sabam_id(sabam_id)` that returns `True` if the sabam_id is valid and otherwise `False`. Check this using a regular expression.
  * A sabam_id consists of exactly 12 characters
  * A sabam_id always starts with SB
  * This is followed by 6 random digits
  * Finally, 4 uppercase vowels follow
  * Examples: "SB123456AEIO" and "SB112233AAEE" are valid sabam_ids, but "SB12345AAAA" and "SB123456AZER" are not.

## Artist

* Define a class `Artist`.
* Define the constructor of `Artist`.
  * The constructor takes three parameters: `sabam_id` (a string), `name` (a string), and `wage` (an integer)
  * Raises a `ValueError` if an invalid sabam_id is provided.
* Store name and wage in public fields.
* Store sabam_id in a private field and make it accessible via a property.
  * Define a getter and a setter for sabam_id.
* Add the `dunder method` to provide a readable string representation of the artist object.
  * When this function is called, the following output should be generated: `Artist: "artist_name", Wage: "artist_wage", Sabam ID: "artist_sabam_id"`.
  * Example: "Artist: Rihanna, Wage: 20000, Sabam ID: SB123456AAAA"

## Event

An `Event` represents an event where artists perform on different stages and during different time slots. There are various types of events, but all events share some common characteristics. Therefore, we will define an abstract class `Event` to store common features of different types of events.

* Define an abstract class `Event`.
* Define the constructor for `Event`.
  * It has three parameters: `name` (a string), `number_of_stages` (an int), and `number_of_slots` (an int).
  * Store these in *public* fields.
  * Add a *private* field `artists` to store a dictionary of all the artists performing at this event.
  * When created, an `Event` has no registered artists.
* Define a read-only property `number_of_artists` that returns the number of registered `artists` for this `Event`.
* Define a read-only property `maximum_artists` that returns the maximum number of registered `artists` for this `Event`.
  * The maximum number of registered artists is obtained by multiplying the number of stages by the number of time slots.
* Define a method `add_artist(artist)` to add an `Artist` to the artists dictionary.
  * When the maximum number of artists has already been reached, this method raises a `RunTimeError`.
* Define a method `remove_artist(artist)` to remove an `Artist` from the `artists` dictionary.
  * When the artist to be removed is not in the dictionary, this method raises a `RunTimeError`.
* Define a property `sum_wages_of_artists` that returns the sum of the wages of all the artists performing at this `Event`.
  * Use List Comprehension for this.
* Define a method `sort_artists_by_name` that returns a list of artists, sorted by name (low to high), using a lambda function.
* Define an abstract method `calculate_profit()`.

## Types of Events

As mentioned earlier, there are different types of events: Festival, Concert, FreeConcert, etc...
Common functionality is already implemented in `Event`. Below, we will define two such subclasses to distinguish between types of events. To prevent this exam from becoming too long, we will only implement `Festival` and `FreeConcert`.

### Festival

A `Festival` inherits from `Event`.

* Define a constructor for `Festival`.
  * It has three parameters: all three inherited from the constructor of `Event`.
  * Add another public field `number_of_attendees` (an int).
  * Add another public field `ticket_price` (an int).
* Implement `calculate_profit`
  * Calculate the profit of this Festival: revenue - costs
  * The revenue is calculated by multiplying the number of attendees by the ticket price
  * The costs are calculated by summing the wages of all present artists

### FreeConcert

A `FreeConcert` inherits from `Event`.

* Define a constructor for `FreeConcert`.
  * It has two parameters: `name` and `number_of_slots`, both inherited from the constructor of `Event`.
  * The number of stages for a FreeConcert is always equal to 1.
* Implement `calculate_profit`
  * Calculate the profit of this FreeConcert: revenue - costs
  * The revenue of a free concert is equal to 0
  * The costs are calculated by summing the wages of all present artists
* Implement the method `add_artist(artist)`:
  * Only artists with a wage under 10000 euros can perform at a FreeConcert
  * If an artist is added who demands more, this method generates a `RunTimeError`

## Example Usage

```python
# creating some artists
>>> rihanna = Artist("SB123456AAAA", "Rihanna", 20000)
>>> camille = Artist("SB123456BBBB", "Camille", 5000)
ValueError("Invalid Sabam ID provided")
>>> metallica = Artist("SB123456EEEE", "Metallica", 30000)
>>> pommelien = Artist("SB123456OOOO", "Pommelien Thijs", 5000)
>>> samson = Artist("SB123456IIII", "Samson en Gert", 8000)
>>> elton = Artist("SB123456UUUU", "Elton John", 22000)
>>> elvis = Artist("SB123455AAAA", "Elvis Presley", 50000)

# printing Rihanna
>>> print(rihanna)
Artist: Rihanna, Wage: 20000, Sabam ID: SB123456AAAA

# creating a Festival
>>> rock_werchter = Festival("Rock Werchter", 1, 2, 10000, 10)

# adding some artists to the festival
>>> rock_werchter.add_artist(metallica)
>>> rock_werchter.add_artist(rihanna)
>>> rock_werchter.add_artist(samson)
RuntimeError("Line-up Full. Cannot add artist")
>>> rock_werchter.remove_artist(rihanna)
>>> rock_werchter.add_artist(samson)
>>> rock_werchter.remove_artist(elvis)
RuntimeError("Artist was not in the line-up")

# Print Artist names sorted
>>> sorted_artists = rock_werchter.sort_artists_by_name()
>>> for artist in sorted_artists:
>>>     print(artist)
Artist: Rihanna, Wage: 20000, Sabam ID: SB123456AAAA
Artist: Metallica, Wage: 30000, Sabam ID: SB123456EEEE
Artist: Samson en Gert, Wage: 8000, Sabam ID: SB123456IIII

# calculating the profit of Rock Werchter
>>> print(rock_werchter.calculate_profit())
62000

# creating a FreeConcert
>>> rock_blanden = FreeConcert("Rock Blanden", 1)

# adding some artists to Rock Blanden
>>> rock_blanden.add_artist(elton)
RuntimeError("Artist too expensive to play on a free concert")
>>> rock_blanden.add_artist(pommelien)

# calculating the profit (loss) of Rock Blanden
>>> print(rock_blanden.calculate_profit())
-5000
```

# Testing
You must write tests that sufficiently test the `calculate_profit` property. Include these tests in the `test-event.py` file.

* Refer to the descriptions of both `Festival` and `FreeConcert` for information on how to implement `calculate_profit`.
* Use the conventions you learned in the chapter on Testing to test this functionality.
