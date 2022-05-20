# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
input_value = int(input('Введите целое положительное число (в десятичной СИ ;-) '))
max_value = input_value % 10
new_value = 0
while input_value > 0:
    input_value //= 10
    new_value = input_value % 10
    if new_value > max_value:
        max_value = new_value
print('Наибольшая цифра: ', max_value)