"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


def salary_count(some_file):
    with open(some_file, 'r', encoding='utf-8') as file:
        i = 0
        average = 0

        # reading lines from the file, splitting to names and salary
        for line in file:
            employees = line.split()
            name = employees[0]

            salary = float(employees[1])

            # calculating salary of all employees
            average += salary
            i += 1

            # searching for employees whose salary is less than 20K
            if salary < 20000:
                print(name)

        # calculating average salary for each employee
        return round((average / i), 2)


if __name__ == '__main__':
    try:
        salary_list = 'salary.txt'
        print(salary_count(salary_list))
    except ValueError:
        print('Must be a number for salary in the second column of file.')