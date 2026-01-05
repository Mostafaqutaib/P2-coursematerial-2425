
# **Exercise: Zoo Management System**

You are tasked with designing a zoo management system to handle information about different types of animals, their diets, living environments, and caretakers. The zoo has various types of animals, and each has distinct characteristics and behaviors. The management system should be able to organize animals into categories, calculate their food requirements, track their health, and generate reports.

---

## **Requirements**

### Part 1: Abstract Animal Class
1. Define an abstract class **`Animal`**:
   - Constructor parameters:
     1. **`name`**: A string representing the animal’s name.
     2. **`age`**: An integer representing the animal’s age.
     3. **`species`**: A string indicating the species of the animal.
   - Create public attributes for `name`, `age`, and `species`.
   - Define private attributes:
     1. **`health`**: An integer (ranging from 0 to 100) that tracks the animal’s health.
     2. **`food_requirements`**: A float representing the daily food requirement in kilograms.
   - Add a property **`health`**:
     - Getter: Returns the animal’s health value.
     - Setter: Updates the health value, ensuring it remains between 0 and 100.
   - Add a property **`food_requirements`**:
     - Getter: Returns the daily food requirement.
     - Setter: Updates the food requirement, ensuring it remains positive.
   - Implement an abstract method **`calculate_food_requirements()`**:
     - Child classes must calculate food requirements based on their species and age.
   - Implement an abstract method **`generate_report()`**:
     - This method generates a detailed report about the animal’s name, age, species, health, and food requirements.

---

### Part 2: Animal Subclasses

#### **2.1 Mammal**
- Define a class **`Mammal`** that inherits from `Animal`:
  - Constructor parameters:
    1. **`fur_type`**: A string indicating the type of fur (e.g., "short", "long").
  - Store `fur_type` as a public attribute.
  - Override **`calculate_food_requirements()`**:
    - Mammals require food calculated as:  
      $$\text{food requirement} = \text{age} \times 0.5\ (in kg)$$
  - Override **`generate_report()`**:
    - Include `fur_type` in the report.

#### **2.2 Bird**
- Define a class **`Bird`** that inherits from `Animal`:
  - Constructor parameters:
    1. **`wing_span`**: A float representing the wingspan in meters.
  - Store `wing_span` as a public attribute.
  - Override **`calculate_food_requirements()`**:
    - Birds require food calculated as:  
      $$\text{food requirement} = \text{age} \times 0.2\ (in kg)$$
  - Override **`generate_report()`**:
    - Include `wing_span` in the report.

#### **2.3 Reptile**
- Define a class **`Reptile`** that inherits from `Animal`:
  - Constructor parameters:
    1. **`is_venomous`**: A boolean indicating if the reptile is venomous.
  - Store `is_venomous` as a public attribute.
  - Override **`calculate_food_requirements()`**:
    - Reptiles require food calculated as:  
      $$\text{food requirement} = \text{age} \times 0.3\ (in kg)$$
  - Override **`generate_report()`**:
    - Include whether the reptile is venomous in the report.

---

### Part 3: Zoo Class
Define a class **`Zoo`**:
1. Constructor parameters:
   - **`name`**: A string representing the zoo’s name.
   - **`location`**: A string representing the zoo’s location.
2. Attributes:
   - Store `name` and `location` as public attributes.
   - Use a private list `_animals` to store all animals in the zoo.
3. Implement a method **`add_animal(animal)`**:
   - Adds an `Animal` to the zoo.
   - Raises a `TypeError` if the argument is not an instance of the `Animal` class.
4. Implement a method **`remove_animal(animal_name)`**:
   - Removes an animal from the zoo based on its name.
   - Raises a `ValueError` if no animal with the given name exists.
5. Implement a method **`calculate_total_food()`**:
   - Returns the total daily food requirement for all animals in the zoo.
6. Implement a method **`generate_zoo_report()`**:
   - Generates a report including:
     - The zoo’s name and location.
     - The total number of animals.
     - Individual reports for each animal.

---

### Part 4: Advanced Functionality

#### **4.1 Health Check**
Implement a method **`check_animal_health(threshold)`** in the `Zoo` class:
   - Finds and lists all animals with health values below the given threshold.

#### **4.2 Categorize Animals**
Implement a method **`categorize_animals()`** in the `Zoo` class:
   - Categorizes animals into groups based on their species and returns a dictionary.

#### **4.3 Seasonal Food Adjustment**
Add a method **`adjust_food_for_season(season)`**:
   - In winter, increase food requirements for mammals by 20%.
   - In summer, decrease food requirements for reptiles by 10%.
   - Leave birds’ food requirements unchanged.

---

### Example Usage

```python
# Create animals
lion = Mammal("Lion", 5, "Panthera leo", "short")
parrot = Bird("Parrot", 2, "Psittacidae", 0.25)
python_snake = Reptile("Python", 3, "Pythonidae", True)

# Calculate food requirements
lion.calculate_food_requirements()
parrot.calculate_food_requirements()
python_snake.calculate_food_requirements()

# Generate individual reports
print(lion.generate_report())
print(parrot.generate_report())
print(python_snake.generate_report())

# Create a zoo
zoo = Zoo("Safari Zoo", "California")

# Add animals to the zoo
zoo.add_animal(lion)
zoo.add_animal(parrot)
zoo.add_animal(python_snake)

# Generate zoo report
print(zoo.generate_zoo_report())

# Check animals with low health
low_health_animals = zoo.check_animal_health(threshold=50)
print(low_health_animals)

# Categorize animals
categories = zoo.categorize_animals()
print(categories)

# Adjust food for winter
zoo.adjust_food_for_season("winter")
print(zoo.generate_zoo_report())
```
