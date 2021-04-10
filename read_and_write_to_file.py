my_file = open("dolgi.txt", "r+")  # открываем файл

jeka_dolg = int(my_file.readline())  # записываем в переменную jeka_dolg
# содержимое первой строки, которое перевели в int
# got_dolg = int(my_file.readline(20))  #тоже самое, 2-ая строка
print('=============================')
print('|  Считали из файла         |')
print('|  Долг Жеки:   ', jeka_dolg, '      |')
# print('|  Долг Готяры: ', got_dolg, '      |')
print('=============================')

jeka_dolg += 100  # добавляем долг Жеки
# got_dolg -= 100  # вычитаем долг Готяры

print('|  Добавили/списали долги   |')
print('|  Долг Жеки:   ', jeka_dolg, '      |')
# print('|  Долг Готяры: ', got_dolg, '      |')
print('=============================')

my_file.seek(0, 0)
my_file.write(str(jeka_dolg))
my_file.write("\n")
# my_file.write(str(got_dolg))#Записываем в файл значение переменной
print('|  Записали данные в файл   |')
print('=============================')
# my_file.close()
