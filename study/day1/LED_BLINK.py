import RPi.GPIO as GPIO
import time

FL_LED = 26
FR_LED = 16
BL_LED = 20
BR_LED = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(FL_LED,GPIO.OUT)
GPIO.setup(FR_LED,GPIO.OUT)
GPIO.setup(BL_LED,GPIO.OUT)
GPIO.setup(BR_LED,GPIO.OUT)

try:
    while True:
        GPIO.output(FL_LED,GPIO.HIGH)
        GPIO.output(FR_LED,GPIO.HIGH)
        GPIO.output(BL_LED,GPIO.HIGH)
        GPIO.output(BR_LED,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(FL_LED,GPIO.LOW)
        GPIO.output(FR_LED,GPIO.LOW)
        GPIO.output(BL_LED,GPIO.LOW)
        GPIO.output(BR_LED,GPIO.LOW)
        time.sleep(1.0)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
