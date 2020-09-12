# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.

product_template = {
    'name': 'Enter a name of product:',
    'price': 'Enter a price of product',
    'amount': 'Enter amount of products',
    'pieces': 'Enter a unit of measure'
}


products_amount = int(input('How many products would you like to add?\n'))

i = 1
product = {}
product_list = []
analytics = {
    'name': [],
    'price': [],
    'amount': [],
    'pieces': []
}

while i <= products_amount:
    for key, ask in product_template.items():
        product[key] = input(ask + '\n')
    product_list.append((i, product))
    for p in product.keys():
        analytics[p].append(product[p])
    product = {}
    i += 1

print(f'{product_list}\n{analytics}')