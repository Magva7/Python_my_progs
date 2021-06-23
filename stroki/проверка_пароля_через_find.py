password = 'qW545442'

zaglavnie_bukby = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cifry = '1234567890'
strochnie_bukvy = 'abcdefghijklmnopqrstuvwxyz'
specsimvoly = '!@#$%^&*()-+'

# для последующей проверки, есть ли в пароле некорректный символ, для этого складываем все наши строки в одну и
# потом будем делать поиск по ней
all_stroki = zaglavnie_bukby + strochnie_bukvy + cifry +specsimvoly

text = 'Слабый пароль. Рекомендации: '  # изначальный текст

# счетчики
count_zaglav_bukv = 0
count_strochn_bukv = 0
count_cifr = 0
count_spec_simvol = 0
count_error_symvols = 0

# логика следующая - у нас есть строка с паролем, есть условия и есть конечное сообщение, которое мы будем выводить,

# берем первый символ пароля и смотрим, есть ли он в списке заглавных букв, строчных букв и т.д., потом переходим к
# следующему символу

current_passw_symbol_index = 0  # индекс текущего символа в пароле, который проверяем

while current_passw_symbol_index < len(password):
    current_passw_symbol = password[current_passw_symbol_index]  # текущий символ пароля, который проверяем

    if zaglavnie_bukby.find(current_passw_symbol) != -1:  # если текущий символ нашелся в заглавных буквах
        count_zaglav_bukv += 1  # увеличиваем счетчик заглавных букв

    if strochnie_bukvy.find(current_passw_symbol) != -1:  # если текущий символ нашелся в заглавных буквах
        count_strochn_bukv += 1  # увеличиваем счетчик строчных букв

    if cifry.find(current_passw_symbol) != -1:  # если текущий символ нашелся в цифрах
        count_cifr += 1  # увеличиваем счетчик цифр

    if specsimvoly.find(current_passw_symbol) != -1:  # если текущий символ нашелся в спецсимволах
        count_spec_simvol += 1  # увеличиваем счетчик спецсимолов

    current_passw_symbol_index += 1  # увеличиваем индекс, чтобы перейти в следующей итерации к след символу в пароле

if len(password) < 12:  # если длина строки меньше 12 символов
    text += 'увеличить число символов на '  # добавляем текст в нашу переменную
    text += str(12-len(password))  # добавляем текст - на сколько символов надо увеличить длину пароля

# дальше проверяем наши счетчики и набиваем сообщение
elif count_zaglav_bukv == 0:  # если заглавных букв нет, то
    text += ', добавить 1 заглавную букву'  # добавляем в текст сообщение

elif count_strochn_bukv == 0:  # если строчных букв нет, то
    text += ', добавить 1 строчную букву'  # добавляем в текст сообщение

elif count_cifr == 0:  # если цифр нет, то
    text += ', добавить 1 цифру'  # добавляем в текст сообщение

elif count_spec_simvol == 0:  # если спецсимволов нет, то
    text += ', добавить 1 спецсимвол'  # добавляем в текст сообщение

elif count_error_symvols != 0:  # если есть хотя бы 1 некорректный символ
    text = 'Ошибка. Запрещенный спецсимвол'  # Меняем собщение

else:
    text = 'Сильный пароль.'

print(text)