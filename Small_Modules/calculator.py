# Calculator lesson from Codedex

from decimal import * # Allows me perform arithmatic on floating point and integer numbers without trailing 0s on integers. It also cleans up the output so that you don't get weird floating point errors.

from decimal import *

while True:
    try:
        deci = int(input('Max decimal places? '))
        break
    except ValueError:
        print('Please enter an integer.')

getcontext().prec = deci # Allows the user to set the desired number of decimal places to be displayed. This will be used as the max number of decimal places.

def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
        result = a / b
        return result

def exp(a, b):
    result = a ** b
    return result

def inp2():
    while True:
        try:
            val2 = Decimal(input('\nWhat is the second value? ')) # Handles the second variable. this is not stored outside the function.
            return val2
        except ValueError:
            print('Value must be a number.')

operation = [add, subtract, multiply, divide, exp] # allows me to call the function from the list

def calc(): # places the main program inside a function to eliminate the need for an overall while loop.
    print('''
==========================
======= Calculator =======
==========================''')


    print('''
What operation do you wish to perform?

1) addition
2) subtraction
3) multiplaction
4) division
5) exponent
6) quit
''')

    while True: # handles errors in selection of operation.
        try:
            op = int(input())
            if op < 1 or op > 5:
                raise Exception
            break
        except ValueError:
            print('Please input a number')
        except:
            if op == 6:
                exit()
            else:
                print('Please enter a number in the list')

    while True:
        try:
            val1 = Decimal(input('\nWhat is the first value? ')) # Converts the output to a decimal using the decimal module
            break
        except ValueError:
            print('Value must be a number.')

    while True:
        try:
            print(operation[op - 1](val1, inp2())) # pulls the function based on the users selection, and feeds the variables into it.
            input('Press \'enter\' to continue ')
            break
        except ZeroDivisionError: # In the event that someone tries to divide by zero.
            print('Cannot divide by zero.\nPlease reneter value 2.')

while True: # Keeps the program running until the user quits
    calc()