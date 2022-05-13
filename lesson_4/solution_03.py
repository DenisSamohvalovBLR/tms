# Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
# которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
# Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.

string = input('Введите слово для шифрования: ')
key = input('Введите ключ шифрования: ')

# Переводим ключ в число:
key_bin = 0
for el in key:
    key_bin += ord(el)


def xor_cipher(string, key_bin):
    cipher = ''
    for el in string:
        cipher += chr(ord(el) ^ key_bin)
        print(cipher)
    return cipher


def xor_uncipher(x, key_bin):
    uncipher = ''
    for el in x:
        uncipher += chr(ord(el) ^ key_bin)
    return uncipher
