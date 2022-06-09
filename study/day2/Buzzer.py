import RPi.GPIO as GPIO
import time

Buzzer = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer,GPIO.OUT)

p = GPIO.PWM(Buzzer,261)
p.start(50)

try:
    while True:
        p.start(50)
        p.ChangeFrequency(261) #do
        time.sleep(1.0)
        p.ChangeFrequency(293) #le
        time.sleep(1.0)
        p.ChangeFrequency(329) #mi
        time.sleep(1.0)
        p.ChangeFrequency(349) #fa
        time.sleep(1.0)
        p.ChangeFrequency(391) #sol
        time.sleep(1.0)
        p.ChangeFrequency(440) #la
        time.sleep(1.0)
        p.ChangeFrequency(493) #si
        time.sleep(1.0)
        p.ChangeFrequency(523) #doo
        p.stop()
        time.sleep(1.0)
    
except KeyboardInterrupt:
        pass

p.stop()
GPIO.cleanup()