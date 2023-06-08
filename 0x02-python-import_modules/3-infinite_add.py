#!/usr/bin/python3

import sys

def summer():
    """Print the addition of all arguments."""
    total = sum(int(arg) for arg in sys.argv[1:])
    print(total)

if __name__ == "__main__":
    summer()
