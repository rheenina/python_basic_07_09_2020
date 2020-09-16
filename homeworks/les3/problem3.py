"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    result = a + b + c - min(a, b, c)
    return result


try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    print(my_func(a, b, c))
except ValueError:
    print("Enter only numbers!")