"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

tmp_dict = {}

with open('task6.txt', 'r', encoding='utf-8') as f:

    # creating a temporary dictionary
    for line in f:
        tmp = line.split(' ')
        lesson = tmp[0].replace(':', '')
        tmp_dict[lesson] = tmp[1:]

# calculating total number of lessons for each subject, making the final dictionary
schedule = {}
for key, value in tmp_dict.items():
    schedule[key] = sum([int(itm.split('(')[0]) for itm in value if itm.split('(')[0].isdigit()])

print(schedule)
