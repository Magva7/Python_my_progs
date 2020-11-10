k = int(input())
# k = 8
if k < 3:
    print('NO')
elif (k % 3) == 0:
    print('YES')
elif (k % 5) == 0:
    print('YES')
elif (k % 8) == 0:
    print('YES')
elif ((k - 5) % 3) == 0:
    print('YES')
elif ((k - 3) % 5) == 0:
    print('YES')
else:
    print('NO')
