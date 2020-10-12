# 6 Например: a = 2, b = 3. Результат: 1-й день: 2 2-й день: 2,2
# 3-й день: 2,42 4-й день: 2,66 5-й день: 2,93 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

try:
    first_distance = float(input("Enter a first day distance "))
    wanted_distance = float(input("Enter a distance to achieve "))
    days = 1

    # Counting days to achieve wanted distance
    while first_distance < wanted_distance:
        daily_result = first_distance / 10
        first_distance += daily_result
        days += 1

    print(f"You will achieve no less than {wanted_distance} km in {days} days")

except ValueError:
    print("Enter a distance using numbers!")
