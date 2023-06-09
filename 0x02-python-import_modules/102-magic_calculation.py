#!/usr/bin/python3

def magic_calculation(firstNumber, secondNumber):
    """Match bytecode provided"""
    from magic_calculation_102 import add, sub

    if firstNumber < secondNumber:
        result = add(firstNumber, secondNumber)
        for i in range(4, 6):
            result = add(result, i)
        return (result)

    else:
        return (sub(firstNumber, secondNumber))
