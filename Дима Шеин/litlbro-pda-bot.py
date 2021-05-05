import os

import logging

import random

from datetime import datetime

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import MessageHandler, Filters, InlineQueryHandler

import requests
import json

import string

def make_uchr(code: str):
    return chr(int(code.lstrip("U+").zfill(8), 16))

TOKEN = '1795319571:AAGzcetjsm74VPPVnk06Hq0Cgi_6uMPBlXE'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

random.seed()

reqCounter = 0
StartDate = datetime.now()

# функция обработки команды '/start'
def start(update, context):
    # Выбираем случайным образом приветствие между "Здравствуйте", "Привет" и "Доброе время суток"
    N = random.randint(1,3)
    Greeting = ""
    if N == 1:
        Greeting = "Здравствуйте"
    elif N == 2:
        Greeting = "Привет"
    else:
        H = datetime.now().hour
        if 0 < H < 7:
            Greeting = "Доброй ночи"
        elif 6 < H < 12:
            Greeting = "Доброе утро"
        elif 11 < H < 18:
            Greeting = "Добрый день"
        elif 17 < H < 23:
            Greeting = "Добрый вечер"
        else:
            Greeting = "Доброй ночи"
    context.bot.send_message(chat_id=update.effective_user.id, 
                             text=Greeting + ", " + str(update.effective_user.first_name) + " '" + str(update.effective_user.username) + "' " + str(update.effective_user.last_name) + "!")
    
def help(update, context):
    context.bot.send_message(chat_id=update.effective_user.id, 
                             text="Я умею выдавать прогноз погоды!\nДля этого мне надо отправить свое местоположение.\n\nПройдет немного времени, и я научусь еще чему-нибудь полезному! У ботовода на меня большие планы!")

