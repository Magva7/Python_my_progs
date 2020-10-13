minut_count = int(input())
result_hours = (minut_count // 60) % 23  # сколько часов прошло - делим кол-во минут на 60 считаем остаток
result_minut = minut_count % 60  # сколько минут прошло - остаток от деления

print(result_hours, result_minut)
