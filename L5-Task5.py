# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран
from random import randint

a_list = [randint(10, 100) for _ in range(1, 21)]
with open('task_5.txt', 'w') as a_file:
    for value in a_list:
        a_file.write(str(value) + ' ')

with open('task_5.txt') as a_file:
    a_line = a_file.readline()
    print('Значения: ', a_line)
    a_list.clear()
    for value in a_line.split():
        a_list.append(int(value))
    print(f'Сумма: {sum(a_list)}')
