"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

# importing a function from 1st task to create a file
from homeworks.les5.task1 import create_file
from random import randint


def write_random_nums(name):

    # writing down random integer numbers to a file
    with open(name, 'w') as f:
        numbers = [randint(1, 100) for _ in range(1, 50)]
        f.write(' '.join(map(str, numbers)))


def my_sum(name):

    # calculating the sum of numbers in file
    with open(name, 'r') as f:
        numbers = list(map(int, f.read().split(' ')))
        return sum(numbers)


if __name__ == '__main__':
    some_file = create_file()
    write_random_nums(some_file)
    print(my_sum(some_file))
