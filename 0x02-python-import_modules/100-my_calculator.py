#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys


def operationSolver():
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operands = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in operands:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = operands[sys.argv[2]](a, b)
    print(f"{a} {sys.argv[2]} {b} = {result}")


if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    operationSolver()
