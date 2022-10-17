"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
import os
from time import sleep
import curses


def clear_screen():
    os.system('cls' if os == 'nt' else 'clear')


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'\033[34m {self.title} рисует синим!')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'\033[30m {self.title} рисует серым!')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'\033[35m {self.title} рисует фиолетовым!')


p1 = Pen('Карандаш')
p2 = Pencil('Ручка')
h1 = Handle('Маркер')

stdscr = curses.initscr()
curses.curs_set(0)
my_list = [p1, p2, h1]
for i in my_list:
    clear_screen()
    i.draw()
    sleep(2)
clear_screen()
curses.curs_set(1)
