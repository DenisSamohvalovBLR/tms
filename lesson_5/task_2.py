# Создать функцию, которая принимает на вход неопределенное количество аргументов и возвращает их сумму и максимальное
# из них.

def func(*args):
    my_sum = 0
    for el in args:
        my_sum += el
    return my_sum, max(*args)
