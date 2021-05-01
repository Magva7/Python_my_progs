import requests

# appid = "2745926c9f2ffb7903aec82510e1bc65"  # мой id
result = requests.get('https://api.openweathermap.org/data/2.5/weather?id=524901&appid=2745926c9f2ffb7903aec82510e1bc65&lang=RU')
# отправляем запрос и записываем ответ от сервера в переменную
# print(result.text)  # тестовый вывод - смотрим, что нам вернул сайт
data = result.json()  # Разбираем пакет JSON, который получили - получаем
# нужные значения по названиям полей
vidimost = data['weather'][0]['description']
print("видимость:", vidimost)

# print(result.text)