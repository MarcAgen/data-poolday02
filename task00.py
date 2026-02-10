##
## EPITECH PROJECT, 2026
## day02
## File description:
## task00
##

def multiply(a:int | float, b:int | float):
    return a * b

def multiply2(x:int | float):
    return x * 2

def multiply10(x:int | float):
    return x * 10

def getSecondMax(numbers:list[int | float]):
    max = numbers[0]
    second_max:int | float

    if not numbers:
        raise ValueError
    if all(x == numbers[0] for x in numbers):
        raise ValueError

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

print(f"{getSecondMax([])}")
