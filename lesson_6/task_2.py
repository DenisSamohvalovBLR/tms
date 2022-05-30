# Доработать первое задание так, чтобы словарь читался из текстового CSV файла, где на каждой строке пары слов вида:
# apple,яблоко.

import csv


def eng(word):
    return my_dict[word]


def ru(word):
    for key, value in my_dict.items():
        if value == word:
            return key


def load_dict():
    result = {}
    with open('my_dict.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            result[row[0]] = row[1]
    return result


my_dict = load_dict()
