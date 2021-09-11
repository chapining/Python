"""
	до 100г - кетчуп, не берём
	до 200г - мелкие
	до 500г - средние
	от 500г - большие
"""

tomato_kethup = 100
tomato_small = 200
tomato_medium = 500

tomato_weight = int(input("сколько весит этот помидор?(в г.) "))

if tomato_weight < tomato_kethup:
	print("этот на кетчуп!" )
elif tomato_weight < tomato_small:
	print("этот маленький!")
elif tomato_weight < tomato_medium:
	print("этот средний")
elif tomato_weight >= tomato_medium:
	print("этот большой")
else:
	print("НЕ ВЕРНЫЙ ВАРИАНТ ВЕСА!")
