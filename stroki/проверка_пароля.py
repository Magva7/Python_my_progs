password = 'qW@545435342'

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

# хотя бы 1 заглавная буква - сюда мы счетчик повесим - берем первый символ из нашей строки с заглавными буквами и
# проверяем, есть ли он в нашем пароле, если есть, то увеличиваем счетчик на 1 и переходим к следующему символу
# строке заглавных букв

current_passw_symbol_index = 0  # индекс текущего символа в пароле, который проверяем

# print(password[5])
while current_passw_symbol_index < len(password):
    current_passw_symbol = password[current_passw_symbol_index]  # текущий символ пароля, который проверяем
    # пробегаем по всему списку заглавных букв (на самом деле это строка)
    # print(current_passw_symbol_index)
    for current_symbol in zaglavnie_bukby:
        if current_passw_symbol == current_symbol:
            count_zaglav_bukv += 1  # увеличиваем счетчик заглавных букв
    # print('Заглавных букв: ', count_zaglav_bukv)  # выводим для теста

    # пробегаем по всему списку строчных букв
    for current_symbol in strochnie_bukvy:
        if current_passw_symbol == current_symbol:
            count_strochn_bukv += 1  # увеличиваем счетчик строчных букв
    # print('Строчных букв: ', count_strochn_bukv)  # выводим для теста

    # пробегаем по всему списку цифр
    for current_symbol in cifry:
        if current_passw_symbol == current_symbol:
            count_cifr += 1  # увеличиваем счетчик строчных букв
    # print('Цифр: ', count_cifr)  # выводим для теста

    # пробегаем по всему списку спецсимволов
    for current_symbol in specsimvoly:
        if current_passw_symbol == current_symbol:
            count_spec_simvol += 1  # увеличиваем счетчик строчных букв
    # print('Спецсимволов: ', count_cifr)  # выводим для теста

    # пробегаем по общей строке

    # print(current_passw_symbol)
    # print(all_stroki.find(current_passw_symbol))
    if all_stroki.find(current_passw_symbol) == -1:  # если текущий символ не нашелся в строке всех символов
        count_error_symvols += 1  # значит он ошибочный и мы увеличиваем счетчик ошибочных
        print('Ошибочный символ: ', current_passw_symbol)  # выводим для себя

    current_passw_symbol_index += 1  # увеличиваем индекс, чтобы перейти в следующей итерации к след символу в пароле

# Выводим счетчик для теста
# print('Длина: ', len(password))
# print('Заглавных букв: ', count_zaglav_bukv)  # выводим для теста
# print('Строчных букв: ', count_strochn_bukv)  # выводим для теста
# print('Цифр: ', count_cifr)  # выводим для теста
# print('Спецсимволов: ', count_cifr)  # выводим для теста

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