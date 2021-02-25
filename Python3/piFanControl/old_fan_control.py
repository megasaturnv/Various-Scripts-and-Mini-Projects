# MegaSaturnv 2019-07-15

import time
import RPi.GPIO as GPIO

##########################################################################

cpu_temp_file = open("/sys/class/thermal/thermal_zone0/temp" ,"r")

def getTemp():
    cpu_temp_file = open("/sys/class/thermal/thermal_zone0/temp" ,"r")
    temperature = str(cpu_temp_file.readline())+"\b"
    temperature = float(temperature.rstrip("\n\x08"))
    #temperature= float(temperature.rstrip("\x08"))
    return(temperature/1000)

#filename =
#mode =

##########################################################################

#time.sleep(15)
GPIO.setmode(GPIO.BOARD)
#pin 12 = GPIO 18
GPIO.setup(12, GPIO.OUT)
fan = GPIO.PWM(12,20)
fan.start(100)
spinning = False
while True:
    if spinning == False:
        print("Fan isn't spinning!")
        fan.ChangeDutyCycle(100)
        print("Fan at 100%")
        time.sleep(4)
        spinning = True
        print("Fan is spinning")
    print(" ")
    temp = getTemp()
    print("CPU temp: "+str(temp)+" C")
    if temp < 40.0:
        fan.ChangeDutyCycle(40)
        print("Fan at 40%")
    elif (temp >= 40.0) and (temp < 50.0):
        fan.ChangeDutyCycle(60)
        print("Fan at 60%")
    elif (temp >= 50.0) and (temp < 60.0):
        fan.ChangeDutyCycle(80)
        print("Fan at 80%")
    elif temp >= 60.0:
        fan.ChangeDutyCycle(100)
        print("Fan at 100%")
    else:
        fan.ChangeDutyCycle(100)
        print("Temperature read error. Fan at 100%")
    time.sleep(10)

#fan.ChangeDutyCycle(50)
#time.sleep(1)

#GPIO.output(pin, True)
#time.sleep(1)
#GPIO.output(pin, False)
#time.sleep(1)


fan.stop()
print("Done!")
GPIO.cleanup()
print("clean!")

####################################

# Don't try to run this as a script or it will all be over very quickly
# it won't do any harm though.
# these are all the elements you need to control PWM on 'normal' GPIO ports
# with RPi.GPIO - requires RPi.GPIO 0.5.2a or higher

#import RPi.GPIO as GPIO # always needed with RPi.GPIO

#GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM

#GPIO.setup(25, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port

#p = GPIO.PWM(25, 50)    # create an object p for PWM on port 25 at 50 Hertz
                        # you can have more than one of these, but they need
                        # different names for each port
                        # e.g. p1, p2, motor, servo1 etc.

#p.start(50)             # start the PWM on 50 percent duty cycle
                        # duty cycle value can be 0.0 to 100.0%, floats are OK

#p.ChangeDutyCycle(90)   # change the duty cycle to 90%

#p.ChangeFrequency(100)  # change the frequency to 100 Hz (floats also work)
                        # e.g. 100.5, 5.2

#p.stop()                # stop the PWM output

#GPIO.cleanup()          # when your program exits, tidy up after yourself
