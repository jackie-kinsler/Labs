"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculator():
    operator = ''

    while operator != "q":
        user_input = input().split(" ")
        operator = user_input[0]

        if len(user_input) > 1:
            first_value = int(user_input[1])

        if len(user_input) >= 3: 
            second_value = int(user_input[2]) 

        if operator == "square":
            print (square(first_value))
        elif operator == "cube":
            print (cube(first_value))
        elif operator == "+":
            print (add(first_value, second_value))
        elif operator == "-":
            print (subtract(first_value, second_value))
        elif operator == "*":
            print (multiply(first_value, second_value))
        elif operator == "/":
            print (divide(first_value, second_value))
        elif operator == "pow":
            print (power(first_value, second_value))
        elif operator == "mod":
            print (mod(first_value, second_value))
        
calculator()
