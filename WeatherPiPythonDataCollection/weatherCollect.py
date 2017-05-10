import pyowm as OWM
import time
import os
import sys
import Adafruit_DHT
owm = OWM.OWM('your_api_key_here')
cwd = os.getcwd()
os.chdir('..')
os.chdir('WeatherPiJavaGui')
msRunning=0
weather2 = owm.weather_at_place("your_location_here")
weather3 = weather2.get_weather()
weather4 = weather3.get_temperature('celsius')
weather5 = weather4['temp']
while True:
    if msRunning % 360000 == 0:
        weather2 = owm.weather_at_place("your_location_here")
        weather3 = weather2.get_weather()
        weather4 = weather3.get_temperature('celsius')
        weather5 = weather4['temp']
        msRunning = 0
    #humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
    file = open('temperatures.txt','r+')
    file.truncate()
    #if humidity is not None and temp is not None and weather5 is not None:
    file.write(''+'%.2f'%weather5+','+'%.2f'%temperature)
    print(weather5)
    file.close()
    msRunning=msRunning+10000
    time.sleep(10)
done
