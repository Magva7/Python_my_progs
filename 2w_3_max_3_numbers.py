number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 >= number2:  # если 1-ое больше 2
    if number1 >= number3:  # если предыдущее условие выполнилось, то
        # проверяем, что 1-ое больше 3
        print(number1)
    else:
        print(number3)
else:  # здесь у нас в случае, если 1-ое меньше 2
    if number2 > number3:  # проверяем 2-ое, если больше 3
        print(number2)
    else:
        print(number3)
