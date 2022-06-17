# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
numerals = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
try:
    with open('task_4.txt') as src_file:
        with open('task_4_OUT.txt', 'w', encoding='UTF8') as dst_file:
            while True:
                src_line = src_file.readline()
                if len(src_line.strip()) != 0:
                    a_key = src_line.split()[0].strip()
                    a_val = src_line.split()[2].strip()
                    print(f'{a_key} - {a_val} >>> {numerals[a_key]} - {a_val}')
                    dst_file.write(numerals[a_key] + ' - ' + a_val + '\n')
                    continue
                break
except IOError:
    print('Ошибка чтения файла')
