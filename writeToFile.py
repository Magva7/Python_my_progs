# print('1', '2', '3', sep=' + ', end=' ')
# print()
# print('=', 1 + 2 +3)

jekaDebt = "100"
gotDebt = "500"

my_file = open("some.txt", "w") #open txt file
my_file.write("Долг Готяры: ") #write in txt file
my_file.write(gotDebt)
my_file.write("\nДолг Жеки: ") #/n - line break
my_file.write(jekaDebt)
my_file.close()