n = int(input())  # проезжает за 1 день
m = int(input())  # длина пути

full_day = m // n  # целых дней
parts_day = m / n - full_day  # части дней

parts_day_calc = 0  # нецелых дней для расчета

if (parts_day != 0):
    parts_day_calc = 1

# print('целых дней: ', full_day)
# print('нецелых дней: ', parts_day)
# print('Нецелых дней для расчета: ', parts_day_calc)
result = full_day + parts_day_calc
print(result)
