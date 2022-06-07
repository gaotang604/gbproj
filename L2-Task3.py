# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict
seasons_monthly_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето',
                        'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
seasons_dic = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето',
               7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
given_month = int(input('Введите номер месяца от 1 до 12 : '))
if 0 < given_month < 13:
    print('На основе списка: ', seasons_monthly_list[given_month - 1])
    print('На основе словаря: ', seasons_dic[given_month])
else:
    print('Ошибка ввода')
