# print('1', '2', '3', sep=' + ', end=' ')
# print()
# print('=', 1 + 2 +3)

jeka_dolg = "400"
got_dolg = "700"

my_file = open("dolgi.txt", "w") #открываем файл
my_file.write("Долг Готяры: ") #Записываем в файл текст
my_file.write(got_dolg)#Записываем в файл значение переменной
my_file.write("\nДолг Жеки: ") #/n - перенос строки
my_file.write(jeka_dolg)
my_file.close()