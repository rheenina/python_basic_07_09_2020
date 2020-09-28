"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.

Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего
дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _length = 0
    _width = 0
    _mass = 25

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def calculating(self, thickness=5):
        # Returns a number in tonnes
        return (self._length * self._width * self._mass * thickness) / 1000


if __name__ == '__main__':
    rd = Road(20, 5000)
    print(rd.calculating())