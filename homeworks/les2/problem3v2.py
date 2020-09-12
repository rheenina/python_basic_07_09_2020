# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Solution using list

try:
    user_number = int(input('Enter a number from 1 to 12: '))
    season = [0, 'winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'fall', 'fall', 'fall', 'winter']
    print(season[user_number])
except IndexError:
    print('Enter a number from 1 to 12!')
except ValueError:
    print('Enter a number from 1 to 12!')