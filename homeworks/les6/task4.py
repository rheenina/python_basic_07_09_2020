"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from random import randint


class Car:
    speed = 0
    is_police = False

    def __init__(self, name, color, is_police: bool):
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        print('Auto starts moving')
        self.speed = randint(5, 220)

    def stop(self):
        self.speed = 0
        print('Auto stopped')

    def turn(self, direction):
        print(f"Turning {direction}.")

    def show_speed(self):
        print(f'Auto speed is {self.speed} km/h.')
        if self.speed > 120 and self.is_police == False:
            print('Speed limit is 120.')
            self.speed = randint(50, 120)


class TownCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        print(f'Auto speed is {self.speed} km/h.')
        if self.speed > 60:
            print('Speed limit is 60.')
            self.speed = randint(20, 60)


class SportCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        print(f'Auto speed is {self.speed} km/h.')
        if self.speed > 120:
            print('Speed limit is 120.')
            self.speed = randint(120, 250)


class WorkCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        print(f'Auto speed is {self.speed} km/h.')
        if self.speed > 40:
            print('Speed limit is 40.')
            self.speed = randint(20, 40)


class PoliceCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color, True)


if __name__ == '__main__':
    car1 = Car('Lexus', 'black', False)
    car2 = TownCar('Mazda', 'blue')
    car3 = WorkCar('Kia', 'red')
    car4 = SportCar('Ferrari', 'red')
    car5 = PoliceCar('Skoda', 'white')

    print(car1.name, car1.is_police, car1.speed, car1.color, sep=', ')
    car1.go()
    car1.show_speed()
    car1.show_speed()
    car1.turn('left')
    car1.turn('right')
    car1.stop()

    print(car2.name, car2.is_police, car2.speed, car2.color, sep=', ')
    car2.go()
    car2.show_speed()
    car2.show_speed()
    car2.turn('left')
    car2.turn('right')
    car2.stop()