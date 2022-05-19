# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
input_value = int(input('Введите время в секундах: '))
seconds_value = input_value % 60
minute_value = (input_value // 60) % 60
hour_value = input_value // (60 * 60)
print(f'Форматированное время: {hour_value:02d}:{minute_value:02d}:{seconds_value:02d}')
