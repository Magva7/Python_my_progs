d_sklad = int(input())
s_sklad = int(input())
v_sklad = int(input())
d_nout = int(input())
s_nout = int(input())
v_nout = int(input())
# длина, ширина и высота склада
# d_sklad = 7
# s_sklad = 7
# v_sklad = 7
# длина, ширина и высота ноута
# d_nout = 3
# s_nout = 3
# v_nout = 3

# ищем на складе стороны по возрастанию
min_s = 0
average_s = 0
max_s = 0


if d_sklad <= s_sklad <= v_sklad:
    min_s = d_sklad
    average_s = s_sklad
    max_s = v_sklad
elif d_sklad <= v_sklad <= s_sklad:
    min_s = d_sklad
    average_s = v_sklad
    max_s = s_sklad
elif v_sklad <= d_sklad <= s_sklad:
    min_s = v_sklad
    average_s = d_sklad
    max_s = s_sklad
elif v_sklad <= s_sklad <= d_sklad:
    min_s = v_sklad
    average_s = s_sklad
    max_s = d_sklad
elif d_sklad <= v_sklad <= s_sklad:
    min_s = d_sklad
    average_s = v_sklad
    max_s = s_sklad
elif d_sklad <= s_sklad <= v_sklad:
    min_s = d_sklad
    average_s = s_sklad
    max_s = v_sklad

# теперь тоже самое с ноутами
# ищем стороны по возрастанию
min_n = 1
average_n = 1
max_n = 1

if d_nout <= s_nout <= v_nout:
    min_n = d_nout
    average_n = s_nout
    max_n = v_nout
    # print('test_1')
elif d_nout <= v_nout <= s_nout:
    min_n = d_nout
    average_n = v_nout
    max_n = s_nout
    # print('test_2')
elif v_nout <= d_nout <= s_nout:
    min_n = v_nout
    average_n = d_nout
    max_n = s_nout
    # print('test_3')
elif v_nout <= s_nout <= d_nout:
    min_n = v_nout
    average_n = s_nout
    max_n = d_nout
elif d_nout <= v_nout <= s_nout:
    min_n = d_nout
    average_n = v_nout
    max_n = s_nout
elif d_nout <= s_nout <= v_nout:
    min_n = d_nout
    average_n = s_nout
    max_n = v_nout

# считаем, сколько ноутов влезет по длине, ширине и высоте, а потом умножаем
# друг на друга
result = (min_s // min_n) * (average_s // average_n) * (max_s // max_n)
# print(min_s, min_n, average_s, average_n, max_s, max_n)
print(result)
