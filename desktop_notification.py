 
import datetime # to read present date  
import time # to suspend the execution for a specific time  
import weather_app as w  
from plyer import notification
from win10toast import ToastNotifier
  
# create an object to ToastNotifier class
n = ToastNotifier()
temp = w.temperature,  
feels = w.feels_like,  
hum = w.humidity,  
min = w.temp_min,
max = w.temp_max
message = "Temperature :" + str(temp)  + "\nFeels like: " + str(feels)  + "\nHumidity: " + str(hum) + "\nMinimum Temperature:" + str(min)  +"\nMaximum Temperature: "  + str(max)
  
n.show_toast("Weather App", message, duration = 30,
 icon_path ="weather.png")
"""while(True):  
    notification.notify( 
        title = "Weather : {}".format(datetime.date.today()),
        message = "Temperature : {temp}\nFeels like: {feels}\nHumidity: {hum}\nMinimum Temperature: {min}\nMaximum Temperature: {max}".format(  
        temp = w.temperature,  
        feels = w.feels_like,  
        hum = w.humidity,  
        min = w.temp_min,
        max = w.temp_max),
        timeout  = 30  
        )  
"""
#notification for everday
#time.sleep(600 * 600 * 24)