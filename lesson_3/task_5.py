# Найти в списке количество не уникальных элементов:

my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
my_list_1 = set(my_list)
print(len(my_list) - len(my_list_1))
