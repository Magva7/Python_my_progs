# number = int(input())

# number = 22  # введенное число
n = 14
print(1 + (n//100) - ((n % 10) * 10 + (n % 100) // 10))
# a = number // 1000  # первая цифра
# b = number // 100 % 10
# c = number % 100 // 10
# d = number % 10
#
# print('a =', a)
# print('b =', b)
# print('c =', c)
# print('d =', d)
#
# print(a, b, c, d, sep='')  # вывод для теста

# n = int(input())  # наше число
# k = int(input())  # сколько цифр отрезаем
#
# print(n // 10 ** k)
#
#
#
# number2 = d*1000 + c * 100 + b * 10 + a  # число в обратно порядке
# print(number2)  # вывод для теста
# #
# proverka = number % number2  # проверяем - если числа одинаковые, то при
# # выводе остатка получится 0, а если не одинаковые, то что-то другое
# # print(proverka)
#
# itog = int(0**proverka)  # дальше итог - возводим 0 в ту степень, которая у
# # нас получилась в проверке, если там 0, т.е. числа делятся нацело, то будет
# # 0 в нулевой степени, т.е., а если там любое другое число, то будет 0 в
# # другой степени, т.е. 0
# print(itog)
