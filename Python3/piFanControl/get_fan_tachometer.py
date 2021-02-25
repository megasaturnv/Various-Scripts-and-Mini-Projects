#!/usr/bin/python3

# MegaSaturnv 2019-07-23

import time
import RPi.GPIO as GPIO

FAN_ENABLE_PIN = 17
FAN_TACHOMETER_PIN = 18
PWM_FREQUENCY = 50;

def cleanupGPIO():
	global fanPwm

	fanPwm.ChangeDutyCycle(0)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(FAN_ENABLE_PIN, GPIO.OUT)
	GPIO.output(FAN_ENABLE_PIN, GPIO.LOW)
	GPIO.setup(FAN_ENABLE_PIN, GPIO.IN)

	GPIO.setup(FAN_TACHOMETER_PIN, GPIO.IN)

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
	GPIO.setup(FAN_TACHOMETER_PIN, GPIO.IN)

	fanPwm = GPIO.PWM(FAN_ENABLE_PIN, PWM_FREQUENCY)

	dutyCycle = 100
	dutyCycleSlowest = 100
	dutyCycleSpeeds = range(100, 0, -5)
	fanPwm.start(dutyCycle)

	getFanSpinning(fanPwm)

	print("Setting fan duty cycle to 100%")
	fanPwm.ChangeDutyCycle(100)
	time.sleep(5)

	running = True
	while running:
		for i in range(0, 200):
			print( GPIO.input(FAN_TACHOMETER_PIN), end='' )
			time.sleep(0.0075)
		print('')
		if input('Continue? [y/N]').lower() == 'n':
			running = False

	fanPwm.ChangeDutyCycle(0)

except KeyboardInterrupt:
	print("KeyboardInterrupt detected!")
	cleanupGPIO()
except Exception as e:
	print(e)
	cleanupGPIO()
except:
	print("Other exception!")
	cleanupGPIO()
else:
	print("Else")
	cleanupGPIO()

print("End")
cleanupGPIO()

