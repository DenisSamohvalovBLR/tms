# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент func_type.
# В зависимости от func_type вернуть минимальное либо максимальное значение. Написать программу в виде трех функций.

def func(*args, func_type):
    if func_type == 'min':
        return func_min(args)
    elif func_type == 'max':
        return func_max(args)


def func_min(*args):
    return min(*args)


def func_max(*args):
    return max(*args)
