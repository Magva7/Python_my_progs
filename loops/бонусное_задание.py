strok_vsego = 5
current_strok_number = 1  # счетчик строк
current_cifra = 1    # счетчик цифр в строке
text = ''

# добавляем строки до тех пор, пока номер текущей строки меньше, чем сколько всего строк
while current_strok_number <= strok_vsego:

    # строка набитая циклом выглядит так
    current_strok_number += 1  # сейчас равен 1

    # добавляем во все строки в начало пробелов столько, сколько всего строк
    text += str(' ' * (strok_vsego))
    current_cifra = current_strok_number

    # обратном порядке на уменьшение до 1
    while current_cifra != 1:
        current_cifra -= 1
        text += str(current_cifra)

    text += '\n'  # добавляем в конце перенос строки

current_strok_number += 1  # увеличиваем номер текущей строки

print(text)

# очищаем все переменные
strok_vsego = 5
current_strok_number = 5  # счетчик строк
current_cifra = 1    # счетчик цифр в строке
text = ''

# пирамида в обратном порядке, чтобы получился ромб, добавляем строки до тех пор, пока номер текущей строки не будет = 1
while current_strok_number != 1:

    # строка набитая циклом выглядит так
    current_strok_number -= 1  # сейчас равен 1

    # добавляем в начале строки пробелов столько, сколько всего строк, минус номер текущей строки, т.е. в первой
    # строке в начале будет 4 пробела
    text += str(' ' * (strok_vsego - current_strok_number))

    # добавляем во все строки в конец пробелов столько, сколько всего строк
    text += str('' * (strok_vsego))
    current_cifra = current_strok_number

    # потом добавляем числа с 1 до номера текущей строки, т.е. в первой строке будет 1, во 2 - 12
    while current_cifra <= current_strok_number:
        text += str(current_cifra)
        current_cifra += 1

    current_cifra = current_strok_number

    # и в обратном порядке на уменьшение до 1
    while current_cifra != 1:
        current_cifra -= 1
        text += str(current_cifra)

    # потом опять добавляем столько пробелов, сколько всего строк, минус номер текущей строки
    text += str(' ' * (strok_vsego - current_strok_number))
    text += '\n'  # добавляем в конце перенос строки

current_strok_number += 1  # увеличиваем номер текущей строки

text += '33'
print(text)

# строка 5 руками для теста
# print(123454321)
