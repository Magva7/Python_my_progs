x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# x1 = -1
# y1 = 2
# x2 = -1
# y2 = 2

# как обычно, рассмотрим все 4 варианта:

if x1 > 0:  # т.е. если у первого числа по оси х +
    if y1 > 0:  # и по оси y тоже +
        where_1 = 1  # тогда получается, что число в 1 четверти
    else:
        where_1 = 2  # а если по оси y минус, то во 2
else:  # если же у первого числа по оси х минус
    if y1 > 0:  # а по оси y плюс
        where_1 = 4  # то это получается 4 четверть
    else:
        where_1 = 3  # а если по оси y тоже минус, то 3 четверть

if x2 > 0:  # т.е. если у второго числа по оси х +
    if y1 > 0:  # и по оси y тоже +
        where_2 = 1  # тогда получается, что число в 1 четверти
    else:
        where_2 = 2  # а если по оси y минус, то во 2
else:  # если же у второго числа по оси х минус
    if y2 > 0:  # а по оси y плюс
        where_2 = 4  # то это получается 4 четверть
    else:
        where_2 = 3  # а если по оси y тоже минус, то 3 четверть
# Дальше сравниваем
if where_1 == where_2:
    print('YES')
else:
    print('NO')