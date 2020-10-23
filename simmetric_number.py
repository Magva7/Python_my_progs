# number = int(input())

number = 1234  # введенное число
a = number // 1000  # первая цифры
b = number // 100 % 10
c = number % 100 // 10
d = number % 10
print(a, b, c, d, sep='')  # вывод для теста

number2 = d*1000 + c * 100 + b * 10 + a
print(number2)  # вывод для теста

# amount = number % 100  # две последние цифры справа, т.е. десятки и единицы
# print(amount // 10)  # делим нацело на 10, получаем количество десятков
#
# number = int(input())
# print(number % 10)
#
# n = int(input())  # наше число
# k = int(input())  # сколько цифр отрезаем
#
# print(n // 10 ** k)
#
# number = int(input())
# print(number % 100)

# в конце поделить его самого на себя, или в степень возвести, чтобы либо 0,
# либо 1 вывелить