# Employees System Project

The **Employee Management System** assignment, the goal is to manage employee data and handle various employee-related operations (such as hiring, firing, updating details, etc.) using OOP concepts.

The system consists of three primary classes:

1. **Employee**
2. **EmployeesManager**
3. **FrontendManager**

Each class should be implemented in a separate file, and the system should be functional when running the main file. The classes should follow principles of object-oriented design and be able to work together seamlessly to manage employees. Not much information is giving to start, it is up to you to figure out how to programming this system.

## Table of Contents

- [Introduction](#introduction)
- [Classes](#classes)
  - [Employee](#employee)
  - [EmployeesManager](#employeesmanager)
  - [FrontendManager](#frontendmanager)

## Introduction

The Employees System Project demonstrates the implementation of object-oriented programming concepts in Python. It encompasses three primary classes, each serving a distinct purpose:

### Employee

The `Employee` class represents an individual employee with the following attributes:

- `name`: The name of the employee.
- `age`: The age of the employee.
- `salary`: The salary of the employee.

This class provides methods for string representation and formatted output of employee information.

### EmployeesManager

The `EmployeesManager` class is responsible for managing a list of employees. It offers functionalities to:

- Add a new employee to the list.
- List all existing employees.
- Delete employees within a specified age range.
- Find an employee by their name.
- Update an employee's salary by name.

### FrontendManager

The `FrontendManager` class provides a user interface for interacting with the `EmployeesManager`. Users can perform actions such as:

- Adding new employees.
- Listing existing employees.
- Deleting employees based on age range.
- Updating employee salaries by name.