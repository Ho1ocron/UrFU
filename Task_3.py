from random import randint


turn = {
    1: "Камень",
    2: "Бумага",
    3: "Ножницы"
}

user_victory = 0
bot_victory = 0
for i in range(3):
    bot = randint(1, 3)
    usr = int(input("Введите вход от 1 до 3: 1 - Камень, 2 - Ножницы, 3 - Бумага: "))
    if usr - bot == 1 or usr - bot == -2:
        user_victory += 1
        print(f"\nБот выкидывает '{turn[bot]}'")
        print("Пользователь выигрывает этот раунд\n")
    elif bot - usr == 1:
        bot_victory += 1
        print(f"\nБот выкидывает '{turn[bot]}'")
        print("Пользователь проигрывает этот раунд\n")
    else:
        print(f"\nБот выкидывает '{turn[bot]}'")
        print("Раунд заканчивается ничьей\n")

if user_victory > bot_victory:
    print("Выиграл Пользователь")
elif bot_victory > user_victory:
    print("Выигрывает Бот")
else:
    print("Ничья")
    