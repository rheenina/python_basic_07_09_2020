# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Solution using dict

season = {
    '1': 'January is a winter month',
    '2': 'February is a winter month',
    '3': 'March is a spring month',
    '4': 'April is a spring month',
    '5': 'May is a spring month',
    '6': 'June is a summer month',
    '7': 'July is a summer month',
    '8': 'August is a summer month',
    '9': 'September is an autumn month',
    '10': 'October is an autumn month',
    '11': 'November is an autumn month',
    '12': 'December is a winter month'
}

user_number = input("Enter a number from 1 to 12: ")

if user_number.isdigit() and 12 >= int(user_number) >= 1:
    print(season.get(user_number))
else:
    print('Enter a number from 1 to 12!')
