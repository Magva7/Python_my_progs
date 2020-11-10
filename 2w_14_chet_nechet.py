a = int(input())
b = int(input())
c = int(input())

# a = 2
# b = 4
# c = -12

if (a % 2) == 0:  # если a четное
    if (b % 2) == 0:  # если b тоже четное
        if (c % 2) == 0:  # если c тоже четное
            print('NO')
        else:
            print('YES')  # если же c нечетное
    else:
        print('YES')  # если b нечетное, то c дальше можно не проверять

elif (a + 1) % 2 == 0:  # если a нечетное
    if (b + 1) % 2 == 0:  # если b тоже нечетное
        if (c + 1) % 2 == 0:  # если c тоже нечетное
            print('NO')
        else:
            print('YES')  # если же c четное
    else:
        print('YES')  # если b четное, то c дальше можно не проверять
else:
    print('NO')
