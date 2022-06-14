# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

def calc_salary(output, rate, bonus):
    try:
        return int(output) * float(rate) + float(bonus)
    except ValueError:
        print(f'Ошибка в значениях {output} {rate} {bonus}')


output_param, rate_param, bonus_param = argv[1:]
print(f'Зарплата к оплате {calc_salary(output_param, rate_param, bonus_param)}')
