dlina = int(input())
vverh = int(input())
vniz = int(input())
# dlina = 10
# vverh = 5
# vniz = 2
raznica = vverh - vniz
day = 1

count = 0
while((count + vverh) <= dlina):
	count = count + raznica
	day = day + 1
print(day)
