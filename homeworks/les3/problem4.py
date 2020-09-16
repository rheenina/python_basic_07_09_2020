"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

# Variant 1, using **

def my_func(x, y):
    result = x ** y
    return result

# Variant 2, using loop

def my_func2(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res

try:
    x = float(input('Enter a float number: '))
    y = int(input('Enter a negative integer number: '))
    print(my_func(x, y), my_func2(x, y)) if y < 0 else print('Second number should be negative!')
except ValueError:
    print('Enter only numbers!')