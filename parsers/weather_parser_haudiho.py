# from turtle import config_dict

import pyowm
from pyowm.utils.config import get_default_config
# from pyowm.owm import OWM
# from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps

owm = pyowm.OWM('2745926c9f2ffb7903aec82510e1bc65')  # мой API Key

# технические вещи, нужны для работы, пока хз, что значат
config_dict = get_default_config()
config_dict['language'] = 'ru'
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Москва')  # место
pogoda= observation.weather

temperatura = round(pogoda.temperature('celsius')['temp'])
print('В Москве сейчас +' + str(temperatura) + ' по цельсию, ' + pogoda.detailed_status)

print(pogoda)
