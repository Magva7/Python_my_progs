# a = int(input())
# b = int(input())
# c = int(input())

a = 4
b = 5
c = 3
print(a, b, c)

if a > b:
    if a > c:  # т.е. a самое здоровое, c<b<a ставим его в конец
        (a, c) = (c, a)
        if b > c
            (b, c) = (c, b)
    elif a < c:  # т.е. b<a<c


elif a < b:
    if a > c:  # т.е. c<a<b
        (a, c) = (c, a)
        if b > c
            (b, c) = (c, b)




# if a > b:
#     (a, b) = (b, a)
#     print('тест 1 - поменяли местами a и b:', a, b, c)
#     if b > c:
#         (b, c) = (c, b)
#         print('тест 2 - поменяли местами b и c:', a, b, c)
#         if a > c:
#             (a, c) = (c, a)
#             print('тест 3 - поменяли местами a и c:', a, b, c)
#         else:  # a < c
#             if a > b:
#                 (a, b) = (b, a)
#                 print('тест 4 - еще раз поменяли местами a и b:', a, b, c)
#                 if b > c:
#                     (b, c) = (c, b)
#                     print('тест 5 - еще раз поменяли местами b и c:', a, b, c)
#                     if a > c:
#                         (a, c) = (c, a)
#                         print('тест 6 - поменяли местами a и c:', a, b, c)
#                     else:
#                         print(a, b, c)
#                 else:
#                     print(a, b, c)
#             else:
#                 print(a, b, c)
#     else:
#         print(a, b, c)
#     # else:  # b < c
#     #     if a > c:
#     #         (a, c) = (c, a)
#     #         print('тест 3 - поменяли местами a и c:', a, b, c)
#     #     else:  # a < c
#     #         if a > b:
#     #             (a, b) = (b, a)
#     #             print('тест 4 - еще раз поменяли местами a и b:', a, b, c)
#     #             if b > c:
#     #                 (b, c) = (c, b)
#     #                  print('тест 5 - еще раз поменяли местами b и c:', a, b,
#     #                           c)
#     #                 if a > c:
#     #                     (a, c) = (c, a)
#     #                      print('тест 3 - поменяли местами a и c:', a, b, c)
#     #                 else:
