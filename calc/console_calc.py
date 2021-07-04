a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

deystvie = input('Что делаем? (+, -): ')

if deystvie == '+':
    c = a + b
    print(c)
elif deystvie == '-':
    c = a - b
    print(c)
else:
    print('Выбрано неверное действие')
