# Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ, из этих чисел составляется
# первый список. Далее таким же образом вводятся второй и третий списки. Вывести на экран список, элементы которого
# есть в первых двух списках, но отсутствуют в третьем.

my_list = [], [], []
for el in range(0, 3):
    print("Список #" + str(el + 1))
    while True:
        n = input("Введите любое число: ")
        try:
            num = int(n)
        except ValueError:
            break
        my_list[el].append(n)
print([el for el in my_list[0] if el in my_list[1] if el not in my_list[2]])
