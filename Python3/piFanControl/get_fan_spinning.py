#!/usr/bin/python3

# MegaSaturnv 2019-07-23

import time
import RPi.GPIO as GPIO

FAN_ENABLE_PIN = 17
PWM_DUTY_CYCLE = 99
PWM_FREQUENCY = 0.5

def cleanupGPIO():
	global fanPwm

	fanPwm.ChangeDutyCycle(0)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(FAN_ENABLE_PIN, GPIO.OUT)
	GPIO.output(FAN_ENABLE_PIN, GPIO.LOW)
	GPIO.setup(FAN_ENABLE_PIN, GPIO.IN)
	GPIO.setup(FAN_TACHOMETER_PIN, GPIO.IN)
	GPIO.cleanup()

try:
	GPIO.setmode(GPIO.BCM)
	#GPIO.setmode(GPIO.BOARD)

	GPIO.setup(FAN_ENABLE_PIN, GPIO.OUT)
	#GPIO.setup(FAN_TACHOMETER_PIN, GPIO.IN)

	fanPwm = GPIO.PWM(FAN_ENABLE_PIN, PWM_FREQUENCY)

	fanPwm.start(PWM_DUTY_CYCLE)

	time.sleep(3)

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

