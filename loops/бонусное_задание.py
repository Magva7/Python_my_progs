strok_vsego = 9
current_strok_number = 1  # счетчик строк
current_cifra = 1    # счетчик цифр в строке
text = ''

# первая часть добавляем строки до тех пор, пока номер текущей строки меньше, чем сколько всего строк
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
# print(current_strok_number)

# задаем новые значения переменным, теперь у нас номер строки начинается с n
current_strok_number = strok_vsego  # счетчик строк
current_cifra = 0    # счетчик цифр в строке

# вторая часть, пока номер текущей строки не будет = 1
while current_strok_number != 0:

    # строка набитая циклом выглядит так
    current_strok_number -= 1  # сейчас равен 5

    # добавляем во все строки в начало столько пробелов , сколько всего строк, минус текущая строка, минус 1
    text += str(' ' * (strok_vsego - current_strok_number - 1))
    # увеличиваем цифры на 1 и набиваем строку
    current_cifra = 0
    while current_cifra <= current_strok_number:
        current_cifra += 1
        text += str(current_cifra)

    # добавляем во все строки в конец пробелов столько, сколько всего строк, хотя это не обязательно
    # text += str(' ' * (strok_vsego))


    text += '\n'  # добавляем в конце перенос строки


print(text)

# строка 5 руками для теста
# print(123454321)
