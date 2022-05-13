# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while.

n = int(input("Введите любое число от 1: "))

counter = 0
my_sum = 0
while counter <= n:
    my_cube = counter ** 3
    my_sum = my_sum + my_cube
    counter += 1
print(my_sum)

# or:
print(sum([el ** 3 for el in range(1, n + 1)]))
