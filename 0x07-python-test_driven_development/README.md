# 0x07. Python - Test-driven development

## Description

The "0x07. Python - Test-driven development" project introduces the concept of test-driven development (TDD) in Python. Test-driven development is a software development approach that emphasizes writing tests before writing the actual code. By following this approach, we can ensure that our code meets the desired functionality and behaves as expected.

This project focuses on creating unit tests using the `doctest` module in Python. Unit tests are written to verify the correctness of small units of code, such as functions or methods. By writing comprehensive unit tests, we can catch bugs and errors early in the development process and ensure that our code functions as intended.

Throughout this project, we create a series of Python functions and write corresponding tests for each function. The tests are written in the form of docstrings using the `doctest` module, allowing us to run the tests directly from the command line.

The project aims to familiarize you with the principles of test-driven development and provide hands-on experience in writing tests for Python functions. By the end of this project, you will have a solid understanding of how to write effective unit tests and how to use test-driven development to improve the quality and reliability of your code.

## Learning Objectives

1. Understand the concept of test-driven development (TDD) and its benefits.
2. Learn how to write unit tests using the `doctest` module in Python.
3. Gain proficiency in writing test cases to validate the functionality of Python functions.
4. Understand the structure and format of test cases in `doctest` format.
5. Explore various scenarios and edge cases to ensure comprehensive test coverage.
6. Learn how to run and interpret test results using the `doctest` module.

By the end of this project, you should be able to apply test-driven development principles to your Python projects, ensuring the quality, correctness, and reliability of your code.

## Contents

This project contains the following files and directories:

- **README.md**: Provides an overview and description of the project.
- **0-add_integer.py**: Python module that contains a function to add two integers.
- **tests/**: Directory that contains test files for each Python module.
  - **0-add_integer.txt**: Test cases for the `0-add_integer.py` module written in `doctest` format.

## How to Use

To explore the contents of this project, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd 0x07-python-test_driven_development`
3. Open the Python module file (`0-add_integer.py`) to view the implementation of the function.
4. Open the test file (`tests/0-add_integer.txt`) to view the test cases written in `doctest` format.
5. Run the tests using the `doctest` module from the command line:
   - `python3 -m doctest -v ./tests/0-add_integer.txt`

The test results will be displayed on the console, indicating the number of tests passed and any failures encountered.

Feel free to explore and modify the code and tests as needed. You can also create additional test files or modules to further practice test-driven development.

## Acknowledgements

This project is part of the Holberton School curriculum.