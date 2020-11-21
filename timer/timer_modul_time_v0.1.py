import time  # подключаем модуль time


set_min = 10  # количество минут, которое вводим
set_sec = set_min * 60

while set_min != 0:
    set_sec -= 1  # каждую итерацию уменьшаем секунды на 1
    print(time.strftime("Осталось: %M:%S", time.localtime(set_sec)))
    time.sleep(1)  # задержка - раз в секунду