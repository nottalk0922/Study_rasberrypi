import RPi.GPIO as GPIO
import time

FL_SW = 5
FL_LED = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(FL_SW,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(FL_LED,GPIO.OUT)

try:
    while True:
        FL_Value = GPIO.input(FL_SW)
        if FL_Value == 1:
            GPIO.output(FL_LED,GPIO.HIGH)
        elif FL_Value == 0:
            GPIO.output(FL_LED,GPIO.LOW)
    
except KeyboardInterrupt:
        pass
    
GPIO.cleanup()