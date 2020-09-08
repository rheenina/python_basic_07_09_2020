#3.	Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

try:
    n = input("Enter a number ")
    nn = n + n
    nnn = nn + n
    numbers = [n, nn, nnn]
    numbers = [int(n) for n in numbers]
    result = numbers[0] + numbers[1] + numbers[2]
    print(result)
except ValueError:
    print("You've entered not a number!")
