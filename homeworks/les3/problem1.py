"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_func(a, b):
    return a / b


try:
    a = int(input("Enter a divisor: "))
    b = int(input("Enter a divider: "))
    print(f"Result of division {a} by {b} is {division_func(a, b)}")
except ValueError:
    print("Use only numbers!")
except ZeroDivisionError:
    print("You can't divide by zero!")
