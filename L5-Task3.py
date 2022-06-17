# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
try:
    with open('task_3.txt', 'r', ) as a_file:
        emp_count = 0
        employees = []
        ttl_salary = 0.0
        while True:
            a_line = a_file.readline()
            if len(a_line.strip()) != 0:
                a_surname = a_line.split()[0]
                a_salary = float(a_line.split()[1])
                print(f'{a_surname} {a_salary}')
                if a_salary < 20000.00:
                    employees.append(a_surname)
                ttl_salary += a_salary
                emp_count += 1
                continue
            break
        if emp_count > 0:
            print(f'Средняя зарплата {ttl_salary/emp_count}')
            print(f'Наши беднейшие сотрудники {employees}')
except IOError:
    print('Ошибка чтения файла')
