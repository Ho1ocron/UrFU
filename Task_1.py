from random import randint

value = randint(1, 100)
print(value)
for i in range(3):
    s = int(input("Угадай число: "))
    if s == value:
        print("Вы угадали число!")
        break
    else:
        
        if i == 1:
            if value % 2 == 0:
                print("Вы не угадали, по пробуйте еще раз. Число является четным")
            else:
                print("Вы не угадали, по пробуйте еще раз. Число является нечетным")
        elif i == 2:
            print(f"Вы не угадали, ваши попытки закончились. Загаданное число: {value}")
        else:
            print("Вы не угадали, по пробуйте еще раз")


