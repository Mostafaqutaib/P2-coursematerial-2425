# Exam Question 1: Carshow

* Place all code for this exercise in `carshow.py`.
* In these instructions, we always omit the mention of `self`.
  It is up to you to know when to add this extra parameter.
* Make sure you have the names exactly right, even those of the parameters.
* You have received a file `basic_tests.py` that contains basic tests, such as whether certain classes exist and if you used the correct names.
  * Run these tests with the command:

    ```bash
    $ pytest basic_tests.py
    ```

  * A missing class will cause tests targeting that class to be skipped.
    Skipped tests still count as failed.
  * The tests only perform superficial checks.
    Failing/skipped tests mean that your code is certainly incomplete or incorrect.
    But passing tests do not mean your code is fully correct!
* You must also write some tests yourself in the file `test-carshow.py`.
  * All tests that you need to write yourself are indicated in this assignment file.
  * You can add extra tests here if you want to check your code more thoroughly. Only the tests requested in the assignment will be assessed.
  * This test file must be able to run correctly to earn points.

## Util

* Define a class `Util`.
* Define a static method `is_valid_license_plate(license_plate)` that returns `True` if the license_plate is valid based on a regular expression, otherwise `False`.
  * A license_plate consists of 3 parts.
    * The first part consists of the digit 1 or 2
    * The second part consists of three uppercase letters, from AAA to ZZZ
    * The third part consists of three digits, from 111 to 999
  * The three parts of a license_plate are separated by a hyphen (-).
  * Examples: "2-BFQ-223", "1-LUV-368", and "1-ABC-123" are valid license_plates, but "3-XYZ-456", "2-123-ABC", and "1-Gta-276" are not.

## Car

There are various types of cars, but all cars share some common characteristics. Therefore, we will define an abstract class `Car` to store common features of different types of cars.

* Define an abstract class `Car`.
* Define the constructor of `Car`.
  * The constructor takes three parameters: `license_plate` (a string), `color` (a string), `amount_wheels` (an int).
  * When an instance of a `Car` is created with an invalid `license_plate`, a `ValueError` should be raised.
* Store `color` and `amount_wheels` in public fields.
* Store `license_plate` in a private field and make it accessible via a property.
  * Define a getter and a setter for `license_plate`.
* Define an abstract method `get_price()`.

## Types of Cars

As mentioned earlier, there are various types of cars: Supercars, Sedans, Trucks, etc...
Common functionality is already implemented in `Car`. Below, we will define two such subclasses to differentiate between types of cars. To prevent this exam from becoming too long, we will only implement `Supercar` and `Truck`.

### `Supercar`

A `Supercar` inherits from `Car`.

* Define a constructor for `Supercar`.
  * It takes three parameters
    * `license_plate` and `color` are inherited from the `Car` constructor.
      * The amount of wheels of a supercar is always equal to 4.
    * An additional parameter, `top_speed`, which is an integer.
      * Store `top_speed` as a public field.
* Implement `get_price`
  * Calculate the price of this Supercar:
  * The price is calculated by multiplying 500 by the top speed divided by the number of wheels.

### `Truck`

A `Truck` inherits from `Car`.

* Define a constructor for `Truck`.
  * It takes four parameters
    * `license_plate`, `color` and `amount_wheels` inherited from the `Car` constructor.
    * An additional parameter, `weight_of_load`, which is an integer.
      * Store `weight_of_load` as a public field.
* Implement `get_price`
  * Calculate the price of this Truck:
  * The cost is calculated by multiplying 25 by the weight of load divided by the number of wheels.

### `Car (bis)`

