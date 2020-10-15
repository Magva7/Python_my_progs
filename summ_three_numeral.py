number = int(input())
first_numeral = number // 100  # первая цифра числа
second_numeral = (number // 10) % 10  # вторая цифра числа
three_numeral = number % 10  # третья цифра числа

summ = first_numeral + second_numeral + three_numeral

print(summ)
