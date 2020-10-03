# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


try:
    n = int(input("Enter a number "))

    # counting number of digits in n
    count = len(str(n))

    # formulas for getting nn and nnn by multiplying n
    nn = 10 ** count + 1
    nnn = (10 ** (count * 2)) + nn

    result = n + (n*nn) + (n*nnn)
    print(result)
except ValueError:
    print("You've entered not a number!")