# функция обработки присланного объекта location - точки на карте
def progn(update, context):
    global reqCounter
    progn_msg = ""    

    URL="https://api.openweathermap.org/data/2.5/onecall?appid=78c9d13b1a3eedbcf341e2eacc31e38b&units=metric&lang=ru&&lat=" + str(update.message.location.latitude) + "&lon=" + str(update.message.location.longitude)
    response = requests.get(URL)
    
    reqCounter += 1
    
    add_shift = False
    
    if response.status_code != 200:
        progn_msg = "\u2604 Духи метеопрогноза неблагосклонны к нам!"
    else:
        prognosis = json.loads(response.text)
        if "timezone_offset" in prognosis:
            if prognosis["timezone_offset"] != 0:
                if (abs(update.effective_message.date.timestamp() - prognosis["current"]["dt"])/prognosis["timezone_offset"]) > 0.3:
                    add_shift = True
        if add_shift:
            progn_msg = "По данным на " + datetime.fromtimestamp(prognosis["current"]["dt"] + prognosis["timezone_offset"]).strftime("%H:%M:%S %d-%m-%Y") + ", сейчас " 
        else:
            progn_msg = "По данным на " + datetime.fromtimestamp(prognosis["current"]["dt"]).strftime("%H:%M:%S %d-%m-%Y") + ", сейчас " 
        if prognosis["current"]["weather"][0]["id"] == 804:
            progn_msg += make_uchr("U+2601")
        elif prognosis["current"]["weather"][0]["id"] == 803:
            progn_msg += make_uchr("U+1F325")
        elif prognosis["current"]["weather"][0]["id"] == 802:
            progn_msg += make_uchr("U+26C5")
        elif prognosis["current"]["weather"][0]["id"] == 801:
            progn_msg += make_uchr("U+1F324")
        elif prognosis["current"]["weather"][0]["id"] == 800:
            progn_msg += make_uchr("U+2600")
        elif prognosis["current"]["weather"][0]["id"] > 700:
            progn_msg += make_uchr("U+1F32B")
        elif prognosis["current"]["weather"][0]["id"] > 600:
            progn_msg += make_uchr("U+1F328")
        elif prognosis["current"]["weather"][0]["id"] > 500:
            progn_msg += make_uchr("U+1F327")
        elif prognosis["current"]["weather"][0]["id"] > 300:
            progn_msg += make_uchr("U+1F327")
        elif prognosis["current"]["weather"][0]["id"] > 200:
            progn_msg += make_uchr("U+26C8")            
        progn_msg += " " + prognosis["current"]["weather"][0]["description"] 
        if "clouds" in prognosis["current"]:
            progn_msg += ".\nОблачность " + str(prognosis["current"]["clouds"]) + "%"
        if prognosis["current"]["weather"][0]["id"] >= 800 and prognosis["current"]["uvi"] > 3:
            progn_msg += ", " + make_uchr("U+1F3D6") + " солнечный ультрафиолетовый индекс " + (str(prognosis["current"]["uvi"]))
        if prognosis["current"]["uvi"] > 8:
            progn_msg += "Высокий уровень солнечной радиации, требуется защита - полуденные часы пережидайте в помещении, вне помещения оставайтесь в тени, носите одежду с длинными рукавами и головной убор"
        elif prognosis["current"]["uvi"] > 3:
            progn_msg += "Повышенный уровень солнечной радиации, предпочтительна защита - в полуденные часы оставайтесь в тени, носите одежду с длинными рукавами и головной убор"
        progn_msg += ".\n" + make_uchr("U+1F321") + " Температура " + str(prognosis["current"]["temp"])
        progn_msg += ", ощущается как " + str(prognosis["current"]["feels_like"]) 
        if "rain" in prognosis["current"]:
            if prognosis["current"]["rain"]["1h"] < 2.5:
                progn_msg += ".\n" + make_uchr("U+2614") + " Небольшой дождь"
            elif prognosis["current"]["rain"]["1h"] < 8:
                progn_msg += ".\n" + make_uchr("U+2614") + " Умеренный дождь"
            else:
                progn_msg += ".\n" + make_uchr("U+2614") + " Сильный дождь"
            progn_msg += " ({0:.2f} мм/ч)".format(prognosis["current"]["rain"]["1h"])
        if "wind_speed" in prognosis["current"]:
            progn_msg += ".\n" + make_uchr("U+1F32C") + " Ветер "
            if prognosis["current"]["wind_deg"] < 23:
                progn_msg += "северный"
            elif prognosis["current"]["wind_deg"] < 68:
                progn_msg += "северо-восточный"
            elif prognosis["current"]["wind_deg"] < 113:
                progn_msg += "восточный"
            elif prognosis["current"]["wind_deg"] < 158:
                progn_msg += "юго-восточный"
            elif prognosis["current"]["wind_deg"] < 193:
                progn_msg += "южный"
            elif prognosis["current"]["wind_deg"] < 238:
                progn_msg += "юго-западный"
            elif prognosis["current"]["wind_deg"] < 283:
                progn_msg += "западный"
            elif prognosis["current"]["wind_deg"] < 328:
                progn_msg += "северо-западный"
            else:
                progn_msg += "северный"
            progn_msg += " {0:.2f} м/с".format(prognosis["current"]["wind_speed"])
            if "wind_gust" in prognosis["current"]:
                progn_msg += ", порывы до {0:.2f} м/с".format(prognosis["current"]["wind_gust"])
        progn_msg += ".\nАтмосферное давление {0:d} мм рт.ст.".format(int(prognosis["current"]["pressure"] * 0.750064))
        if prognosis["current"]["pressure"] > 1000:
            progn_msg += " (повышенное)."
        elif prognosis["current"]["pressure"] < 985:
            progn_msg += " (пониженное)."
        progn_msg += "\nОтносительная влажность " + str(prognosis["current"]["humidity"]) + "%."
        progn_msg += "\nТочка росы {0:.2f}, видимость {1:d} м".format(prognosis["current"]["dew_point"], prognosis["current"]["visibility"])
        
        progn_msg += "\n\n"
        
        if "minutely" in prognosis:
            is_rain = (prognosis["minutely"][0]["precipitation"] != 0)
            rain_switches = []
            max_rain = 0
            i = 0 
            for i in range(0,len(prognosis["minutely"]) - 1):
                if max_rain > prognosis["minutely"][i]["precipitation"]:
                    max_rain = prognosis["minutely"][i]["precipitation"]
                if (prognosis["minutely"][i]["precipitation"] == 0) and is_rain:
                    is_rain = False                
                    rain_switches.append(i)                
                elif (prognosis["minutely"][i]["precipitation"] != 0) and (not is_rain):
                    is_rain = True
                    rain_switches.append(i)
            
            if (prognosis["minutely"][0]["precipitation"] != 0) and (len(rain_switches) == 0):
                progn_msg += "Идущий сейчас дождь не прекратится в течение ближайшего часа."
            elif (prognosis["minutely"][0]["precipitation"] != 0) and (len(rain_switches) == 1):
                progn_msg += "Идущий сейчас дождь прекратится через {0:d} минут.".format(rain_switches[0])
            elif (prognosis["minutely"][0]["precipitation"] != 0) and (len(rain_switches) == 2):
                progn_msg += "Дождь прекратится через {0:d} и возобновится через {1:d} минут.".format(rain_switches[0], rain_switches[1])
            elif (prognosis["minutely"][0]["precipitation"] != 0) and (len(rain_switches) == 3):
                progn_msg += "Дождь прекратится через {0:d}, возобновится через {1:d} и вновь прекратится через {2:d} минут.".format(rain_switches[0], rain_switches[1], rain_switches[2])
            elif (prognosis["minutely"][0]["precipitation"] != 0) and (len(rain_switches) > 3):
                progn_msg += "В ближайший час ожидаются кратковременные дожди."
            elif (prognosis["minutely"][0]["precipitation"] == 0) and (len(rain_switches) == 0):
                progn_msg += "В ближайший час дождя не ожидается."
            elif (prognosis["minutely"][0]["precipitation"] == 0) and (len(rain_switches) == 1):
                progn_msg += "Через {0:d} минут начнется дождь.".format(rain_switches[0])
            elif (prognosis["minutely"][0]["precipitation"] == 0) and (len(rain_switches) == 2):
                progn_msg += "Дождь начнется через {0:d} и закончится через {1:d} минут.".format(rain_switches[0], rain_switches[1])
            elif (prognosis["minutely"][0]["precipitation"] == 0) and (len(rain_switches) == 3):
                progn_msg += "Дождь начнется через {0:d}, закончится через {1:d} и вновь зарядит через {2:d} минут.".format(rain_switches[0], rain_switches[1], rain_switches[2])            
            elif (prognosis["minutely"][0]["precipitation"] == 0) and (len(rain_switches) > 1):
                progn_msg += "В ближайший час ожидаются кратковременные дожди."
            
            if max_rain > 2.5:
                progn_msg += " Лить будет сильно!"
            
        if "hourly" in prognosis:
            temper = []
            press = []
            humid = []
            rain = []
            wind = []
            
            for i in range(1, len(prognosis["hourly"]) - 2):
                if prognosis["hourly"][i-1]["temp"] < prognosis["hourly"][i]["temp"] > prognosis["hourly"][i+1]["temp"]:
                    temper.append(("max",prognosis["hourly"][i]["dt"],prognosis["hourly"][i]["temp"]))
                if prognosis["hourly"][i-1]["temp"] > prognosis["hourly"][i]["temp"] < prognosis["hourly"][i+1]["temp"]:
                    temper.append(("min",prognosis["hourly"][i]["dt"],prognosis["hourly"][i]["temp"]))
                if prognosis["hourly"][i-1]["pressure"] < prognosis["hourly"][i]["pressure"] > prognosis["hourly"][i+1]["pressure"]:
                    press.append(("max",prognosis["hourly"][i]["dt"],prognosis["hourly"][i]["pressure"]))
                if prognosis["hourly"][i-1]["pressure"] > prognosis["hourly"][i]["pressure"] < prognosis["hourly"][i+1]["pressure"]:
                    press.append(("min",prognosis["hourly"][i]["dt"],prognosis["hourly"][i]["pressure"]))
                if prognosis["hourly"][i-1]["humidity"] < prognosis["hourly"][i]["humidity"] > prognosis["hourly"][i+1]["humidity"]:
                    humid.append(("max",prognosis["hourly"][i]["dt"],prognosis["hourly"][i]["humidity"]))
                if prognosis["hourly"][i-1]["humidity"] > prognosis["hourly"][i]["humidity"] < prognosis["hourly"][i+1]["humidity"]:
                    humid.append(("min",prognosis["hourly"][i]["dt"],prognosis["hourly"][i]["humidity"]))
            if len(temper) > 1:
                for i in range(len(temper) - 1, 1, -1):
                    if (abs(temper[i][2] - temper[i - 1][2]) < 3) and (temper[i][2] * temper[i-1][2] > 0):
                        temper.pop(i)
            if len(press) > 1:
                for i in range(len(press) - 1, 1, -1):
                    if abs(press[i][2] - press[i-1][2]) < 5:
                        press.pop(i)
            if len(humid) > 1:
                for i in range(len(humid) - 1, 1, -1):
                    if abs(humid[i][2] - humid[i-1][2]) < 5:
                        humid.pop(i)
                        
            progn_msg += "\n\nВ ближайшие двое суток температура воздуха "
            if len(temper) > 0:
                if temper[0][0] == "max":
                    progn_msg += "повысится до {0:.2f} к ".format(temper[0][2])
                else:
                    progn_msg += "опустится до {0:.2f} к ".format(temper[0][2])
                if add_shift:
                    progn_msg += datetime.fromtimestamp(temper[0][1] + prognosis["timezone_offset"]).strftime("%H:%M %d-%m-%Y")                    
                else:
                    progn_msg += datetime.fromtimestamp(temper[0][1]).strftime("%H:%M %d-%m-%Y")
                for i in range(1, len(temper) - 1):
                    N = random.randint(1, 4)
                    if N == 1:
                        progn_msg += ", далее "
                    elif N == 2:
                        progn_msg += ", потом "
                    elif N == 3:
                        progn_msg += ", затем "
                    elif N == 4:
                        progn_msg += ", после этого "
                    progn_msg += "температура "
                    if temper[i][0] == "max":
                        progn_msg += "повысится до {0:.2f} градусов к ".format(temper[i][2])
                    else:
                        progn_msg += "опустится до {0:.2f} градусов к ".format(temper[i][2])
                    if add_shift: 
                        progn_msg += datetime.fromtimestamp(temper[i][1] + prognosis["timezone_offset"]).strftime("%H:%M %d-%m-%Y")                        
                    else:
                        progn_msg += datetime.fromtimestamp(temper[i][1]).strftime("%H:%M %d-%m-%Y")
            else:
                if prognosis["hourly"][47]["temp"] < prognosis["hourly"][0]["temp"]:
                    progn_msg += "будет стабильно понижаться с нынешних {0:.2f} до {1:.2f} градусов".format(prognosis["current"]["temp"], prognosis["hourly"][47]["temp"])
                elif prognosis["hourly"][47]["temp"] > prognosis["hourly"][0]["temp"]:
                    progn_msg += "будет стабильно повышаться с нынешних {0:.2f} до {1:.2f} градусов".format(prognosis["current"]["temp"], prognosis["hourly"][47]["temp"])
                else:
                    progn_msg += "останется неизменной - {0:.2f} градусов".format(prognosis["current"]["temp"])

            progn_msg += ".\n\nАтмосферное давление "
            if len(press) > 0:
                if press[0][0] == "max":
                    progn_msg += "возрастет до {0:d} мм рт.ст. к ".format(int(press[0][2] * 0.750064))
                else:
                    progn_msg += "понизится до {0:d} мм рт.ст. к ".format(int(press[0][2] * 0.750064))
                if add_shift:
                    progn_msg += datetime.fromtimestamp(press[0][1] + prognosis["timezone_offset"]).strftime("%H:%M %d-%m-%Y")                    
                else:
                    progn_msg += datetime.fromtimestamp(press[0][1]).strftime("%H:%M %d-%m-%Y")
                for i in range(1, len(press) - 1):
                    N = random.randint(1, 4)
                    if N == 1:
                        progn_msg += ", далее "
                    elif N == 2:
                        progn_msg += ", потом "
                    elif N == 3:
                        progn_msg += ", затем "
                    elif N == 4:
                        progn_msg += ", после этого "
                    progn_msg += "давление "
                    if press[i][0] == "max":
                        progn_msg += "возрастет до {0:d} мм рт.ст. к ".format(int(press[i][2] * 0.750064))
                    else:
                        progn_msg += "понизится до {0:d} мм рт.ст. к ".format(int(press[i][2] * 0.750064))
                    if add_shift:
                        progn_msg += datetime.fromtimestamp(press[i][1] + prognosis["timezone_offset"]).strftime("%H:%M %d-%m-%Y")                        
                    else:
                        progn_msg += datetime.fromtimestamp(press[i][1]).strftime("%H:%M %d-%m-%Y")
            else:
                if prognosis["hourly"][47]["pressure"] < prognosis["hourly"][0]["pressure"]:
                    progn_msg += "будет стабильно понижаться с нынешних {0:d} до {1:d} мм рт.ст.".format(int(prognosis["current"]["pressure"]  * 0.750064), int(prognosis["hourly"][47]["pressure"]  * 0.750064))
                elif prognosis["hourly"][47]["pressure"] > prognosis["hourly"][0]["pressure"]:
                    progn_msg += "будет стабильно повышаться с нынешних {0:d} до {1:d} мм рт.ст.".format(int(prognosis["current"]["pressure"]  * 0.750064), int(prognosis["hourly"][47]["pressure"]  * 0.750064))
                else:
                    progn_msg += "останется неизменным - {0:d} мм рт.ст.".format(int(prognosis["current"]["pressure"]))

            progn_msg += ".\n\nВлажность воздуха "
            if len(humid) > 0:
                if humid[0][0] == "max":
                    progn_msg += "повысится до {0:d}% к ".format(humid[0][2])
                else:
                    progn_msg += "опустится до {0:d}% к ".format(humid[0][2])
                if add_shift:
                    progn_msg += datetime.fromtimestamp(humid[0][1] + prognosis["timezone_offset"]).strftime("%H:%M %d-%m-%Y")                    
                else:
                    progn_msg += datetime.fromtimestamp(humid[0][1]).strftime("%H:%M %d-%m-%Y")
                for i in range(1, len(humid) - 1):
                    N = random.randint(1, 4)
                    if N == 1:
                        progn_msg += ", далее "
                    elif N == 2:
                        progn_msg += ", потом "
                    elif N == 3:
                        progn_msg += ", затем "
                    elif N == 4:
                        progn_msg += ", после этого "
                    progn_msg += "влажность "
                    if humid[i][0] == "max":
                        progn_msg += "повысится до {0:d}% к ".format(humid[i][2])
                    else:
                        progn_msg += "опустится до {0:d}% к ".format(humid[i][2])
                    if add_shift:
                        progn_msg += datetime.fromtimestamp(humid[i][1] + prognosis["timezone_offset"]).strftime("%H:%M %d-%m-%Y")
                    else:
                        progn_msg += datetime.fromtimestamp(humid[i][1]).strftime("%H:%M %d-%m-%Y")                        
            else:
                if prognosis["hourly"][47]["humidity"] < prognosis["hourly"][0]["humidity"]:
                    progn_msg += "будет стабильно понижаться с нынешних {0:d} до {1:d}%".format(prognosis["current"]["humidity"], prognosis["hourly"][47]["humidity"])
                elif prognosis["hourly"][47]["humidity"] > prognosis["hourly"][0]["humidity"]:
                    progn_msg += "будет стабильно повышаться с нынешних {0:d} до {1:d} градусов".format(prognosis["current"]["humidity"], prognosis["hourly"][47]["humidity"])
                else:
                    progn_msg += "останется неизменной - {0:d}%".format(prognosis["current"]["humidity"])        
        
        progn_msg += "\n\n"
        
        if "alerts" in prognosis:
            if len(prognosis["alerts"]) > 0:
                progn_msg += make_uchr("U+1F6A8") + " Предупреждения метеослужбы:\n"
                for i in range(0, len(prognosis["alerts"]) - 1):
                    if len(prognosis["alerts"][i]["description"]) > 0:
                        progn_msg += prognosis["alerts"][i]["event"] + ": " + prognosis["alerts"][i]["description"] + " c " + datetime.fromtimestamp(prognosis["alerts"][i]["start"]  + prognosis["timezone_offset"]).strftime("%H:%M:%S %d-%m-%Y") + " по " + datetime.fromtimestamp(prognosis["alerts"][i]["end"]  + prognosis["timezone_offset"]).strftime("%H:%M:%S %d-%m-%Y") + ".\n"
      
        context.bot.send_message(chat_id=update.effective_user.id, 
                             text=progn_msg)

