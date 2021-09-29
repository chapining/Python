import os
import random as rnd

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
        choice = input("""Куда дальше?
1 или 2
вариант ответа:""")
    #проверить ответ пользователя
    if choice == "1":
        show_location_casino()
    elif choice == "2":
        show_location_home()


def show_location_casino():
    #описыва локацию
    os.system("cls")
    print("Ты в казино")
    print("1 - домой")
    print("2 - ждать")
    print("3 - играть")
    choice = ""
    while choice not in ("1", "2", "3"):
        #TODO: доделай вопрос!
        choice = input("""Куда дальше?
1, 2 или 3
вариант ответа:""")
    #проверить ответ пользователя
    if choice == "1":
        show_location_home()
    elif choice == "2":
        show_location_casino()
    elif choice == "3":
        show_gamble()


def show_gamble():
    user_dice = rnd.randint(2, 12)
    casino_dice = rnd.randint(2, 12)
    print(f"Вы бросили кости, выпало {user_dice}")
    print(f"Казино кости, выпало {casino_dice}")
    if user_dice > casino_dice:
        print("Вы победили")
    elif user_dice < casino_dice:
        print("Вы проиграли")
    elif user_dice == casino_dice:
        print("НиЧьЯ")
    else:
        print("ощибка")
    input("Нажмите ENTER, чтобы вернуться в казино")
    show_location_casino()


show_location_home()