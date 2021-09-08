minimum_age = 30
minimum_balance = 350

user_age = input("Сколько вам лет?")
user_age = int(user_age)
difference_age = minimum_age - user_age

if user_age >= minimum_age:
	print("Возраст у вас подходящий!")
else: 
	print("Вы ещё слишком молод, приходите через", difference_age, " лет.")
if user_age > minimum_age:
	user_balance = input("Сколько у вас есть деняк?")
	user_balance = int(user_balance)
	difference_balance = minimum_balance - user_balance
	
	if user_age >= minimum_age and user_balance >= minimum_balance:
		print("Всего хватает, проходите, деньги спишуться автоматически!")
	elif user_age >= minimum_age and user_balance < minimum_balance:
		print("Но денег слишком мало, приходите когда получите ещё", difference_balance, "!")
