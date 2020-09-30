"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.

К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Cloth:

    @property
    @abstractmethod
    def fabric_usage(self):
        pass

    @property
    @abstractmethod
    def measures(self):
        pass


class Coat(Cloth):

    def __init__(self, name, size: float):
        self.name = name
        self.size = size

    @property
    def fabric_usage(self):
        return self.size / 6.5 + 0.5

    @property
    def measures(self):
        return self.size


class Suit(Cloth):

    def __init__(self, name, height: float):
        self.name = name
        self.height = height

    @property
    def fabric_usage(self):
        return self.height * 2 + 0.3

    @property
    def measures(self):
        return self.height


if __name__ == '__main__':
    coat = Coat('black coat', 44)
    print(coat.fabric_usage)
    suit = Suit('black suit', 166)
    print(suit.fabric_usage)