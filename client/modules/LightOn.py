import re
import RPi.GPIO as GPIO
import time

WORDS = ["TURN", "ON", "LIGHT"]


def handle(text, mic, profile):

	GPIO.setmode(GPIO.BCM)
	
	#setting up the pin to be a pin that outputs information
	GPIO.output(18, GPIO.HIGH) #kita pake GPIO18
	
	#yg ini bisa buat off kayaknya
	#time.sleep(3)
	#GPIO.output(18, GPIO.LOW)
	#GPIO.cleanup()

	#suruh jasper jwb lampunya ud nyala
	message = "light on"
	mic.say(message)

def isValid(text):
	return bool(re.search(r'\bturn on light\b', text, re.IGNORECASE))