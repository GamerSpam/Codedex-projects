# Calculator lesson from Codedex

# WIP I am searching for a way to remove the trailing zeros from non decimal numbers.

import sys

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
    try:
        result = a / b
        return result
    except TypeError:
        a = int(a)
        b = int(b)
        result = a / b
        return result

def exp(a, b):
    result = a ** b
    return result

def inp2():
    while True:
        try:
            val2 = float(input('\nWhat is the second value? '))
            return val2
        except ValueError:
            print('Value must be a number.')

operation = [add, subtract, multiply, divide, exp]

def calc():
    print('''
==========================
======= Calculator =======
==========================
        ''')


    print('''

What operation do you wish to perform? 
1) addition
2) subtraction
3) multiplaction
4) division
5) exponent
6) quit
''')

    while True:
        try:
            op = int(input())
            if op < 1 or op > 5:
                raise Exception
            break
        except ValueError:
            print('Please input a number')
        except:
            if op == 6:
                sys._ExitCode
            else:
                print('Please enter a number in the list')
    
    while True:
        try:
            val1 = float(input('\nWhat is the first value? '))
            break
        except ValueError:
            print('Value must be a number.')

    while True:
        try:
            print(operation[op - 1](val1, inp2()))
            break
        except ZeroDivisionError:
            print('Cannot divide by zero.\nPlease reneter value 2.')

calc()