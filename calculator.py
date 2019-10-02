"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def get_user_input():
    user_input = input()
    user_input = user_input.split()
    return user_input

def integerize(user_input):
    for i in range(1,len(user_input)):
        user_input[i] = float(user_input[i])
        i += 1
    return user_input

#print(get_user_input())
