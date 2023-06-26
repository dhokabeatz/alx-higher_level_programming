#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    newList = []
    for number in range(0, list_length):
        try:
            result = my_list_1[number] / my_list_2[number]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            newList.append(result)
    return (newList)
