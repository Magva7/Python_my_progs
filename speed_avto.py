speed = int(input("Введите скорость автомобиля: "))
porog = 60
if(speed > porog):
    print("Превышаем!")

    if(speed>100):
        print("И куда летим?")
else:
    if(speed<0):
        print("Введите скорость больше нуля")
    else:
        if(speed==0):
            print("Стоим!")
        else:
            print("Нормально, скорость в пределах")
        
