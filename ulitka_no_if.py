dlina = int(input())
vverh = int(input())
vniz = int(input())
# dlina = 10
# vverh = 3
# vniz = 2
vverh_v_den = vverh - vniz

dlina_calc = dlina - vverh  # длина бз последнего дня - вместо него прибавим
# потом 1
day = dlina_calc / vverh_v_den

print(int(day) + vverh_v_den)
