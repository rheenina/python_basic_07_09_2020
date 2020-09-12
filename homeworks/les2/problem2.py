# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

new_list = input("Enter a sequence of something using comma\n").split()
x = 0

for i in range(int(len(new_list) / 2)):
    new_list[x], new_list[x + 1] = new_list[x + 1], new_list[x]
    x += 2
print(new_list)