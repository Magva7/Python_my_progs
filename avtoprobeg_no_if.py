n = int(input())  # проезжает за 1 день
m = int(input()) - 1  # длина пути, 1 отнимаем для того, чтобы если m // n
# потом будет нацело делиться без остатка, чтобы наше итоговое число было на
# 1 меньше, т.е. например n = 300, m = 600, отнимаем 1, получается при
# делении нацело 1 и потом мы 1 прибавим, а если например n = 300,
# a m = 720, то при делении нацело получится 719 // 300 = 2, потом прибавим
# 1 и получится в итоге 3, а если например m = 601, то будет 600 // 2 = 2,
# как нам и надо

result = m // n + 1
print(result)
