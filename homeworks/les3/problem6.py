"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

user_text = input("Enter something using lower case: ")


def int_func(text: str):
    # Returns first letter of the first word in upper case
    return ''.join((text[0].upper(), text[1:]))


def int_func2(text: str):
    # Returns first letter of every word in upper case
    return text.title()


print(int_func(user_text))
print(int_func2(user_text))
