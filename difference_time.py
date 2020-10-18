# вводим 2 раза время - часы, минуты и секунды
f_hours = int(input())
f_min = int(input())
f_sec = int(input())
s_hours = int(input())
s_min = int(input())
s_sec = int(input())

# нужно вывести разницу времен, для этого сложим все секунды у обоих чисел, а
# потом выведем разницу

# сумма секунд у первого времени
sum_sec_f_time = f_hours * 3600 + f_min * 60 + f_sec

# сумма секунд у первого времени
sum_sec_s_time = s_hours * 3600 + s_min * 60 + s_sec

# разница - второе время, минус первое
result = sum_sec_s_time - sum_sec_f_time
print(result)
