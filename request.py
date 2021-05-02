import requests

import telebot

# appid = "2745926c9f2ffb7903aec82510e1bc65"  # мой id

# отправляем запрос и записываем ответ от сервера в переменную, там данные по погоде на сейчас
res = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=2745926c9f2ffb7903aec82510e1bc65&units=metric&lang=RU')

data = res.json()  # Записываем в переменую пакет JSON, который получили - в нем есть поля и их значения

# print(result.text)  # тестовый вывод - смотрим, что нам вернул сайт

# получаем нужные значения по названиям полей и печатаем погоду
def pogoda():

    temperatura = 'За бортом:  ' + '' + str(data['list'][0]['main']['temp']) + '' + ' по цельсию'
    veter = 'Ветрина:   ' + str(data['list'][0]['wind']['speed']) + ' м/с'
    vidimost = 'Видимость:   ' + str(data['list'][0]['weather'][0]['description'])
    zavtra = 'Завтра:  ' +  str(data['list'][1]['main']['temp']) + ' по цельсию'
    result = temperatura + '\n' + veter + '\n' + vidimost + '\n' + zavtra
    return result


#Бот
#токен: 1706338684:AAGojuK3Xw50cqr1osXwC6uvTRql0gQ-5cw
bot = telebot.TeleBot('1706338684:AAGojuK3Xw50cqr1osXwC6uvTRql0gQ-5cw')

@bot.message_handler(commands=['start'])  # прослушивание команды start
def send_welcome(message):  # приветственное сообщение
    if(message.from_user.first_name=='Magv'):
        bot.reply_to(message, f'Привет, создатель, погодку показать?')

    elif(message.from_user.first_name=='Melyashova'):
        bot.reply_to(message, f'Привет сестрам, погоду показать?')

    elif (message.from_user.first_name == 'LitlBro'):
        bot.reply_to(message, f'Привет, Димон, погоду показать?')

    elif (message.from_user.id == '497936829'):
        bot.reply_to(message, f'Привет, Палыч, погоду показать?')

    elif (message.from_user.id == '766674112'):
        bot.reply_to(message, f'Привет, Готяр, погоду показать?')

    elif (message.from_user.id == '576521348'):
        bot.reply_to(message, f'Здорова, Евген, погоду показать?')

    elif (message.from_user.id == '348719040'):
        bot.reply_to(message, f'Привет, Мам, погоду показать?')
    else:
        bot.reply_to(message, f'Здорово, бро, пока я умею здороваться и показывать погоду, чтоб глянуть погоду, напиши погода, кстати как тя зовут?')
    # bot.reply_to(message, f'Здорово, бро, {message.from_user.first_name}')
    print(message.from_user.first_name)
@bot.message_handler(commands=['help'])  # прослушивание команд help
def send_welcome(message):  # приветственное сообщение
        bot.reply_to(message, f'Чтоб глянуть погоду, напиши погода')
    # bot.reply_to(message, f'Здорово, бро, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])  # прослушивание текстовых сообщений
def get_text_messages(message):
    if message.text.lower() == "миша":
        bot.send_message(message.from_user.id, "Здорова, Палыч, погоду показать?")
    if message.text.lower() == "михаил":
            bot.send_message(message.from_user.id, "Здорова, Палыч, погоду показать?")
    elif message.text.lower() == "юран":
        bot.send_message(message.from_user.id, "Приветствую, создатель")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Тута будет помощь")
    elif message.text.lower() == "да" or "угу" or 'давай' or 'можно' or 'кажи' or 'ок' or 'ok':
        bot.send_message(message.from_user.id, pogoda())
        print(message.from_user.first_name, '-', message.from_user.id)
    elif message.text.lower() == "погода":
        bot.send_message(message.from_user.id, pogoda())
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True)