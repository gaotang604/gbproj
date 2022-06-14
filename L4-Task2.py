# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Исходный список ', source_list)
prev_element = None
cur_element = None
new_list = []
for cur_element in source_list:
    if prev_element != None:
        if int(cur_element) > int(prev_element):
            new_list.append(cur_element)
    prev_element = cur_element
print('Результирующий список ', new_list)
