# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчёте на одного сотрудника.
revenue = int(input('Введите выручку: '))
expenses = int(input('Введите издержки: '))
net_income = revenue - expenses
if net_income:
    print('Фирма прибыльная')
elif net_income < 0:
    print('Фирма убыточная')
else:
    print('Фирма на самоокупаемости')
print('Рентабельность (процент): %.2f' % (net_income/revenue * 100))
staff_count = int(input('Введите кол-во сотрудников: '))
print('В расчете на одного сотрудника (процент): %.2f' % ((net_income / revenue * 100) / staff_count))