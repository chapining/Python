def play_dice(bet):
	result = 0
	user_dice = random.randint(2,12)
	casino_dice = random.randint(2,12)
	if user_dice > casino_dice:
		result += bet
	elif user_dice == casino_dice:
		result = result
	else:
		result -= bet
	return result