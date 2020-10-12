# 5.	Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

try:
    income = float(input("Enter an income of you business "))
    outcome = float(input("Enter an outcome of you business "))
    profit = income - outcome

    # checking if income more than outcome, if true calculating profit per an employee
    if income > outcome:
        employees = int(input("Enter a number of employees "))
        print(f"Your profit is {profit}\nProfit per an employee is {round(profit / employees, 2)}")

    # showing loses if outcome more than income
    else:
        print(f"Your business is not profitable. Your income is {profit}.")
except ValueError:
    print("You've entered not a number!")
