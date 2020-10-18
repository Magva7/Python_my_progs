secund_input = int(input())  # сколько секунд ввели

# сколько часов прошло - делим количество секунд на 3600 и считаем остаток от 24
result_hours = (secund_input // 3600) % 24

# сколько минут прошло - делим количество секунд на 60
result_minut = (secund_input // 60) % 60

# сколько секунд прошло - остаток от деления на 3600
result_secund = secund_input % 60

print(result_hours, result_minut, result_secund)
