minut_count = int(input())  # сколько минут ввели

# сколько часов прошло - делим количество минут на 60 и считаем остаток от 24
result_hours = (minut_count // 60) % 24

# сколько минут прошло - остаток от деления
result_minut = minut_count % 60

print(result_hours, result_minut)
