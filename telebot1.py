import pyowm
import telebot

owm = pyowm.OWM( "8e9ccecaf16992a4741dada8f947c9b2" )
bot = telebot.TeleBot( "1918795668:AAFr7Ai04OXAoq5m08wbU27fqeXV-3swYXI" )

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.got_temperature('celsius')["temp"]

	answer = "В городе " + message.text + "сейчас " + w.get_detailed_status() + "\n"
	answer = answer + "Температура сейчас в районе " + str(temp) + "\n\n"

	if temp < 10:
		answer = answer + " Оч холодно, одевайся в шубу." 
	elif temp < 20:
		answer = answer + "Сейчас прохладно, одевайся потеплее." 
	else:
		answer = answer + "Температура норм, иди как хочешь." 

	bot.sand_message(message.chat.id, answer)

bot.polling( none_stop = True )