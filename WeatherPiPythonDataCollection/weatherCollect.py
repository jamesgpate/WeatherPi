import pyowm as OWM
import time
import os
owm = OWM.OWM('388dfaa254e9e7cade977c9fc818581e')
cwd = os.getcwd()
os.chdir('..')
os.chdir('WeatherPiJavaGui')
msRunning=0
weather2 = owm.weather_at_place("College station, us")
weather3 = weather2.get_weather()
weather4 = weather3.get_temperature('celsius')
weather5 = weather4['temp']
while True:
    if msRunning % 360000 == 0:
        weather2 = owm.weather_at_id(4682464)
        weather3 = weather2.get_weather()
        weather4 = weather3.get_temperature('celsius')
        weather5 = weather4['temp']
        msRunning = 0
    file = open('temperatures.txt','r+')
    file.truncate()
    file.write(''+'%.2f'%weather5+',0')
    print(weather5)
    file.close()
    msRunning=msRunning+10000
    time.sleep(10)
done
