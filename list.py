#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {
        '1a': 15,
        '1b': 16,
        '6a': 17,
        '7B': 18
    }
    print("Начальный вид классов и учеников:", '\n', school)
    # Изменение в 1b классе
    school['6a'] = 24
    # Новый класс
    school['7a'] = 19
    # Класс был расформирован
    del school['1b']
    S = sum(school.values())
    print('\n', school, '\n', "Общее количество учеников в школе :", S)