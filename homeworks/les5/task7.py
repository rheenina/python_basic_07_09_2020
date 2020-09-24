"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json


def income_outcome(name) -> list:
    with open(name, 'r', encoding='utf-8') as f:
        profit = {}
        deficit = {}
        average = {}

        # i for counting profitable firms, a for counting profit of profitable firms
        i = 1
        a = 0

        for line in f:
            line = line.split()
            tmp = round(float(line[2]) - float(line[3]), 2)

            # profit and average profit
            if tmp > 0:
                tmp_dict = {line[0]: tmp}
                profit.update(tmp_dict)

                a += tmp
                average_profit = round((a / i), 2)
                average = {'average': average_profit}
                average.update(average)
                i += 1

            # deficit
            else:
                tmp_dict = {line[0]: tmp}
                deficit.update(tmp_dict)

        return [profit, average, deficit]


def dumping(name):
    with open('task7.json', 'w', encoding='utf-8') as f:
        json.dump(income_outcome(name), f)


if __name__ == '__main__':
    firms = 'task7.txt'
    dumping(firms)
