"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time
import os


def clear_screen():
    os.system('cls' if os == 'nt' else 'clear')


def task_1():

    class TrafficLight:

        def __init__(self):
            self.__colour = None

        def running(self):
            colours = {'31m': 7, '33m': 2, '32m': 4}
            text_colour = '[31m'
            for k in colours.keys():
                for i in range(1, colours[k] + 1):
                    clear_screen()
                    self.colour = k
                    print(
                        f'\033[{self.colour}СИГНАЛ СВЕТОФОРА       \033[37m{i}сек')
                    time.sleep(1)
            clear_screen()

    t = TrafficLight()
    t.running()


task_1()
