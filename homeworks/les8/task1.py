"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год».

В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число».

Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.

"""


class Date:

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def reformat_date(cls, date: str):
        try:
            day, month, year = map(int, date.split('-'))
            return f'Day: {day}, Month: {month}, Year: {year}'
        except ValueError:
            return 'Inappropriate date format'

    @staticmethod
    def validation(day, month, year):
        if day not in range(1, 32) or month not in range(1, 13) or year > 2020:
            raise ValueError('Date is incorrect')
        return 'Date is correct.'


if __name__ == '__main__':
    print(Date.reformat_date('10-12-2013'))
    print(Date.validation(10, 10, 2013))
