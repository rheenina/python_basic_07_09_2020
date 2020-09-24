"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""


def counting(file_name):

    with open(file_name, 'r') as file:
        string = 0

        # counting strings and words for each string
        for line in file:
            string += 1
            words = line.split()
            word = len(words)
            print(string, word)


if __name__ == '__main__':
    some_file = 'test.txt'
    counting(some_file)