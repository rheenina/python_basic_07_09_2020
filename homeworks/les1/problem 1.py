#1.	Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.
a = 46
user_name = input("Enter your name ")
user_surname = input("Enter your surname ")

try:
    user_age = int(input("Enter your age "))
    result_age = a + user_age
    print(f"Hello, {user_surname} {user_name}! You're {user_age} years old. You will turn {result_age} in 46 years.")
except ValueError:
    print("Enter your age using numbers!")
finally:
    print('Come back again!')