"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами.

"""
from sys import argv

_, hours, hour_pay, bonus = argv


def salary(hours: float, hour_pay: float, bonus: float):
    # Calculating month salary with bonus
    month_salary = hours * hour_pay + bonus
    return f"Salary is {month_salary}."


try:
    employee_salary = salary(float(hours), float(hour_pay), float(bonus))
    print(employee_salary)
except ValueError:
    print("Enter only numbers to calculate a salary!")
