# 7. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит
# не менее b километров. Программа должна принимать
# значения параметров a и b и выводить одно натуральное число — номер дня.
a = float(input('Введите а: '))
b = float(input('Введите b: '))
d = 1
while b > a:
    a *= 1.1
    d += 1
print('Номер дня:', d)
