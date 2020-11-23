import time  # подключаем модули

import pygame

# set_min = 0.05
print('Введите количество минут: ', end='')
set_min = int(input())  # количество минут, которое вводим
set_sec = set_min * 60

while set_sec != 0:
    set_sec -= 1  # каждую итерацию уменьшаем секунды на 1
    print(time.strftime("Осталось: %M:%S", time.localtime(set_sec)), end='')
    # выводим оставшее время, в конце end='', чтобы не выводило каждый раз с
    # новой строки
    time.sleep(1)  # задержка - раз в секунду
    print('\r', end='')  # еще раз очищаем строку

print('Пыпыньк =)')

# как цикл выполнился, т.е. дошло до 0, выводим музон
pygame.init()  # инициируем что-то
pygame.mixer.init()  # инициируем миксер

# pygame.mixer.music.load('../media/komon.mp3')  # путь к музлу
pygame.mixer.music.load('C:/Windows/Media/tada.wav')  # путь к музлу
pygame.mixer.music.play()  # запуск
while pygame.mixer.music.get_busy():  # цикл для ожидания, без него не играет
    pygame.time.Clock().tick(10)
