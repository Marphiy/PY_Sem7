"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

from curses.ascii import isdigit
from time import sleep
import os


def clear_screen():
    os.system('cls' if os == 'nt' else 'clear')


class Car:
    max_speed = 40

    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def __str__(self):
        if not self.is_police:
            civ = 'Гражданский'
        else:
            civ = 'Полиция'
        return f'{self.name}, {self.colour}, {civ}, Макс. разр. скорость {self.max_speed}'

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')
        sleep(2)

    def turn(self, direction):
        if direction == 'l':
            print('Поворот налево')
        elif direction == 'r':
            print('Поворот направо')
        else:
            print('Команда не распознанна!')

    def show_speed(self):
        if self.speed >= self.max_speed:
            print(f'Внимание, Ваша скорость {self.speed}км/ч при разрешенной {self.max_speed}'
                  f'км/ч!\nCбавьте скорость!')
        else:
            print(f'Скорость = {self.speed}км/ч')


class TownCar(Car):
    max_speed = 60

    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)
        self.is_police = is_police


class SportCar(Car):
    max_speed = 120

    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)
        self.is_police = is_police


class WorkCar(Car):
    max_speed = 40

    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)
        self.is_police = is_police


class PoliceCar(Car):
    max_speed = 300

    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)
        self.is_police = is_police


t_c = TownCar(5, 'Синий', 'Lada')
s_c = SportCar(5, 'Белый', 'Porche')
w_c = WorkCar(5, 'Красный', 'Fiat')
p_c = PoliceCar(5, 'Черный', 'Ford', True)
while True:
    clear_screen()
    print(f'Выберите транспортное средство:\n'
          f'1: {t_c}\n'
          f'2: {s_c}\n'
          f'3: {w_c}\n'
          f'4: {p_c}\n')
    selected = input()
    if selected == '1':
        transport = t_c
        break
    elif selected == '2':
        transport = s_c
        break
    elif selected == '3':
        transport = w_c
        break
    elif selected == '4':
        transport = p_c
        break
    else:
        print('Ввод неверен!')
        sleep(2)

clear_screen()
new_speed = transport.speed
key_pressed = str()
print(transport)
print('Для выхода сброcьте скорость до 0!')
input('Нажмите "Enter" для начала движения!')
transport.go()
sleep(2)
while new_speed > 0:
    clear_screen()
    transport.show_speed()
    key_pressed = input('Введите новое значение скорости или маневра (l/r): ')
    if key_pressed.isdigit():
        new_speed = int(key_pressed)
        transport.speed = new_speed
    else:
        turn_to = key_pressed
        transport.turn(turn_to)
        sleep(2)
clear_screen()
transport.stop()
