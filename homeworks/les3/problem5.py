"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.

Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.

Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале
нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


numbers = input('enter some numbers with space or "q" to exit: ').split()
result = 0


try:
    while numbers != ['q']:
        if 'q' in numbers:
            numbers.remove('q')
            numbers = map(int, numbers)
            result = result + sum(numbers)
            print(f"Result is {result}.")
            break
        else:
            numbers = map(int, numbers)
            result = result + sum(numbers)
            print(f"Result is {result}.")
            numbers = input('enter some numbers or "q" to exit: ').split()
except ValueError:
    print("Enter only numbers or 'q', use space between them.")
