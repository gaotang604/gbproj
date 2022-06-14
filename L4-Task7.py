# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from itertools import count
from math import factorial


def factorial_gen():
    for item in count(1):
        yield factorial(item)


my_gen = factorial_gen()
cur_number = 1
for el in my_gen:
    print(f'Факториал {cur_number} равен {el}')
    cur_number += 1
    if cur_number > 7:
        break
