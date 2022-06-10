# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться
# к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.
def add_numbers(input_str):
    sum_value = 0
    value_list = str(input_str).split()
    for a_value in value_list:
        if a_value == 'N':
            return False, sum_value
        try:
            sum_value += int(a_value)
        except ValueError:
            print('Ошибка в значении "', a_value, '"')
    return True, sum_value


sum_value = 0
while True:
    do_continue, s = add_numbers(input('Введите числа через пробел, или "N" для выхода: '))
    sum_value += s
    print('Сумма = ', sum_value)
    if not do_continue:
        break
print('Bye bye!')