# функция обработки команды admstatus
def admStatus(update, context):
    is_heroku = os.environ.get('HEROKU', False)
    if is_heroku:
        context.bot.send_message(chat_id=update.effective_user.id, 
                             text="Сейчас " + datetime.now().strftime("%H:%M:%S %d-%m-%Y") + ",\nбот был запущен в " + StartDate.strftime("%H:%M:%S %d-%m-%Y") + ".\nМетеосводка запрашивалась {0:d} раз.\nБот запущен на HEROKU".format(reqCounter))
    else:
        context.bot.send_message(chat_id=update.effective_user.id, 
                             text="Сейчас " + datetime.now().strftime("%H:%M:%S %d-%m-%Y") + ",\nбот был запущен в " + StartDate.strftime("%H:%M:%S %d-%m-%Y") + ".\nМетеосводка запрашивалась {0:d} раз.\nБот запущен локально".format(reqCounter))

# функция обработки нераспознанных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_user.id, 
                             text="Простите, " + update.effective_user.first_name + " '" + update.effective_user.username + "' " + update.effective_user.last_name + ", я не понимаю, о чем Вы просите!")
    
# ежеминутная проверка перехода через полночь
def callback_minute(context: CallbackContext):
    global reqCounter
    global StartDate
    curDate = datetime.now()
    if curDate.isoweekday() != StartDate.isoweekday():
        StartDate = curDate
        reqCounter = 0

# обработчик команды '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# обработчик команды '/help'
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

# обработчик location
location_handler = MessageHandler(Filters.location, progn)
dispatcher.add_handler(location_handler)

# обработчик команды '/admstatus'
admStatus_handler = CommandHandler('admstatus', admStatus)
dispatcher.add_handler(admStatus_handler)

# обработчик нераспознанных команд
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# запуск очереди сообщений
updater.job_queue.run_repeating(callback_minute, interval=60, first=0)

is_heroku = os.environ.get('HEROKU', False)
if is_heroku:
    PORT = int(os.environ.get('PORT', '8443'))
    updater.start_webhook(listen="0.0.0.0",
                        port=PORT,
                        url_path=TOKEN,
                        webhook_url="https://litlbro-pda-bot.herokuapp.com/" + TOKEN)    
else:
    updater.start_polling()
    
# обработчик нажатия Ctrl+C
updater.idle()
