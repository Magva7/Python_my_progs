# обрабатываем строковые данные и возвращаем их с первыми заглавными буквами в каждом слове.

# stroka = 'иванов иван иваныч иванько'
# stroka = 'ivan ivanov'
# stroka = 'can    you   solve  it?'
# stroka = 'abraсadabra'
stroka = 'a1 2b  3   abc d3e r2D2'

stroka_list = list(stroka)  # записываем нашу строку в список, т.к. нам потом надо будет в ней менять символы,
# а в питоне строку менять нельзя, это неизменяемый тип, зато можно перевести строку в список, поменять, что надо,
# а потом перевести получившийся список обратно в строку
# После обработки данных код должен выводить: "Иванов Иван"
# логика следующая сначала проверяем, что у нас в первом символе именно буква, если буква, то всегда делаем заглавным
# первый символ,
# потом циклом пробегаемся по всем символам, ищем, на каком месте строки у нас пробел, потом делаем символ,
# который идет за пробелом заглавным

if stroka_list[0].isalpha() == True:  # проверяем, что первый символ это буква, если да, то
    stroka_list[0] = stroka_list[0].upper()  # делаем его большим

# дальше у нас цикл - увеличиваем символы, после пробела
# пробегаем во всем символам
current_symbol_index = 1
while current_symbol_index < len(stroka):
    if (stroka_list[current_symbol_index] == ' '):  # если текущий символ пробел
        if stroka_list[current_symbol_index + 1].isalpha() == True:  # тогда проверяем что следующий символ, это буква
            stroka_list[current_symbol_index + 1] = stroka_list[current_symbol_index + 1].upper()  # делаем его большим
    current_symbol_index += 1

stroka = ''.join(stroka_list)  # записываем получившийся список обратно в строку
# print(stroka_list)  # результат в виде списка для теста
print(stroka)  # результат в виде строки
