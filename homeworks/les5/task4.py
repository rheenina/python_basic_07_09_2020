"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


numbers = {
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре'
}


def read_file(name):
    with open(name, 'r', encoding='UTF-8') as f:
        i = 1

        # reading lines from the file, substituting english words with russians
        for line in f:
            line = line.split()
            line[0] = numbers[i]
            i += 1

        # opening a 'new_numbers.txt' to write down a result or creating a new one if file doesn't exist
            with open('new_numbers.txt', 'a', encoding='utf-8') as new_file:
                print(' '.join(line), file=new_file)


if __name__ == '__main__':
    some_file = 'task4.txt'
    read_file(some_file)
