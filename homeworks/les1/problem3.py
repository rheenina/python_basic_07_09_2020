#3.	Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

try:
    n = int(input("Enter a number "))
    nn = n * 11
    nnn = nn * 10 + n
    result = n + nn + nnn
    print(result)
except ValueError:
    print("You've entered not a number!")
