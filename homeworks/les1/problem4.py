#4.	Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

try:
    number = int(input("Enter a number "))
    max_number = -1
    if number > 0:
        while number > 0:
            tmp = number % 10
            number //= 10
            if tmp > max_number:
                max_number = tmp
        print(max_number)
    else:
        print("Enter a positive number!")
except ValueError:
    print("You've entered not a number!")


