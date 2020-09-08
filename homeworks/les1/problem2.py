#2.Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.
print("Hi! I'll help to convert seconds into hh:mm:ss time format.")

try:
    time_sec = int(input("Enter seconds "))
    hours = time_sec // 3600
    ms = time_sec - hours * 3600
    minutes = ms // 60
    seconds = ms - minutes * 60
    print(f"{time_sec} seconds are {hours}:{minutes}:{seconds}")
except ValueError:
    print("You've entered not a number! Please, try again and do not use any symbols.")

