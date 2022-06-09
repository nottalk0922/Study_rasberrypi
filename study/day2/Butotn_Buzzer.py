import RPi.GPIO as GPIO
import time

FL_LED = 26
FR_LED = 16
BL_LED = 20
BR_LED = 21
FL_SW = 5
FR_SW = 6
BL_SW = 13
BR_SW = 19
Buzzer = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(FL_LED,GPIO.OUT)
GPIO.setup(FR_LED,GPIO.OUT)
GPIO.setup(BL_LED,GPIO.OUT)
GPIO.setup(BR_LED,GPIO.OUT)
GPIO.setup(FL_SW,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(FR_SW,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BL_SW,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BR_SW,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(Buzzer,GPIO.OUT)

p = GPIO.PWM(Buzzer,261)

value = [0,0,0,0] 

try:
    while True:
        value[0] = GPIO.input(FL_SW)
        if value[0] == 1:
            GPIO.output(FL_LED,GPIO.HIGH)
        elif value[0] == 0:
            GPIO.output(FL_LED,GPIO.LOW)
        
        value[1] = GPIO.input(FR_SW)
        if value[1] == 1:
            GPIO.output(FR_LED,GPIO.HIGH)
        elif value[1] == 0:
            GPIO.output(FR_LED,GPIO.LOW)
        
        value[2] = GPIO.input(BL_SW)
        if value[2] == 1:
            GPIO.output(BL_LED,GPIO.HIGH)
        elif value[2] == 0:
            GPIO.output(BL_LED,GPIO.LOW)
        
        value[3] = GPIO.input(BR_SW)
        if value[3] == 1:
            GPIO.output(BR_LED,GPIO.HIGH)
        elif value[3] == 0:
            GPIO.output(BR_LED,GPIO.LOW)
        
        if (value[0] == 1) and (value[1] == 1) and (value[2] == 1) and (value[3] == 1):
            p.start(50)
            time.sleep(1.0)
            p.stop()
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
