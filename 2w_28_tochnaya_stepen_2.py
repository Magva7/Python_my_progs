a = int(input())
# a = 18
stepen = 0

while 2**stepen < a:  # т.е. пока 2 в текущей степени меньше заданного числа
    stepen = stepen + 1  # каждую итерацию увеличиваем степень на 1
if 2**stepen == a:  # если совпало, то да
    print('YES')
else:
    print('NO')
