# Exam Question: Smart Home Management System

* Place all your code for this exercise in `smarthome.py`.
* Throughout these instructions, include the `self` parameter in all instance methods as needed.
* Ensure all names (class names, method names, parameter names) match the specifications exactly.

---

## Part 1: Validation Utility

1. Define a class named **`Validator`**:
   - Add a **static method** `is_valid_device_id(device_id)` to validate `device_id`s using a regular expression.
   - A valid `device_id` must:
     - Contain exactly 8 characters.
     - Begin with the prefix `DEV`.
     - Be followed by a 5-digit number between **10000** and **99999**.
   - Return `True` if the `device_id` is valid; otherwise, return `False`.
   - Examples of valid IDs: `"DEV12345"`, `"DEV67890"`.  
     Examples of invalid IDs: `"DEV01234"`, `"DEV56789X"`.

---

## Part 2: SmartDevice Class

2. Define a class named **`SmartDevice`**:
   - The constructor accepts:
     1. **`device_id`**: A string representing the unique identifier of the device.
     2. **`device_name`**: A string representing the name of the device (e.g., "Smart Thermostat").
     3. **`power_usage`**: A float representing the power consumption of the device in watts.
   - Raise a `ValueError` if the `device_id` is invalid during instantiation.
   - Store `device_name` and `power_usage` as public attributes.
   - Store `device_id` in a **private attribute**, but make it accessible and modifiable using a property (getter and setter).
   - Implement a **dunder method** (`__str__`) to provide a readable string representation of a `SmartDevice` object:  
     Format:  
     `Device: "<device_name>", Power Usage: <power_usage>W, Device ID: <device_id>`  
     Example: `"Device: Smart Thermostat, Power Usage: 45.0W, Device ID: DEV12345"`

---

## Part 3: SmartHub Abstract Class

3. Define an **abstract class** named **`SmartHub`**:
   - Constructor parameters:
     1. **`name`**: A string representing the name of the smart hub.
     2. **`max_devices`**: An integer defining the maximum number of devices the hub can manage.
   - Store `name` and `max_devices` as public attributes.
   - Use a **private dictionary** `devices` to store the hub's devices:
     - Keys are `device_id`s.
     - Values are `SmartDevice` objects.
     - When initialized, the hub should have no devices.
   - Add a **read-only property** `total_devices`:
     - Returns the number of devices connected to the hub.
   - Add a **read-only property** `available_capacity`:
     - Returns the hub's remaining capacity (`max_devices - total_devices`).
   - Define a method `add_device(device)`:
     - Adds a device to the hub.
     - Raises an exception if adding the device exceeds the hub's capacity.
   - Define a method `remove_device(device_id)`:
     - Removes a device from the hub using its `device_id`.
     - Raises an exception if the `device_id` does not exist in the hub.
   - Add a property `power_consumption`:
     - Returns the total power consumption of all devices using **list comprehension**.
   - Add a method `sort_devices_by_power()`:
     - Returns a list of devices sorted by power consumption (from high to low) using a lambda function.
   - Define an **abstract method** `generate_hub_report()`.

---

## Part 4: SmartHub Subclasses

### 4.1 `HomeHub`

Define a class **`HomeHub`** that inherits from `SmartHub`:
   - Constructor parameters:
     1. Inherits `name` and `max_devices` from `SmartHub`.
     2. **`residents`**: A list of strings representing the names of people who use the hub.  
        Store this as a public attribute.
   - Add a method `add_resident(resident)` to add a person to the `residents` list.
   - Implement the `generate_hub_report()` method:
     - Returns a report string containing:
       - The hub's name.
       - A list of its residents.
       - A list of its devices sorted by power usage (from high to low).
     - For each device, display the `device_id`, power usage, and device name.

### 4.2 `CorporateHub`

Define a class **`CorporateHub`** that inherits from `SmartHub`:
   - Constructor parameter:
     1. Inherits `name` from `SmartHub`.
     - The `max_devices` for a corporate hub is always **100**.
   - Implement the `generate_hub_report()` method:
     - Returns a report string containing:
       - The hub's name.
       - A list of its devices sorted by power usage (from high to low).
     - For each device, display the `device_id`, power usage, and device name.
   - Override the `add_device(device)` method:
     - Only allows devices with power usage **≤ 500.0W** to be added.
     - Raises a `RuntimeError` if the device's power usage exceeds this limit.

---

## Example Usage

```python
# Create devices
>>> thermostat = SmartDevice("DEV12345", "Smart Thermostat", 45.0)
>>> lightbulb = SmartDevice("DEV67890", "Smart Lightbulb", 10.0)
>>> heater = SmartDevice("DEV23456", "Smart Heater", 1500.0)

# Invalid Device ID example
>>> invalid_device = SmartDevice("DEV12", "Invalid Device", 500.0)
ValueError: Invalid Device ID provided

# Print a device
>>> print(thermostat)
Device: Smart Thermostat, Power Usage: 45.0W, Device ID: DEV12345

# Create and manage a Home Hub
>>> home_hub = HomeHub("Family Hub", 10, ["Alice", "Bob"])
>>> home_hub.add_device(thermostat)
>>> home_hub.add_device(lightbulb)

>>> print(home_hub.generate_hub_report())
Hub: Family Hub
Residents: Alice, Bob
DEV12345 - 45.0W (Smart Thermostat)
DEV67890 - 10.0W (Smart Lightbulb)

# Create a Corporate Hub
>>> corporate_hub = CorporateHub("Office Hub")
>>> corporate_hub.add_device(heater)
RuntimeError: Devices with power usage above 500.0W cannot be added to a CorporateHub
```

---

## Part 5: Testing

Write unit tests to validate the behavior of `generate_hub_report`. Include these tests in `test_smarthome.py` and adhere to testing best practices.
