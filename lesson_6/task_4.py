# Использую функцию из предыдущей задачи, написать программу игру Блэкджек, т.е. реализовать цикл в котором на каждом
# ходу у игрока спрашивается, достать ли следующую карту, в случае положительного ответа  - вытягивать случайную карту.
# Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.

import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(cards)

i = 0

while True:
    choice = input('Take a card? y/n\n')
    if choice == 'y':
        current = cards.pop()
        print('You got a card of %d' % current)
        i += current
        if i > 21:
            print('You lose.')
            break
        elif i == 21:
            print('You win!')
            break
        else:
            print('Your %d points.' % i)
    elif choice == 'n':
        print('Your %d points. Finish.' % i)
        break
print('Bye!')
