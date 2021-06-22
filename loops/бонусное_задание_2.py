all_strok = 5
current_cifra = 1
current_stroka = 1
text = ''

# верхняя часть - оборачиваем все в цикл
while current_stroka <= all_strok:  # пока текущая строка < или равна всего строк
    text += 'X' * all_strok  # добавляем в начало каждой строки столько пробелов, сколько всего строк:

    # далее добавляем цифры на уменьшение, первая цифра = текущей строке и так до 1
    current_cifra = current_stroka
    while current_cifra >= 1:  # до тех пор, пока текущая цифра не будет > или = 1
        text += str(current_cifra)  # добавляем цифру, переведенную в str
        current_cifra -= 1 # каждую итерацию уменьшаем текущую цифру на 1
    text += '\n'  # добавляем в конце перенос строки
    current_stroka += 1
print(text)
