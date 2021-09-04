import pyowm

owm =  pyowm.OWM('8e9ccecaf16992a4741dada8f947c9b2',language = "RU")

place = input("В каком городе/стране?: ")
observation = owm.weather_at_place(place)
w = observation.get_weather()

print("В городе " + place + " сейчас " + 
w.get_detailed_status())
temp = w.get_temperature('celsius')['temp']
print('Температура в районе: ' + str(temp) + '°C')