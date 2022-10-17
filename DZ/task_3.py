"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
import os
from time import sleep


def clear_screen():
    os.system('cls' if os == 'nt' else 'clear')


class Worker:

    def __init__(self, name, surname, position, income={}):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

    def __str__(self):
        return f'{self.name} {self.surname}: {self.position}'


class Position(Worker):
    def __init__(self, name, surname, position, income={}):
        super().__init__(name, surname, position, income)
        if self.position.lower() == 'каменщик':
            self.__income = {'wage': 60000, 'bonus': 10000}
        elif self.position.lower() == 'уборщик':
            self.__income = {'wage': 20000, 'bonus': 4000}
        elif self.position.lower() == 'сварщик':
            self.__income = {'wage': 40000, 'bonus': 7000}

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.__income['wage'] + self.__income['bonus']


clear_screen()
p_1 = Position('Марк', 'Подгорный', 'Каменщик')
print(f'Имя сотрудника: {p_1.name}\n'
      f'Фамилия сотрудника: {p_1.surname}\n'
      f'Должность сотрудника: {p_1.position}')
print(f'{p_1.income}')
print(p_1)
print(
    f'Сотрудник: {p_1.get_full_name()}. Заработная плата: {p_1.get_total_income()}р. в месяц.')

sleep(8)
clear_screen()
p_2 = Position('Егор', 'Носков', 'Сварщик')
print(f'Имя сотрудника: {p_2.name}\n'
      f'Фамилия сотрудника: {p_2.surname}\n'
      f'Должность сотрудника: {p_2.position}')
print(f'{p_2.income}')
print(p_2)
print(
    f'Сотрудник: {p_2.get_full_name()}. Заработная плата: {p_2.get_total_income()}р. в месяц.')

sleep(10)
clear_screen()
p_3 = Position('Анастасия', 'Заправская', 'Уборщик')
print(f'Имя сотрудника: {p_3.name}\n'
      f'Фамилия сотрудника: {p_3.surname}\n'
      f'Должность сотрудника: {p_3.position}')
print(f'{p_3.income}')
print(p_3)
print(
    f'Сотрудник: {p_3.get_full_name()}. Заработная плата: {p_3.get_total_income()}р. в месяц.')
