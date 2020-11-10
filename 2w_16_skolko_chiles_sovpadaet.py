a = int(input())
b = int(input())
c = int(input())

# a = 1
# b = 2
# c = 2

sovpad = 0

if a == b:
    sovpad = 2
    if a == c:
        sovpad = 3
elif a == c:
    sovpad = 2
elif b == c:
    sovpad = 2

print(sovpad)
