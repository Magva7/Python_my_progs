a = int(input())
# a = 8
stepen = 0

while 2**stepen <= a:
    print(2**stepen, end=' ')
    stepen = stepen + 1
