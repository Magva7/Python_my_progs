secund_input = int(input())  # сколько секунд ввели

# сколько получилось целых часов, т.е. сколько часов прошло - делим
# введенные секунды на 3600 и считаем остаток от 24
result_hours = (secund_input // 3600) % 24

# дальше выводим количество минут - разбиваем на 2 символа, десятки и единицы,
# т.к. если у нас целых минут получится меньше 10, то в первом символе,
# где десятки, должен быть ноль

# сколько получилось целых минут - делим количество введенных секунд на 60
# и считаем остаток от 60
minut = (secund_input // 60) % 60

# первая цифра в минутах
minut_a = minut // 10

# вторая цифра в минутах
minut_b = minut % 10

# дальше также работаем с секундами
# сколько всего получилось секунд
secund = secund_input % 60

# первая цифра в минутах
secund_a = secund // 10

# вторая цифра в минутах
secund_b = secund % 10

# сколько секунд прошло - остаток от деления на 3600
result_secund = secund_input % 60

print(result_hours, ':', minut_a, minut_b, ':', secund_a, secund_b, sep='')
