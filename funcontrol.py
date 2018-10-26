#!/usr/bin/python

import RPi.GPIO as GPIO
import os, sys, traceback, signal

from time import sleep
from re import findall
from subprocess import check_output

def gpio_cleanup(signum, frame):
	raise  KeyboardInterrupt

def get_temp():
	temp = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()
    temp = float(findall('\d+\.\d+', temp)[0])
    return(temp)
try:
    tempOn = 72             # Temp Cooler On
	tempOff = 45			# Temp Cooler Off
    controlPin = 14         # Control Pin Number
	latencyTime = 10		# Time in sec between temperature measuring 
    pinState = False
    # === Init Pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(controlPin, GPIO.OUT, initial=0)
	signal.signal(signal.SIGTERM, gpio_cleanup)
	signal.signal(signal.SIGINT, gpio_cleanup)
    while True:
		temp = get_temp()
        if temp > tempOn and not pinState or temp < tempOff and pinState:
			pinState = not pinState
            GPIO.output(controlPin, pinState)
			print(str(temp) + "  " + str(pinState))
        sleep(latencyTime)
except KeyboardInterrupt:
	# ...
    print("Exit pressed Ctrl+C")
except:
	# ...
	print("Other Exception")
    print("--- Start Exception Data:")
    traceback.print_exc(limit=2, file=sys.stdout)
    print("--- End Exception Data:")
finally:
	print("CleanUp")
    GPIO.cleanup()
	print("End of Program");
