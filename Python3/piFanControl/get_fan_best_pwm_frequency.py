#!/usr/bin/python3

# MegaSaturnv 2019-07-23

import time
import RPi.GPIO as GPIO

FAN_ENABLE_PIN = 17
FAN_TACHOMETER_PIN = 18
PWM_FREQUENCY = 50;
PWM_DUTYCYCLE = 50;

def getTemp():
    cpu_temp_file = open("/sys/class/thermal/thermal_zone0/temp" ,"r")
    temperature = str(cpu_temp_file.readline())+"\b"
    temperature = float(temperature.rstrip("\n\x08"))
    #temperature= float(temperature.rstrip("\x08"))
    return(temperature/1000)

def cleanupGPIO():
	global fanPwm

	fanPwm.ChangeDutyCycle(0)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(FAN_ENABLE_PIN, GPIO.OUT)
	GPIO.output(FAN_ENABLE_PIN, GPIO.LOW)
	GPIO.setup(FAN_ENABLE_PIN, GPIO.IN)
	#GPIO.setup(FAN_TACHOMETER_PIN, GPIO.IN)
	GPIO.cleanup()

def getFanSpinning(fanPwm):
	print("Getting fan spinning")
	fanPwm.ChangeDutyCycle(99)
	fanPwm.ChangeFrequency(0.5)
	time.sleep(5)
	fanPwm.ChangeDutyCycle(100)
	fanPwm.ChangeFrequency(PWM_FREQUENCY)

try:
	GPIO.setmode(GPIO.BCM)
	#GPIO.setmode(GPIO.BOARD)

	GPIO.setup(FAN_ENABLE_PIN, GPIO.OUT)
	#GPIO.setup(FAN_TACHOMETER_PIN, GPIO.IN)

	fanPwm = GPIO.PWM(FAN_ENABLE_PIN, PWM_FREQUENCY)

	frequency = 50

	fanPwm.start(PWM_DUTYCYCLE)

	getFanSpinning(fanPwm)

	for i in dutyCycleSpeeds:
		print("Setting fan duty cycle to " + str(i))
		fanPwm.ChangeDutyCycle(i)
		q = input("Is the fan spinning?")
		if q.lower() == "n" or q.lower() == "no":
			dutyCycleSlowest = dutyCycleSpeeds[  max([0, dutyCycleSpeeds.index(i) - 1])  ]
			print("Slowest acceptable duty cycle is " + str(dutyCycleSlowest))
			break

	getFanSpinning(fanPwm)
	print("Setting fan duty cycle to " + str(dutyCycleSlowest))
	fanPwm.ChangeDutyCycle(dutyCycleSlowest)

	time.sleep(20)

except KeyboardInterrupt:
	print("KeyboardInterrupt detected!")
	cleanupGPIO()
except:
	print("Other exception!")
	cleanupGPIO()
else:
	print("Else")
	cleanupGPIO()

print("End")
cleanupGPIO()

