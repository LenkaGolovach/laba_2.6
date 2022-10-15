# Использовать словарь, содержащий следующие ключи: фамилия, имя; знак Зодиака; дата
# рождения (массив из трех чисел). Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи
# должны быть упорядочены по знакам Зодиака; вывод на экран информации о людях,
# родившихся в месяц, значение которого введено с клавиатуры; если таких нет, выдать на
# дисплей соответствующее сообщение.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date

if __name__ == '__main__':
    #Список людей
    peoples = []

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            name = input("Фамилия и инициалы? ")
            zodiak = input("Знак зодиака? ")
            date = input("Дата рождения? ")

            people = {
                'name': name,
                'zodiak': zodiak,
                'date': date,
            }

            peoples.append(people)

            if len(peoples) > 1:
                peoples.sort(key=lambda item: item.get('zodiak', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Ф.И.О.",
                    "З. Зодиака",
                    "Год рождения"
                )
            )
            print(line)

            for idx, people in enumerate(peoples, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        people.get('name', ''),
                        people.get('zodiak', ''),
                        people.get('year', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):
            months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
                      7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
