import os
import random as rnd

text = """
Здравствуйте, это игра на тему "три поездки Ильи Муромца"
А если проще, то камень и три развилки
"""
print(text)
input("НАЖМИТЕ Enter, ЧТОБЫ ПРОДОЛЖИТЬ \n")

os.system("cls")

text = """
В этой игре вам будет даваться выбор и цифрами вы должны будете его совершить
Вы играете за Илью Муромца, игра видётся от первого лица
Примечание: использовать только цифры которые о которых сказано в вопросе.
"""
print(text)
input("НАЖМИТЕ Enter, ЧТОБЫ НАЧАТЬ ИГРУ \n")

os.system("cls")

text = """
Вы едите по не изведоной до этого тропе и встречаете горюч-камень,
а на камне надпись написана: «Если прямо ехать – убиту быть,
направо ехать – женату быть, а налево ехать – богатому стать»

Что делать: 1 Ехать прямо; 2 Ехать направо; 3 Ехать налево
"""

print(text)

choice = ""
level = "0"
game = True

while choice not in ("1", "2", "3"):
    choice = input("вариант ответа: ")

# text = "Выбран неверный вариант ответа!"
# print(text)

level = level + choice # 01 02 03

if level == "01":
    os.system("cls")

    text = """
    – Мне, старому, в бою смерть не писана. Дай поеду, где убиту быть.
    """
    print(text)

elif level == "02":

    os.system("cls")

    text = """
    -Жена это не плохо, поехали Бурушка!
    """

    print(text)

elif level == "03":

    os.system("cls")

    text = """
    -Богатство это хорошо, но сыр только в мышеловке! Посмотрим, что там такое.
    """

    print(text)

choice = ""
while choice not in ("1", "2"):
    os.system("cls")
    #TODO: доделай вопрос!
    choice = input("""
Куда дальше???
1 или 2
вариант ответа: 
        """)

level = level + choice # 011 012 021 022 031 032

if level == "011":
    os.system("cls")
    #TODO: историю доделай!
    print("""
ты встретил казаков, хочешь сыграть в кости на мешок денег, в нём 100 золотых, или подраться?
        """)
    choice = ""
    while 

elif level == "012":
    os.system("cls")
    print("012")

elif level == "021":
    os.system("cls")
    print("021")
elif level == "022":
    os.system("cls")
    print("022")

elif level == "031":
    os.system("cls")
    print("031")
else:
    os.system("cls")
    print("032")
    
