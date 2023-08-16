import RPi.GPIO as GPIO
from time import sleep
import time
import os
from twilio.rest import Client
import gps as loc

#Disable warnings (optional)
buttonPin = 19
GPIO.setmode(GPIO.BCM) # choose BCM or BOARD numbering schemes. I use BCM  
GPIO.setup(13, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

account_sid = "AC174a0802c2e63396a3807e4d26b6bc88"
auth_token = "32f7d8cf2a5d76bc4cdd2504d3df0765"
client = Client(account_sid, auth_token)

def buz():
 n =1 
 p = GPIO.PWM(13, 200000)    # create an object p for PWM on port 25 at 50 Hertz  
 p.start(50)             # start the PWM on 70 percent duty cycle  
 print("Buzzer working")
 p.ChangeFrequency(20000)
 latitude, longitude = loc.gps_start()
 message = client.messages.create(
 body="Person in danger. Call to check\nlatitude:"+ latitude +"\nlongitude:"+longitude+"\n",
 from_="+19498326594",
 to="+918529691031" )
 print(message.sid)
 
 while n==1:
   buttonState = GPIO.input(buttonPin)
   if buttonState == False:
      message = client.messages.create(
      body="Help not needed",
      from_="+19498326594",
      to="+918529691031" )
      print(message.sid)
      p.stop()
      
      n=0
       
def stop():
   p.stop()
