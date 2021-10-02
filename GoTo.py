import os
import random as rnd
import math

def  show_location_home():
    #описыва локацию
    os.system("cls")
    print("Ты у себя дома")
    print("1 - в казино")
    print("2 - ничего")

    #спросить пользователя
    choice = ""
    while choice not in ("1", "2"):
        #TODO: доделай вопрос!
        choice = input("Куда дальше? \n 1 или 2 \n вариант ответа:")
    #проверить ответ пользователя
    if choice == "1":
        show_location_casino()
    elif choice == "2":
        show_location_home()


def show_location_casino():
    #описыва локацию
    global counter
    os.system("cls")
    print("Ты в казино")
    print("1 - домой")
    print("2 - ждать")
    print("3 - играть")
    choice = ""
    while choice not in ("1", "2", "3"):
        #TODO: доделай вопрос!
        choice = input("Куда дальше? \n 1, 2 или 3 \n вариант ответа:")
    #проверить ответ пользователя
    if choice == "1":
        show_location_home()
    elif choice == "2":
        show_location_casino()
    elif choice == "3":
        while counter != 0:
            counter -= 1
            show_gamble()
            if user_money <= 0:
                break



def show_gamble():
    global user_money
    loss = 0.9
    win = 1.1
    #input(f"У вас на входе {user_money}, нажмите ENTER")
    user_dice = rnd.randint(2, 12)
    casino_dice = rnd.randint(2, 12)
    print(f"Вы бросили кости, выпало {user_dice}")
    print(f"Казино бросило кости, выпало {casino_dice}")
    if user_dice > casino_dice:
        if isinstance(user_money, int):
            user_money = int(user_money * win)
        else:
            math.ceil(user_money * win)
        print("Вы победили")
    elif user_dice < casino_dice:
        user_money = int(math.ceil(user_money * loss))
        print("Вы проиграли")
    elif user_dice == casino_dice:
        print("НиЧьЯ")
    else:
        print("ощибка")
    print(f"У вас теперь  {user_money}")
    print(f"прошло{100000-counter}")
    #input("Нажмите ENTER, чтобы вернуться в казино")
    


# игра началась здесь
counter = 100000
user_name = "Вася"
user_money = 5000
show_location_home()
