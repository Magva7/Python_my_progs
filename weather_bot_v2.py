import requests
# import pytelegrambotapi
import telebot
from telebot import types

# appid = "2745926c9f2ffb7903aec82510e1bc65"  # мой id для погоды на openweathermap.org

# координаты места
koord_dacha = 'https://api.openweathermap.org/data/2.5/forecast?id=548410&appid=2745926c9f2ffb7903aec82510e1bc65&units=metric&lang=RU'
# koord_dacha_lat_lon = 'https://api.openweathermap.org/data/2.5/forecast?lat=54&lon=34&appid=2745926c9f2ffb7903aec82510e1bc65&units=metric&lang=RU'
koord_moscow = 'https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=2745926c9f2ffb7903aec82510e1bc65&units=metric&lang=RU'
# pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={API key}
koord_rayon = 'https://api.openweathermap.org/data/2.5/forecast?lat=55.83950537444567&lon=37.507909885375916&appid=2745926c9f2ffb7903aec82510e1bc65&units=metric&lang=RU'

# функция принимает координаты места и запрашивает погоду и возвращает данные, которые потом будем распарсивать
def zapros_pogody(koord):
    # отправляем запрос и записываем ответ от сервера в переменную, там данные по погоде на сейчас
    res = requests.get(koord)
    # res = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=2745926c9f2ffb7903aec82510e1bc65&units=metric&lang=RU')
    data = res.json()  # Записываем в переменую пакет JSON, который получили - в нем есть поля и их значения
    print('Заново запросил погоду')  # вывод в консоль для теста
    temp_current = round(data['list'][0]['main']['temp'])  # температура сейчас в цифрах, округляем
    temp_zavtra = round(data['list'][1]['main']['temp'])  # температура завтра в цифрах, округляем
    temperatura = 'За бортом:  + ' + '' + str(temp_current) + '' + ' по цельсию'
    veter = 'Ветрина:   ' + str(round(data['list'][0]['wind']['speed'])) + ' м/с'
    osadki = 'Осадки:   ' + str(data['list'][0]['weather'][0]['description'])
    zavtra = 'Завтра:  + ' + str(temp_zavtra) + ' по цельсию'
    result = temperatura + '\n' + veter + '\n' + osadki + '\n' + zavtra
    return result


# Бот токен: 1706338684:AAGojuK3Xw50cqr1osXwC6uvTRql0gQ-5cw
bot = telebot.TeleBot('1706338684:AAGojuK3Xw50cqr1osXwC6uvTRql0gQ-5cw')


@bot.message_handler(commands=['start'])  # прослушивание команды start
def send_welcome(message):  # приветственное сообщение
    # bot.reply_to(message, f'Привет, где погодку показать?')
    keyboard = types.InlineKeyboardMarkup()  # Техническая штука для кнопок - сами кнопки и обработчики

    key_rayon = types.InlineKeyboardButton(text='Район', callback_data='rayon')
    keyboard.add(key_rayon)

    key_dacha = types.InlineKeyboardButton(text='Дача', callback_data='dacha')  # сама кнопка
    keyboard.add(key_dacha)  # добавляем кнопку на экран

    key_piter = types.InlineKeyboardButton(text='Питер', callback_data='piter')
    keyboard.add(key_piter)

    bot.send_message(message.from_user.id, text='Привет, где показать погодку?', reply_markup=keyboard)  # Приветственное сообщение и кнопки

    # print(message.from_user.first_name)

@bot.message_handler(commands=['help'])  # прослушивание команды help
def send_welcome(message):  # приветственное сообщение
    bot.reply_to(message, f'Чтоб глянуть погоду на районе, напиши 1, на даче 2, в Питере 3')


# bot.reply_to(message, f'Здорово, бро, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])  # прослушивание текстовых сообщений
def get_text_messages(message):
    if message.text.lower() == "миша":
        bot.send_message(message.from_user.id, "Здорова, Палыч, погоду показать?")
    elif message.text.lower() == "1":  # если пришло 1
        bot.send_message(message.from_user.id, zapros_pogody(koord_rayon))
        print('Кто написал:', message.from_user.first_name, '-', message.from_user.id, 'что написал:', message.text)
    elif message.text.lower() == "2":  # если пришло 2
        bot.send_message(message.from_user.id, zapros_pogody(koord_dacha))  # запускается функция, которая запрашивает и выдает погоду, в нее передаем координаты дачи
        print('Кто написал:', message.from_user.first_name, '-', message.from_user.id, 'что написал:', message.text)
    # elif message.text.lower() == "погода":
    #     bot.send_message(message.from_user.id, zapros_pogody())
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)  # Прослушивание нажатий кнопок
def callback_worker(call):  # Прослушивание нажатий кнопок
    if call.data == 'dacha':  # Нажата кнопка дача
        msg_dacha = 'Cейчас:  ' + '\n' + '\n' + zapros_pogody(koord_dacha) + '\n' + '\n' + 'Чтобы обновить, напиши 2'  # сообщение, которое отправится
        bot.send_message(call.message.chat.id, msg_dacha)  # Отправляем текст в Телеграм
        print('Кто:', call.message.chat.id, '-', 'какую кнопку нажал:', call.data)

    if call.data == 'rayon':  # Нажата кнопка район
        msg_rayon = 'Cейчас:  ' + '\n' + '\n' + zapros_pogody(koord_rayon) + '\n' + '\n' + 'Чтобы обновить, напиши 2'  # сообщение, которое отправится
        bot.send_message(call.message.chat.id, msg_rayon)  # Отправляем текст в Телеграм
        print('Кто:', call.message.chat.id, '-', 'какую кнопку нажал:', call.data)
bot.polling(none_stop=True, interval=0)
