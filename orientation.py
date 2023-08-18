import time
import board
import busio
import adafruit_adxl34x		
from time import sleep          
import buzzerf as b
import os
from twilio.rest import Client

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)


    
accelerometer.enable_freefall_detection(threshold=15, time=20)
accelerometer.enable_motion_detection(threshold=18)
accelerometer.enable_tap_detection(tap_count=1, threshold=20, duration=50, latency=20, window=255)
n=1
while True:

        print(accelerometer.acceleration)
    
        if accelerometer.events['freefall'] == True:
            print("Dropped: %s"%accelerometer.events["freefall"])
            print("Tapped: %s"%accelerometer.events['tap'])
            print("Motion detected: %s"%accelerometer.events['motion'])
            print("okay")
            b.buz()
            
        
        time.sleep(0.5)




