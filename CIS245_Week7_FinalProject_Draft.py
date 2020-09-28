import json
import requests

while True:
    print('Welcome to the weather app!')
    userZip = input('Please enter your zip code to see your current weather or enter "q" to quit: ')

    if userZip == 'q':
        print('Thank you for stopping by!')
        break
    else:
        userZip = int(userZip)
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={userZip},us&units=imperial&appid=83a1ade6e787fb0206dc4f8bcfed4fda')

    returnedData = json.loads(r.text)

    currentTemp = returnedData['main']['temp']
    highTemp = returnedData['main']['temp_max']
    lowTemp = returnedData['main']['temp_min']
    humidity = returnedData['main']['humidity']
    windSpeed = returnedData['wind']['speed']
    currentConditions = returnedData['weather'][0]['description']

    currentWeatherConditions = {'current condition': currentConditions,
                            'current temperature': currentTemp,
                            'high temperature': highTemp,
                            'low temperature': lowTemp,
                            'humidity': humidity,
                            'wind speed': windSpeed,
    }

    for key in currentWeatherConditions:
        print("The {} is {}.".format(key,currentWeatherConditions[key]))

    restart = input('Would you like to check another zip code? Y/n --> ')
    if restart.upper() == 'Y':
        continue
    elif restart.upper() == 'N':
        print('Thank you for stopping by!')
        break


