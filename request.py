import requests

# appid = "2745926c9f2ffb7903aec82510e1bc65"  # мой id

# отправляем запрос и записываем ответ от сервера в переменную, там данные по погоде на сейчас
res = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=2745926c9f2ffb7903aec82510e1bc65&units=metric&lang=RU')

data = res.json()  # Записываем в переменую пакет JSON, который получили - в ней есть поля и их значения

# отправляем запрос и записываем ответ от сервера в переменную, там данные по погоде на следующие дни
# zavtra_res = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=2745926c9f2ffb7903aec82510e1bc65&units=metric&lang=RU')
# zavtra_data = today_res.json()  # Записываем в переменую пакет JSON, который получили - в ней есть поля и их значения

# print(result.text)  # тестовый вывод - смотрим, что нам вернул сайт


# получаем нужные значения по названиям полей
print('Сейчас:')
print("Видимость:", data['list'][0]['weather'][0]['description'])  # выбираем в массиве первый элемент - 0 и из него вытаскиваем значение полей, которые надо
print('Ветрина:', data['list'][0]['wind']['speed'], 'м/с')
print("За бортом:", data['list'][0]['main']['temp'], 'по цельсию')
print('')
print('Завтра:', data['list'][1]['main']['temp'], 'по цельсию')
# print("Видимость:", data['list'][1]['weather'][0]['description'])  # выбираем в массиве первый элемент - 0 и из него вытаскиваем значение полей, которые надо
# print('Ветрина:', data['list'][1]['wind']['speed'], 'м/с')
# print("За бортом:", data['list'][1]['main']['temp'], 'по цельсию')
