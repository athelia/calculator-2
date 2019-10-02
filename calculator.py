"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def get_user_input():
    user_input = input()
    user_input = user_input.split()
    return user_input

def make_float(user_input):
    for i in range(1,len(user_input)):
        user_input[i] = float(user_input[i])
        i += 1
    return user_input

def calculate(user_input):
    which_operation = user_input[0]
    num1 = user_input[1]
    if len(user_input)>2:
        num2 = user_input[2]

    if which_operation == "+":
        add(num1, num2)
    elif which_operation == "-":
        subtract(num1, num2)
    elif which_operation == "*":
        multiply(num1, num2)
    elif which_operation == "/":
        divide(num1, num2)
    elif which_operation == "square":
        square(num1)
    elif which_operation == "cube":
        cube(num1)
    elif which_operation == "pow":
        power(num1, num2)
    elif which_operation == "mod":
        mod(num1, num2)
    elif which_operation == "q":
        return

#print(get_user_input())
