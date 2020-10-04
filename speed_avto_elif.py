speed = int(input("Введите скорость автомобиля: "))
porog = 60

if(speed>100):
    print("И куда летим?")
elif(speed > porog):
    print("Превышаем!")
elif(speed<0):
    print("Введите скорость больше нуля")
elif(speed==0):
    print("Стоим!")
else:
    print("Нормально, скорость в пределах")
        
