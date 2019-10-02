"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""


from arithmetic import *


def get_user_input():
    user_input = input("> ")
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
        print(add(num1, num2))
    elif which_operation == "-":
        print(subtract(num1, num2))
    elif which_operation == "*":
        print(multiply(num1, num2))
    elif which_operation == "/":
        print(divide(num1, num2))
    elif which_operation == "square":
        print(square(num1))
    elif which_operation == "cube":
        print(cube(num1))
    elif which_operation == "pow":
        print(power(num1, num2))
    elif which_operation == "mod":
        print(mod(num1, num2))
    elif which_operation == "q":
        return

def run_calculator():
    user_input = get_user_input()
    user_input = make_float(user_input)
    result = calculate(user_input)
    print(result)

#print(get_user_input())

print(run_calculator())