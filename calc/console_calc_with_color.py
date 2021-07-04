from colorama import init
from colorama import Fore, Back, Style

init()  # чтобы работало на винде

print(Fore.BLACK)  # меняем цвет текста
print(Back.CYAN)  # окрашиваем фон в команде принт в зеленый цвет

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

print(Back.GREEN)  # окрашиваем фон в команде принт в цвет аква

deystvie = input('Что делаем? (+, -): ')

print(Back.YELLOW)
if deystvie == '+':
    c = a + b
    print(c)
elif deystvie == '-':
    c = a - b
    print(c)
else:
    print('Выбрано неверное действие')
input()
