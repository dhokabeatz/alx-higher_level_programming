# 0x0C. Python - Almost a Circle

![Python](https://img.shields.io/badge/python-v3.8-blue)

This is a sub-project of the ALX-Holberton School Low-level Programming curriculum, focusing on advanced Python concepts. In this project, we work on creating a base class and subclasses to represent geometric shapes, specifically rectangles and squares. We implement various functionalities related to these shapes, including calculations, serialization, and deserialization.

The goal of this project is to apply object-oriented programming principles and techniques in Python to build a robust and flexible class hierarchy for geometric shapes. We use inheritance, encapsulation, and polymorphism to create reusable and extensible code.

## Project Structure

The repository is organized into multiple directories, each containing Python scripts and code files related to specific concepts or tasks. Here is an overview of the directory structure:

- `models/`: Directory containing the implementation of the base class and subclasses for geometric shapes.
- `tests/`: Directory containing test files and scripts to verify the functionality of the implemented code.
- `main_files/`: Directory containing additional main files to showcase the usage of the implemented classes.

Here are the key files and directories within the project:

- `models/base.py`: Python module containing the definition of the `Base` class, which serves as the base class for all other shapes.
- `models/rectangle.py`: Python module containing the definition of the `Rectangle` class, a subclass of `Base` representing rectangles.
- `models/square.py`: Python module containing the definition of the `Square` class, a subclass of `Rectangle` representing squares.
- `models/__init__.py`: Empty `__init__.py` file to mark the `models` directory as a Python package.
- `tests/`: Directory containing various test scripts to validate the functionality of the implemented classes.
- `main_files/`: Directory containing main scripts that demonstrate the usage of the implemented classes.

## Getting Started

To get started with this project, you can follow these steps:

1. Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/dhokabeatz/alx-higher_level_programming.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x0C-Python_Almost_a_Circle
   ```

3. Explore the individual files within the `models` directory to understand the class hierarchy and implementations.

4. Review the test files in the `tests` directory to understand the test cases for the implemented code.

5. Optionally, run the test files using the following command to verify the functionality:

   ```bash
   python3 -m unittest discover tests
   ```

6. Check the main files within the `main_files` directory to see examples of how to use the implemented classes.

## Resources

- [Python Object-Oriented Programming (OOP)](https://realpython.com/python3-object-oriented-programming/)
- [Python `unittest` Module](https://docs.python.org/3/library/unittest.html)
- [Python `json` Module](https://docs.python.org/3/library/json.html)
- [Python File Input/Output](https://docs.python.org/3/tutorial/inputoutput.html)

## Author

This project is implemented and maintained by [@dhokabeatz](https://github.com/dhokabeatz).