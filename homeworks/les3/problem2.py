"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_info(**kwargs) -> str:

    name = kwargs.get('name', '')
    surname = kwargs.get('surname', '')
    birth_year = kwargs.get('birth_year', '')
    city = kwargs.get('city', '')
    email = kwargs.get('email', '')
    phone = kwargs.get('phone', '')

    return f"{name} {surname} was born in {birth_year} in {city}. Contacts: {email}, {phone}"
