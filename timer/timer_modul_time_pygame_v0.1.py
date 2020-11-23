import time

import pyglet

pyglet  # подключаем модули

# set_min = 0.1
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
song = pyglet.media.load('../media/komon.mp3')
# song = pyglet.media.load('C:/Windows/Media/tada.wav')
song.play()
pyglet.app.run()
