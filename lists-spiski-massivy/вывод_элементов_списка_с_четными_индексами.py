# Задан список с числами. Напишите программу, которая выводит все элементы списка с четными индексами в виде нового
# списка.

# list1 = [1, 2, 3, 4, 5]
# list1 = [9, 4, 5, 2, 3]
# list1 = [7, 8]
list1 = [90, 45, 3, 43]

list2 = []

# print(len(list1))
# логика следующая - пробегаемся по всем элементам списка, если у элемента индекс четный, то добавляем его в новый
# список
i = 0  # индекс
while i < len(list1): # пробегаемся по всем элементам списка
    if (i % 2) == 0:  # если у элемента индекс четный
        list2.append(list1[i])  # добавляем текущий элемент в новый список
    i += 1  # идем к следующему

print(list2)