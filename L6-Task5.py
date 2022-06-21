# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationary():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title} Запуск отрисовки')

class Pen(Stationary):
    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print(f'{self.title} пишет тонко')

class Pencil(Stationary):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print(f'{self.title} пишет изящно')

class Handle(Stationary):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print(f'{self.title} пишет сочно')

stationary = Stationary('Скрепка')
stationary.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
