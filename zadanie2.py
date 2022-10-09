#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")
    # Преобразуем строки в множества
    first = set(string1)
    second = set(string2)

    # Нахождение общих символов
    a = first.intersection(second)
    print("Общие символы: ", a)