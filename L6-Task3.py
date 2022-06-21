# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker():
    def __init__(self, name, surname, position, income = {'wage': 0, 'bonus': 0}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.position

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

worker1 = Worker('Иван', 'Иванов', 'Хороший человек', {'wage': 100000, 'bonus': 20000})
position1 = Position('Петр', 'Петров', 'Директор', {'wage': 150000, 'bonus': 50000})
print(worker1.name, worker1.surname, worker1.position)
print(position1.get_full_name(), position1.get_total_income())
