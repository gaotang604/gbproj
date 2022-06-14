# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.
print([element for element in range(20, 241, 1) if (element % 20 == 0) or (element % 21 == 0)])
# range upper limit is 241 so that 240 will be in range as it requested
