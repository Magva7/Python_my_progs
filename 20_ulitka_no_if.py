dlina = int(input())
vverh = int(input())
vniz = int(input())
# dlina = 10
# vverh = 3
# vniz = 2
vverh_v_den = vverh - vniz

dlina_calc = dlina - vverh  # длина без последнего дня - вместо него прибавим
# потом 1
result_calc = (dlina_calc - 1) // vverh_v_den  # делим получившуюся длину без
# последнего дня на то, сколько улитка проползает за 1 раз, при делении от
# длины отнимаем 1, чтобы потом округлить вверх
print(result_calc+2)  # к итогу прибавляем 2 - 1, чтобы округлить вверх,
# т.к. мы раньше 1 отняли и еще 1 за последний день

#Пояснения:
# для начала нужно понимать, что движение Улитки разделено на 2 цикличные фазы
# - День(когда она поднимается) и Ночь(когда скользит вниз) и при достижение
# Финиша будет приходиться на фазу Дня, т.к. именно тогда Улитка сделает своё
# последнее движение к цели. Соответственно, она сделает X циклов (День-Ночь)
# и в конце еще один полуцикл Дня. Мы должны заранее отнять одно продвижение
# вверх от высоты шеста и поделить оставшееся расстояние на скорость улитки
# (сколько она проползает за сутки - полный цикл День-Ночь) с округлением
# вверх и, наконец, прибавить единицу, вернув результату еще 1 День
# на последний рывок.
