# Exam Question 2: Gaming Inventory System

* Place all code for this exercise in `inventory.py`.
* In these instructions, we always omit mentioning `self`.
  It is up to you to know when to add this extra parameter.
* Make sure you get the names exactly right, including the parameter names.

---

## Util

* Define a class `Util`.
* Define a static method `is_valid_item_id(item_id)` that returns `True` if the item\_id is valid, otherwise `False`. Check this using a regular expression.

  * An `item_id` consists of exactly 9 characters.
  * An `item_id` always starts with `ITM`.
  * This is followed by a 4-digit number between 1000 and 9999.
  * Finally, there are 2 uppercase letters.
  * Examples: `"ITM1234AB"` and `"ITM5678CD"` are valid item\_ids, but `"ITM0123B"` and `"ITM56789EF"` are not.

---

## Item

* Define a class `Item`.
* Define the constructor of `Item`.

  * The constructor takes three parameters: `item_id` (a string), `name` (a string), and `value` (a float).
  * When an instance of `Item` is created with an invalid item\_id, a `ValueError` should be raised.
* Store `name` and `value` in public fields.
* Store `item_id` in a private field and make it accessible via a property.
* Add the `dunder method` to provide a readable string representation of the item object.

  * Example:

    * `"Item: Sword of Power, Value: 499.99, Item ID: ITM1234AB"`

---

## Inventory

An `Inventory` represents a collection of game items. There are different types of inventories (depending on the game), but all inventories share some common features. Therefore, we will define an abstract class `Inventory` to store the common features.

* Define an abstract class `Inventory`.
* Define a constructor for `Inventory`.

  * It has two parameters: `owner` (a string), `max_items` (an int).
  * Store these in *public* fields.
  * Add a *private* field `items` to store a dictionary of all the items in this inventory.

    * The keys of this dictionary are the item\_ids.
    * The values are the item objects.
  * When created, an `Inventory` has no items.
* Define a read-only property `stored_items` that returns the number of items currently in the inventory.
* Define a read-only property `available_space` that returns how many more items can be stored.
* Define a method `add_item(item)` to add an `Item` to the `items` dictionary.

  * When the number of items exceeds the available space, this method generates a `RunTimeError`.
* Define a method `remove_item(item)` to remove an `Item` from the `items` dictionary.

  * When the item is not in the dictionary, this method generates a `RunTimeError`.
* Define a property `item_values` that returns a list of the values of all the items.
* Define a method `sort_items_by_value` that returns a list of items sorted by value (high to low).
* Define an abstract method `create_inventory_summary()`.

---

## Types of Inventories

We will define two subclasses: `PlayerInventory` and `GuildInventory`.

### `PlayerInventory`

A `PlayerInventory` inherits from `Inventory`.

* Define a constructor for `PlayerInventory`.

  * It has two parameters, both inherited from `Inventory`.
  * Add another public field `character_class` (a string, e.g., `"Mage"`, `"Warrior"`).
* Implement `create_inventory_summary`:

  * The summary should include:

    * The name of the player (owner).
    * The character class.
    * The list of items (one line per item), sorted by value (high to low).

      * Each line: `item_id - value (name)`

---

### `GuildInventory`

A `GuildInventory` inherits from `Inventory`.

* Define a constructor for `GuildInventory`.

  * It has one parameter: `owner`, inherited from `Inventory`.
  * The `max_items` of a `GuildInventory` is always equal to 1000.
* Implement `create_inventory_summary`:

  * The summary should include:

    * The guild name (owner).
    * The list of items (sorted by value high → low).
* Implement the method `add_item(item)`:

  * Only items with a value less than or equal to 1000.00 can be added.
  * If a more expensive item is added, this method raises a `RunTimeError`.

---

## Example Usage

```python
# Create some items
>>> sword = Item("ITM1234AB", "Sword of Power", 499.99)
>>> potion = Item("ITM5678CD", "Health Potion", 29.99)
>>> guild_banner = Item("ITM2345EF", "Guild Banner", 750.00)
>>> invalid_item = Item("ITM789GH", "Broken Shield", 15.00)
ValueError: Invalid Item ID provided
>>> legendary_artifact = Item("ITM3456IJ", "Legendary Artifact", 5000.00)

# Print Sword
>>> print(sword)
Item: Sword of Power, Value: 499.99, Item ID: ITM1234AB

# Create a player inventory
>>> mage_inventory = PlayerInventory("Arthas", 20, "Mage")

# Add items
>>> mage_inventory.add_item(sword)
>>> mage_inventory.add_item(potion)

# Print item values
>>> print(mage_inventory.item_values)
[499.99, 29.99]

# Print inventory summary
>>> print(mage_inventory.create_inventory_summary())
Player: Arthas (Class: Mage)
ITM1234AB - 499.99 (Sword of Power)
ITM5678CD - 29.99 (Health Potion)

# Create a guild inventory
>>> guild_inventory = GuildInventory("Knights of Valor")

# Add items
>>> guild_inventory.add_item(guild_banner)
>>> guild_inventory.add_item(legendary_artifact)
RuntimeError: Items valued above 1000.00 cannot be added to a GuildInventory

# Print guild summary
>>> print(guild_inventory.create_inventory_summary())
Guild: Knights of Valor
ITM2345EF - 750.00 (Guild Banner)
```
