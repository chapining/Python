user_money = 500

def waste_money():
	global user_money 
	user_money -= 100


waste_money()
print(user_money)