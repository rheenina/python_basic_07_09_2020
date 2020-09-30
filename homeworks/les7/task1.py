"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
from typing import List
from copy import deepcopy


class Matrix:

    def __init__(self, matrix: List[List[int]]):
        self.__matrix = deepcopy(matrix)
        self.__size = (len(max(self.__matrix, key=len)), len(self.__matrix))

    def __str__(self):
        result = ''
        for row in self.__matrix:
            result += ''.join([f'{itm:4d}' for itm in row]) + '\n'
        return result

    def __add__(self, other: "Matrix"):
        if not isinstance(other, Matrix):
            raise TypeError(f'{other} is not a matrix!')
        if self.__size != other.__size:
            raise ValueError('Matrix 1 is not equal to matrix 2 by its size.')

        result = []
        for sublist in zip(self.__matrix, other.__matrix):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            result.append(temp)
        return Matrix(result)


if __name__ == '__main__':
    m1 = Matrix([[1, 2, 3], [10, 11, 12], [6, 8, 3]])
    m2 = Matrix([[7, 8, 9], [10, 11, 12], [1, 5, 9]])
    m3 = m1 + m2
    print(m3)