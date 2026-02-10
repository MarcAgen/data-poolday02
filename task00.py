##
## EPITECH PROJECT, 2026
## day02
## File description:
## task00
##

def multiply(a, b):
    return a * b

def multiply2(x):
    return x * 2

def multiply10(x):
    return x * 10

def getSecondMax(numbers):
    max = numbers[0]
    second_max:int

    if all(x == numbers[0] for x in numbers):
        return numbers[0]

    for i in numbers:
        if i > max:
            max = i
    for i in numbers:
        if i < max:
            second_max = i
            break
    for i in numbers:
        if i < max and i > second_max:
            second_max = i
    return second_max
