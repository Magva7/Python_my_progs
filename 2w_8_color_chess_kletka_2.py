v1 = int(input())
h1 = int(input())
v2 = int(input())
h2 = int(input())

# v1 = 4
# h1 = 5
# v2 = 1
# h2 = 2

# print(h2-h1)
# print(v2-v1)

# вариант, который подглядел у других
# dif_h = abs(h2 - h1)
# dif_v = abs(v2 - v1)

# итак у нас одинаковый цвет клеток в двух случаях и мы их все опишем:
# 1) клетки в одном столбце или через столбец, через 3 столбца  и т.д.,
# т.е. у них разница по горизонтали кратна 2, при этом у них разница по
# вертикали тоже кратна 2
# 2) клетки в соседнем столбце или в соседнем и через столбец и т.д., тогда у
# них разница по горизонтали + 1 кратна 2, т.е. как бы (n + 1) % 2 == 0 и по
# вертикали так же

# 1 - опишем первый случай - клетки в одном столбце или через столбец,
# через 3 столбца  и т.д.
if (h1 + h2 + v1 + v2) % 2 == 0:  # если сумма всех координат кратна 2
    print('YES')
else:
    print('NO')