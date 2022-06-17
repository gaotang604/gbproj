# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
try:
    with open('task_2.txt') as a_file:
        a_line_num = 1
        a_content = a_file.readlines()
        print(f'Содержимое файла: {a_content}')
        print('Строк в файле: ', len(a_content))
        for a_line in a_content:
            print(f'Строка {a_line_num} слов {len(a_line.split())}')
            a_line_num += 1
except IOError:
    print('Ошибка чтения файла')
