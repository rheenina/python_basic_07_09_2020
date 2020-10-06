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
            return day, month, year
        except ValueError:
            return 'Inappropriate date format'

    @staticmethod
    def validation(day: int, month: int, year: int):
        days_31 = [1, 3, 5, 7, 8, 10, 12]
        if month in days_31 and day not in range(1, 32):
            raise ValueError('Date is incorrect. Month has 31 days')

        elif month == 2:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                if day not in range(1, 30):
                    raise ValueError(f'Date is incorrect. February of {year} has 29 days.')
            elif day not in range(1, 29):
                raise ValueError(f'Date is incorrect. February of {year} has 28 days.')

        elif month not in days_31 and day not in range(1, 31):
            raise ValueError('Date is incorrect. Month has 30 days')

        return 'Date is correct.'


if __name__ == '__main__':
    print(Date.reformat_date('10-12-2013'))
    print(Date.validation(29, 2, 2012))
