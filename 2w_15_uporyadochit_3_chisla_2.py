a = int(input())
b = int(input())
c = int(input())

# a = 50
# b = 0
# c = 2
# print(a, b, c)

# как обычно перечисляем все варианты в порядке возрастания:
# abc
if a >= b >= c:
    (a, b, c) = (c, b, a)
# acb
elif a >= c >= b:
    (a, b, c) = (b, c, a)
# bac
elif b >= a >= c:
    (a, b, c) = (c, a, b)
# bca
elif b >= c >= a:
    (a, b, c) = (a, c, b)
# cab
elif c >= a >= b:
    (a, b, c) = (b, a, c)
# cba - не нужно, все и так по возрастанию

print(a, b, c)
