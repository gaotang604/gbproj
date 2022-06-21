# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
class Car():
    def __init__(self, color, name, is_police=False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0

    def go(self, speed):
        self.speed = speed
        print(f'Машина {self.name} тронулась')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.name} ПРЕВЫШЕНА, {self.speed} км/ч')
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость {self.name} ПРЕВЫШЕНА, {self.speed} км/ч')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


car = Car('белый', 'трабант')
print(f'Машина {car.name}, цвет {car.color}, копы(?) {car.is_police}')
car.go(100)
car.show_speed()
car.turn('налево')
car.stop()

town_car = TownCar('синий', 'додж')
print(f'Машина {town_car.name}, цвет {town_car.color}, копы(?) {town_car.is_police}')
town_car.go(30)
town_car.show_speed()
town_car.go(70)
town_car.show_speed()
town_car.stop()

sport_car = SportCar('красный', 'зондо')
print(f'Машина {sport_car.name}, цвет {sport_car.color}, копы(?) {sport_car.is_police}')
sport_car.go(30)
sport_car.show_speed()
sport_car.go(100)
sport_car.show_speed()

work_car = WorkCar('зелёный', 'фолькстваген')
print(f'Машина {work_car.name}, цвет {work_car.color}, копы(?) {work_car.is_police}')
work_car.go(30)
work_car.show_speed()
work_car.go(70)
work_car.show_speed()
work_car.stop()

cop_car = PoliceCar('сине-белый', 'лада')
print(f'Машина {cop_car.name}, цвет {cop_car.color}, копы(?) {cop_car.is_police}')
cop_car.go(30)
cop_car.show_speed()
cop_car.go(100)
cop_car.show_speed()
