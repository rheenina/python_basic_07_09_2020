# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

new_list = [1, (3, 4, 5), 'hello', [8, 9], {1, 5}, '99', 2.65]

for i in range(len(new_list)):
    print(type(new_list[i]))
