# Exam Question: Event Ticketing System

* Place all code for this exercise in `ticketing.py`.
* In these instructions, we always omit mentioning `self`.
  It is up to you to know when to add this extra parameter.
* Make sure you get the names exactly right, including the parameter names.

## Util

* Define a class `Util`.
* Define a static method `is_valid_ticket_id(ticket_id)` that returns `True` if the ticket_id is valid, otherwise `False`. Check this using a regular expression.
  * A ticket_id consists of exactly 10 characters.
  * A ticket_id always starts with TICK.
  * This is followed by a 4-digit number between 1000 and 9999.
  * Finally, there are 2 uppercase letters.
  * Examples: "TICK1234AB" and "TICK5678CD" are valid ticket_ids, but "TICK0123AB" and "TICK56789EF" are not.

## Ticket

* Define a class `Ticket`.
* Define the constructor of `Ticket`.
  * The constructor takes three parameters: `ticket_id` (a string), `event_name` (a string), and `price` (a float).
  * When an instance of `Ticket` is created with an invalid ticket_id, a `ValueError` should be raised.
* Store `event_name` and `price` in public fields.
* Store `ticket_id` in a private field and make it accessible via a property.
  * Define a getter and a setter for `ticket_id`.
* Add the `dunder method` to provide a readable string representation of the ticket object.
  * When this function is called, it should produce the following output: `Ticket: "event_name", Price: "price", Ticket ID: "ticket_id"`
  * Example:
    * "Ticket: Live Concert, Price: 99.99, Ticket ID: TICK5678AB"

## Event

An `Event` represents a collection of tickets. There are different types of events, but all events share some common features. Therefore, we will define an abstract class `Event` to store the common features of different types of events.

* Define an abstract class `Event`.
* Define a constructor for `Event`.
  * It has two parameters: `name` (a string), `max_tickets` (an int).
  * Store these in *public* fields.
  * Add a *private* field `tickets` to store a dictionary of all the tickets that are available for this event.
    * The keys of this dictionary are the ticket_id's.
    * The values of this dictionary are the ticket objects.
  * When created, an `Event` has no tickets.
* Define a read-only property `sold_tickets` that returns the number of tickets sold for this `Event`.
* Define a read-only property `available_tickets` that returns the remaining number of tickets for this `Event`.
  * The remaining number of tickets is obtained by subtracting the `sold_tickets` from the `max_tickets`.
* Define a method `add_ticket(ticket)` to add a `Ticket` to the `tickets` dictionary.
  * When the number of tickets exceeds the available tickets, this method generates a `RunTimeError`.
* Define a method `remove_ticket(ticket)` to remove a `Ticket` from the `tickets` dictionary.
  * When the ticket to be removed is not in the dictionary, this method generates a `RunTimeError`.
* Define a property `ticket_prices` that returns a list of prices (floats) of all the tickets that are in this `Event`.
  * Use List Comprehension for this.
* Define a method `sort_tickets_by_price` that returns a list of tickets sorted by price (high to low) using a lambda function.
* Define an abstract method `create_event_summary()`.

## Types of Events

As previously mentioned, there are different types of Events: Concert, Conference, SportsEvent, etc. Common functionality has already been implemented in Event. Below, we will define two such subclasses to distinguish between types of events. To prevent this exam from becoming too long, we will only implement Concert and Conference.

### `Concert`

A `Concert` inherits from `Event`.

* Define a constructor for `Concert`.
  * It has two parameters, both inherited from the constructor of `Event`.
  * Add another public field `performers` (a list of strings).
* Implement `create_event_summary`
  * This function returns a string representing the event summary.
  * The string is composed of:
    * The name of the Concert
    * The performers in the concert
    * The tickets of the concert (one line per ticket), sorted on the price of the ticket (high to low)
      * Each line is constructed with the ticket_id followed by the price of the ticket and the event_name.
    * See example usage below.

### `Conference`

A `Conference` inherits from `Event`.

* Define a constructor for `Conference`.
  * It has one parameter: `name`, inherited from the constructor of `Event`.
  * The `max_tickets` of a `Conference` is always equal to 500.
* Implement `create_event_summary`
  * This function returns a string representing the event summary.
  * The string is composed of:
    * The name of the Conference
    * The tickets of the conference (one line per ticket), sorted on the price of the ticket (high to low)
      * Each line is constructed with the ticket_id followed by the price of the ticket and the event_name.
    * See example usage below
* Implement the method `add_ticket(ticket)`:
  * Due to the nature of a Conference, only tickets with a price less than or equal to 300.00 can be added.
  * If a ticket with a higher price is added, this method raises a RunTimeError.

  price is added, this method raises a `RunTimeError`.

## Example Usage

```python
# Create some tickets
>>> vip_ticket = Ticket("TICK1234AB", "VIP Concert", 299.99)
>>> regular_ticket = Ticket("TICK5678CD", "Live Concert", 99.99)
>>> conference_ticket = Ticket("TICK2345EF", "Tech Conference", 150.00)
>>> invalid_ticket = Ticket("TICK6789GH", "Sports Event", 75.00)
ValueError: Invalid Ticket ID provided
>>> premium_conference_ticket = Ticket("TICK3456IJ", "Tech Conference", 350.00)

# Print VIP Ticket
>>> print(vip_ticket)
Ticket: "VIP Concert", Price: 299.99, Ticket ID: TICK1234AB

# Create a concert event
>>> rock_concert = Concert("Rock Fest", 500, ["Band A", "Band B", "Band C"])

# Adding tickets to our concert
>>> rock_concert.add_ticket(vip_ticket)
>>> rock_concert.add_ticket(regular_ticket)

# Print ticket prices
>>> print(rock_concert.ticket_prices)
[299.99, 99.99]

# Print Event Summary
>>> print(rock_concert.create_event_summary())
Event: Rock Fest
Performers: Band A, Band B, Band C
TICK1234AB - 299.99 (VIP Concert)
TICK5678CD - 99.99 (Live Concert)

# Create a conference event
>>> tech_conference = Conference("Tech Innovations")

# Adding tickets to our conference
>>> tech_conference.add_ticket(conference_ticket)
>>> tech_conference.add_ticket(premium_conference_ticket)
RuntimeError: Tickets priced above 300.00 cannot be added to a Conference

# Print the conference summary
>>> print(tech_conference.create_event_summary())
Event: Tech Innovations
TICK2345EF - 150.00 (Tech Conference)
```

# Testing
You need to write tests that adequately test the `create_event_summary` method. Include these tests in the `test-ticketing.py` file.

* Refer to the description of both `Concert` and `Conference` for information on how to implement `create_event_summary`.
* Use the conventions you have learned in the Testing chapter to test this functionality.
