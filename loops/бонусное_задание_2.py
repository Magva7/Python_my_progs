all_strok = 9
current_cifra = 1
current_stroka = 1
text = ''

# верхняя часть
while current_stroka <= all_strok:  # пока текущая строка < или равна всего строк
    text += ' ' * all_strok  # добавляем в начало каждой строки столько пробелов, сколько всего строк:

    # далее добавляем цифры на уменьшение, первая цифра = текущей строке и так до 1
    current_cifra = current_stroka
    while current_cifra >= 1:  # до тех пор, пока текущая цифра не будет > или = 1
        text += str(current_cifra)  # добавляем цифру, переведенную в str
        current_cifra -= 1 # каждую итерацию уменьшаем текущую цифру на 1
    text += '\n'  # добавляем в конце перенос строки
    current_stroka += 1  # когда маленький цикл отработал, увеличиваем текущую строку на 1

# нижняя часть - сначала обнуляем переменные, теперь у нас текущая строка = всего строк и по строкам идем на уменьшение
current_cifra = 1
current_stroka = all_strok
# print(current_stroka)

# оборачиваем все в цикл
while current_stroka >= 1:  # пока текущая строка > или = 1
    # добавляем в начало строки столько пробелов, сколько у нас всего строк, минус текущая строка
    text += ' ' * (all_strok - current_stroka)

    # далее добавляем цифры на уменьшение, первая цифра всегда = 1
    current_cifra = 1

    # потом добавляем цифры, пока текущая цифра меньше или равна текущей строке
    while current_cifra <= current_stroka:
        text += str(current_cifra)
        current_cifra += 1  # каждую итерацию увеличиваем цифру на 1

    # в конце любой строки добавляем столько пробелов, сколько всего строк
    text += ' ' * all_strok
    current_stroka -= 1  # когда маленький цикл отработал, уменьшаем текущую строку на 1
    # print(current_stroka)

    text += '\n'
print(text)
