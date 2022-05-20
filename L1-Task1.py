# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные,
# затем выведите на экран.
value_one = 700
value_two = 350
ops_result = value_one / value_two
print('Результат =', ops_result)

some_string = input('Введите строку: ')
some_integer = int(input('Введите целое число: '))
print('Строка:', some_string)
print('Число:', some_integer)
print('Строка: %s и Число(hex): %x' % (some_string, some_integer))
