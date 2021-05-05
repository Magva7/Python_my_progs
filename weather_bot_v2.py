import requests
# import pytelegrambotapi
import telebot
from telebot import types

# appid = "2745926c9f2ffb7903aec82510e1bc65"  # мой id для погоды на openweathermap.org

# Функция, которая запрашивает погоду, распарсивает json ответ и записывает его части в переменные
def pogoda():
    # отправляем запрос и записываем ответ от сервера в переменную, там данные по погоде на сейчас
    res = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=2745926c9f2ffb7903aec82510e1bc65&units=metric&lang=RU')
    print('Заново запросил погоду')  # вывод в консоль для теста

    data = res.json()  # Записываем в переменую пакет JSON, который получили - в нем есть поля и их значения

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

    key_dacha = types.InlineKeyboardButton(text='Дача', callback_data='dacha')  # сама кнопка
    keyboard.add(key_dacha)  # добавляем кнопку на экран

    key_rayon = types.InlineKeyboardButton(text='Район', callback_data='rayon')
    keyboard.add(key_rayon)

    key_piter = types.InlineKeyboardButton(text='Питер', callback_data='piter')
    keyboard.add(key_piter)

    bot.send_message(message.from_user.id, text='Привет, где показать погодку?', reply_markup=keyboard)  # Отправляем кнопки

    # print(message.from_user.first_name)


@bot.message_handler(commands=['help'])  # прослушивание команды help
def send_welcome(message):  # приветственное сообщение
    bot.reply_to(message, f'Чтоб глянуть погоду, напиши погода')


# bot.reply_to(message, f'Здорово, бро, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])  # прослушивание текстовых сообщений
def get_text_messages(message):
    if message.text.lower() == "миша":
        bot.send_message(message.from_user.id, "Здорова, Палыч, погоду показать?")
    elif message.text.lower() == "погода":
        bot.send_message(message.from_user.id, pogoda())
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)  # Прослушивание нажатий кнопок
def callback_worker(call):  # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == 'dacha':  # Формируем гороскоп
        msg = '1'
        # bot.send_message(call.message.chat.id, msg)  # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, f'На дачке ща: ', msg, '')
        # bot.reply_to(message, f'На дачке ща: 'б)


bot.polling(none_stop=True, interval=0)