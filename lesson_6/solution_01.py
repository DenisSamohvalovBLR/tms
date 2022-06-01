# Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.

from collections import Counter
import re


def func(text):
    string = re.sub(r'[^\w\s]', '', text.lower()).split()
    return max(string, key=len), Counter(string).most_common()[0]
