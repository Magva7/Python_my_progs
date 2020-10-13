minut_count = int(input())

# сколько часов прошло - делим кол-во минут на 60 считаем остаток
result_hours = (minut_count // 60) % 23

# сколько минут прошло - остаток от деления
result_minut = minut_count % 60

print(result_hours, result_minut)
