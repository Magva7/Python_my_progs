v1 = 4
h1 = 5
v2 = 5
h2 = 5

# итак у нас вокруг короля есть 8 клеток, на которые он может пойти, т.е.
# есть 8 случаев, когда клетки соседние, т.е. когда надо выводить да,
# опишем все случаи, идем по часовой:

# 1) по диагонали вправо наверх, т.е. во второй клетке по горизонтали больше
# на 1 и по вертикали больше на 1
if (h2 - h1) == 1:
    if (v2 - v1) == 1:
        print('YES')
    else:
        print('NO')

# 2) направо, т.е. по горизонтали больше, а по вертикали также
elif(h2 - h1) == 1:
    if (v2 - v1) == 0:
        print('YES')
    else:
        print('NO')

# 3) по диагонали направо вниз, т.е. по горизонтали больше, а по вертикали
# меньше
elif(h2 - h1) == 1:
    if (v2 - v1) == -1:
        print('YES')
    else:
        print('NO')

# 4) вниз, т.е. по горизионтали также, а по вертикали меньше
elif(h2 - h1) == 0:
    if (v2 - v1) == 1:
        print('YES')
    else:
        print('NO')

# 5) по диагонали налево вниз, т.е. и там и там меньше
elif(h2 - h1) == -1:
    if (v2 - v1) == -1:
        print('YES')
    else:
        print('NO')

# 6) налево, т.е. по горизонтали меньше, а по вертикали также
elif(h2 - h1) == -1:
    if (v2 - v1) == 0:
        print('YES')
    else:
        print('NO')

# 7) по диагонали налево вверх, т.е. по горизонтали меньше, а по вертикали
# больше
elif(h2 - h1) == -1:
    if (v2 - v1) == 1:
        print('YES')
    else:
        print('NO')

# 8) вверх, т.е. по горизонтали также, а по вертикали больше
elif(h2 - h1) == 0:
    if (v2 - v1) == 1:
        print('YES')
    else:
        print('NO')

# во всех остальных случаях NO
else:
    print('NO')
