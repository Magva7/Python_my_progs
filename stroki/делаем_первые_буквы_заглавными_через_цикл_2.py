text = 'иванов иван иваныч иванько'
# text = 'a1 2b  3   abc d3e r2D2'

dlina = len(text)
# переводим в массив
text_list = list(text)

# проверяем, что первый символ не пробел, и что это буква, если да, то делаем букву большой
if text_list[0] != ' ' and text_list[0].isalpha:
    text_list[0] = text_list[0].upper()

# перебираем символы по очереди, как доходим до пробела, проверяем следующий символ, если буква - делаем большой
i = 0
while i < dlina:
    if text_list[i] == ' ':
        if text_list[i+1].isalpha():
            text_list[i+1] = text_list[i+1].upper()
    # print(text_list[i])
    i += 1

text = ''.join(text_list)  # переводим обратно в строку
print(text)