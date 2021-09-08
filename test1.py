minimum_age = 30
minimum_balanc = 650

user_age = input("Сколько вам лет?")
use_balanc = input("Сколько у вас есть деняк?")

int(user_age)
int(use_balanc)

if user_age >= minimum_age:
	print("Возраст у вас подходящий!")
else: 
	print("Вы ещё слишком молод, приходите позже.")
if user_age >= minimum_age and use_balanc >= minimum_balanc:
	print("Всего хватает, проходите, деньги спишуться автоматически!")
elif user_age >= minimum_age and use_balanc < minimum_balanc:
	print("Но денег слишком мало, приходите когда будут!")
