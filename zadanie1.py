#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    letters = {'а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё'}
    string = list(input('Введите строку: ').lower())

    count = 0
    for i, slovo in enumerate(string):
        if slovo in letters:
            count += 1
    print(count)