* Add the dunder method to provide a readable string representation of the car object.
  * When this function is called, the following output is generated if it is a supercar: `License Plate: "license_plate", Color: "color", Amount of Wheels: "amount_wheels", Top Speed: "top_speed"`
  * When this function is called, the following output is generated if it is a truck: `License Plate: "license_plate", Color: "color", Amount of Wheels: "amount_wheels", Weight of Load: "weight_of_load"`
  * Examples:
    * print(mclarenp1)
    * "License Plate: 2-BFQ-223, Color: Orange, Amount of Wheels: 4, Top Speed: 350"
    * print(scania)
    * "License Plate: 1-ABC-123, Color: Blue, Amount of Wheels: 8, Weight of Load: 32000"

## Carshow

A `Carshow` represents a car show containing multiple cars.

* Define a class `Carshow`.
* Define a constructor for `Carshow`.
  * It takes three parameters: `name` (a string), `halls` (an int), `spots` (an int).
  * Store these in *public* fields.
  * Add a *private* field `cars` to store a list of all cars present in the car show.
    * The values of this list are the car objects.
  * Upon creation, a `Carshow` has no registered cars.
* Define a read-only property `number_of_cars` returning the number of registered `cars` for this `Carshow`.
* Define a method `add_car(car)` to add a `Car` to the `cars` list.
  * When the maximum number of cars has already been reached, this method raises a `RunTimeError`.
  * The maximum number of allowed cars is the number of halls multiplied by the number of spots.
* Define a method `remove_car(car)` to remove a `Car` from the `cars` list.
  * When the car to be removed is not in the list, this method raises a `RunTimeError`.
* Define a property `car_license_plates` returning a list of license plates (strings) of all cars present in this `Carshow`.
  * Utilize List Comprehension for this.
* Define a method `sort_cars_by_license_plate` returning a list of cars sorted in ascending order based on license plate using a lambda function.
* Define a method `get_total_price()`.
  * Returns the total price of the car show by summing the individual prices of each car.

## Example Usage

```python
# Making some cars
>>> mclarenp1 = Supercar("2-BFQ-223", "Orange", 350)
>>> bugattichiron = Supercar("1-LUV-368", "Black", 420)
>>> faulty_car = Supercar("1-Gta-276", "Green" , 10)
ValueError("Invalid license plate provided")
>>> scania = Truck("1-ABC-123", "Blue", 8, 32000)
>>> iveco = Truck("2-IVE-400", "White", 10, 40000)
>>> dactrucks = Truck("1-DAC-440", "Yellow", 12, 44000)

# Print Sportscar
>>> print(mclarenp1)
License Plate: 2-BFQ-223, Color: Orange, Amount of Wheels: 4, Top Speed: 350
# Print Truck
>>> print(scania)
License Plate: 1-ABC-123, Color: Blue, Amount of Wheels: 8, Weight of Load: 32000

# Calculating the price of a car
>>> print(bugattichiron.get_price())
52500.0
>>> print(iveco.get_price())
100000.0

# Making a Carshow
>>> ucll_carshow = Carshow("UCLL Carshow", 1, 3)

# Adding some cars to the carshow
>>> ucll_carshow.add_car(mclarenp1)
>>> ucll_carshow.add_car(bugattichiron)
>>> ucll_carshow.add_car(scania)
>>> ucll_carshow.add_car(dactrucks)
RuntimeError("The carshow is full")
>>> ucll_carshow.remove_car(iveco)
RuntimeError("Car was not in the carshow")
>>> ucll_carshow.remove_car(scania)
>>> ucll_carshow.add_car(dactrucks)

# Carshow methods & properties
>>> print(ucll_carshow.number_of_cars)
3
>>> print(ucll_carshow.car_license_plates)
['2-BFQ-223', '1-LUV-368', '1-DAC-440']

>>> print(ucll_carshow.get_total_price())
187916.6666666667
```

# Testing

You need to write tests that sufficiently test the `get_price` property. Include these tests in the file `test-carshow.py`.

* Refer to the descriptions of both `Supercar` and `Truck` for information on how to implement `get_price`.
* Use the conventions you have learned in the Testing chapter to test this functionality.