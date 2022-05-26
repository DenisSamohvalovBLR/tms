# Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}". Создать список из 5 имен.
# Вызвать функцию для каждого элемента списка в цикле.

def func():
    print(f"Hello, {name}")


name_list = {'Den', 'Dima', 'Max', 'Andrey', 'Sergey'}
for name in name_list:
    func()
