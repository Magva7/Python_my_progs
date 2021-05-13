import pyautogui
import time

time.sleep(5)  # пауза 5 секунд перед запуском, чтобы успеть развернуть окно ро

# screen = pyautogui.screenshot('ro_screen.png')  # делаем скрин
# pyautogui.size()  # смотрим размер экрана
# width, height = pyautogui.size()
# print(width, height)
# currentMouseX, currentMouseY = pyautogui.position()  # Получаем XY координаты курсора.
# print(currentMouseX, currentMouseY)  # выводим для теста координаты курсора
pyautogui.click(1094, 1094)  # Перемещение мыши по XY координатам и клик по ним
time.sleep(3)
pyautogui.click(483, 257)  # Перемещение мыши по XY координатам и клик по ним
pyautogui.press('insert')
time.sleep(1)
pyautogui.press('esc')

# egg1 = pyautogui.locateCenterOnScreen('egg1.png')  # If the file is not a png file it will not work
# print(egg1)

# egg2 = pyautogui.locateCenterOnScreen('egg2.png')  #I f the file is not a png file it will not work
# print('Нашел яйцо по координатам: ', egg2)

# pyautogui.moveTo(egg1)  # Moves the mouse to the coordinates of the image
# pyautogui.click(egg1)
# time.sleep(2)

# pyautogui.moveTo(egg2)  # Moves the mouse to the coordinates of the image
# pyautogui.click(egg2)
# pyautogui.moveTo(483, 257)
# time.sleep(1)
# pyautogui.click(483, 257)  # Перемещение мыши по XY координатам и клик по ним.
# pyautogui.mouseDown(button='left')
# pyautogui.move(50, 0)      # Перемещение мыши вправо от текущей позиции на 50
# time.sleep(1)
# print('Переместил мышку')
# pyautogui.move(50, 0)      # Перемещение мыши вправо от текущей позиции на 50
# time.sleep(1)
# print('Переместил мышку')
# pyautogui.move(50, 0)      # Перемещение мыши вправо от текущей позиции на 50
# pyautogui.mouseUp(button='left')
# print(screen)
# if pyautogui.click('egg.png'):
#     print('Нашел яйцо')
# else:
#     print('Что-то пошло не так')
# pyautogui.click('excel.png')
