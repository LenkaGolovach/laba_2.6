#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import datetime

if __name__ == '__main__':
    print("help - список всех команд")
    # Список людей.
    humans = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            surname = input("Фамилия: ")
            name = input("Имя: ")
            zodiak = input("Знак Зодиака: ")
            date_str = input("Введите дату выпуска (dd/mm/yyyy)\n")
            date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()

            # Создать словарь.
            human = {
                'surname': surname,
                'name': name,
                'zodiak': zodiak,
                'date': date
            }

            # Добавить словарь в список.
            humans.append(human)
            # Отсортировать список в случае необходимости.
            if len(humans) > 1:
                humans.sort(key=lambda item: item.get('d.m', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Фамилия и имя",
                    "Знак Зодиака",
                    "Дата рождения"
                )
            )
            print(line)

            # Вывести данные о всех сотрудниках.
            for idx, worker in enumerate(humans, 1):
                date = worker.get('date', '')
                print(
                    '| {:^4} | {:<14} {:<15} | {:<20} | {}{} |'.format(
                        idx,
                        worker.get('surname', ''),
                        worker.get('name', ''),
                        worker.get('zodiak', ''),
                        date,
                        ' ' * 5
                    )
                )

            print(line)

        elif command.startswith('select '):
            # Получить введенный месяц
            month = month(input())

            # Инициализировать счетчик.
            count = 0
            # Проверить сведения работников из списка.
            for human in humans:
                if human.get('month', '') == month:
                    count += 1
                    print(
                        '{:>4}: {} {}'.format(
                            count, human.get('surname', ''),
                            human.get('name', '')
                        )
                    )

            # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("Люди с таким ЗЗ не найдены.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("help - список всех команд;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
