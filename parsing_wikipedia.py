import requests
from bs4 import BeautifulSoup
import lxml  # pip install lxml

resp = requests.get('https://wikipedia.org/')  # запрашиваем гл. стр. вики
html = resp.text  # сохраняем страницу в переменной

# print(html)  # test1

soup = BeautifulSoup(html, 'lxml')  # распарсиваем страницу в переменную
# print(soup)  # test2
tags = soup('a', 'other-project-link')  # сохраняем в переменную содержимое тегов

print([teg['href'] for teg in tags])  # перебираем содержимое, т.е. то, что в href
