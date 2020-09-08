#4.	Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

number = input("Enter a number ")
numbers = []
i = 0

if number.isdigit():
    while i != len(number):
        numbers.append(number[i])
        i += 1
    print(max(numbers))
else:
    print("You've entered not a number!")


