# 0x0A. Python - Inheritance

This sub-project focuses on inheritance in Python. Inheritance is a fundamental concept in object-oriented programming that allows classes to inherit attributes and methods from other classes. It provides a way to create hierarchical relationships between classes, promoting code reuse and organization.

## Learning Objectives

- What is a superclass, baseclass, or parent class?
- What is a subclass, derived class, or child class?
- How to define and use inheritance in Python
- What is the `super` function and how to use it
- What is a method override and when to use it
- What is a class attribute and instance attribute, and the difference between them
- What is an is-a relationship and a has-a relationship
- What is the difference between inheritance and composition
- How to create a subclass that inherits from multiple superclasses

## Files

The following files are included in this sub-project:

| Filename | Description |
| -------- | ----------- |
| `0-lookup.py` | Python function that returns the list of available attributes and methods of an object |
| `1-my_list.py` | Class `MyList` that inherits from the built-in class `list` |
| `2-is_same_class.py` | Python function that checks if an object is an instance of a specified class |
| `3-is_kind_of_class.py` | Python function that checks if an object is an instance of a class or inherited from a specified class |
| `4-inherits_from.py` | Python function that checks if an object is an instance of a class that inherited (directly or indirectly) from a specified class |
| `5-base_geometry.py` | Empty class `BaseGeometry` |
| `6-base_geometry.py` | Class `BaseGeometry` with public instance method `def area(self):` that raises an exception |
| `7-base_geometry.py` | Class `BaseGeometry` with public instance methods `def area(self):` and `def integer_validator(self, name, value):` |
| `8-rectangle.py` | Class `Rectangle` that inherits from `BaseGeometry` |
| `9-rectangle.py` | Class `Rectangle` that inherits from `BaseGeometry`. Adds width and height validation |
| `10-square.py` | Class `Square` that inherits from `Rectangle` |
| `11-square.py` | Class `Square` that inherits from `Rectangle`. Adds area calculation |

## Usage

Each file in this sub-project is intended to be executed on its own to showcase the concepts and implementation of inheritance in Python. Feel free to explore each file and run them individually to see the results.

```bash
$ python3 0-lookup.py
$ python3 1-my_list.py
$ python3 2-is_same_class.py
$ python3 3-is_kind_of_class.py
$ python3 4-inherits_from.py
$ python3 5-base_geometry.py
$ python3 6-base_geometry.py
$ python3 7-base_geometry.py
$ python3 8-rectangle.py
$ python3 9-rectangle.py
$ python3 10-square.py
$ python3 11-square.py
```

## Resources

- [Inheritance - Python Documentation](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Inheritance in Python - GeeksforGeeks](https://www.geeksforgeeks.org/inheritance-in-python/)
- [Python Inheritance Tutorial - Real Python](https://realpython.com/python-inheritance/)
- [Understanding Class Inheritance in Python 3 - DigitalOcean](https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3)