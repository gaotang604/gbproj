# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
items = []
item_id = 1
while True:
    item_name = input('Введите название: ')
    item_price = float(input('Введите цену: '))
    item_amount = int(input('Введите количество: '))
    item_units = input('Введите единицу измерения: ')
    items.append((item_id, {'Название': item_name, 'Цена': item_price, 'Кол-во': item_amount, 'Ед.изм': item_units}))
    item_id += 1
    if input('Что бы ввести ещё товар, введите "1" ') != '1':
        break
print('------------------------')
print(items)
print('------------------------')
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
items_analytics = {'Название': [], 'Цена': [], 'Кол-во': [], 'Ед.изм': []}
for current_item in items:
    if current_item[1]['Название'] not in items_analytics['Название']:
        items_analytics['Название'].append(current_item[1]['Название'])
    if current_item[1]['Цена'] not in items_analytics['Цена']:
        items_analytics['Цена'].append(current_item[1]['Цена'])
    if current_item[1]['Кол-во'] not in items_analytics['Кол-во']:
        items_analytics['Кол-во'].append(current_item[1]['Кол-во'])
    if current_item[1]['Ед.изм'] not in items_analytics['Ед.изм']:
        items_analytics['Ед.изм'].append(current_item[1]['Ед.изм'])
print(items_analytics)
