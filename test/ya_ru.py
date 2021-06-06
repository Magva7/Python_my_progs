import requests

res = requests.get('https://ya.ru')
page = res.text
print(page)