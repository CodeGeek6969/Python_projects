import time  
from plyer import notification     #pip install plyer is a module that can be used to give notifications in python

if __name__== "__main__":
    while True:            
        notification.notify(
            title = "DRINK WATER NOW !!",                         #this is the title of the notification
            message= "drinking water is good for health",         #this is the message under the notification
            timeout= 10                                           #time until the notification stays 
        )

        time.sleep (15*15)                   
