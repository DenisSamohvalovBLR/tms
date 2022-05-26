# Написать функцию, которая используя модуль requests скачивает файл сохраняет его на файловой системе, функция имеет
# два параметра: ссылка на файл и имя на файловой системе. В качестве примера ссылки на файл можно использовать
# лицензию из ГитХаба из вашего репозитория.

import requests

url = 'https://raw.githubusercontent.com/DenisSamohvalovBLR/tms/master/LICENSE'


def func(url):
    response = requests.get(url)
    open('LICENSE', 'wb').write(response.content)


func(url)
