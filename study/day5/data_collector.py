import threading
import serial
import time
import RPi.GPIO as GPIO
import cv2 

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

gData = ""

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(PWMA,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)

GPIO.setup(PWMB,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)

L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMB,500)
R_Motor.start(0)

def motor_go(speed):
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    R_Motor.ChangeDutyCycle(speed)

def motor_back(speed):
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)
    R_Motor.ChangeDutyCycle(speed)
    
def motor_left(speed):
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    R_Motor.ChangeDutyCycle(speed)
    
def motor_right(speed):
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)
    R_Motor.ChangeDutyCycle(speed)

def motor_stop():
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    R_Motor.ChangeDutyCycle(0)

def serial_thread():
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data


speedSet = 50


def camera_func(carState,image,i):
    
#     print('ca')
#    camera = cv2.VideoCapture(-1)
#    camera.set(3, 640)
#    camera.set(4, 480)
    filepath = "/home/leechan/study/video/"  
     
    height, _, _ = image.shape
    save_image = image[int(height/2):,:,:]
    save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2YUV)
    save_image = cv2.GaussianBlur(save_image, (3,3), 0)
    save_image = cv2.resize(save_image, (200,66))
    cv2.imshow('Save', save_image)
        
    if carState == "left":
         cv2.imwrite("%s_%05d_%03d.png" % (filepath, i, 45), save_image)

    elif carState == "right":
        cv2.imwrite("%s_%05d_%03d.png" % (filepath, i, 135), save_image)

    elif carState == "go":
        cv2.imwrite("%s_%05d_%03d.png" % (filepath, i, 90), save_image)

    


def main():
#     print('main')
    global gData
    carState = ""
    camera = cv2.VideoCapture(-1)
    camera.set(3, 640)
    camera.set(4, 480)
  

    i = 0
    try:
        while (camera.isOpened() ):
            keyvelue = cv2.waitKey(10)
        
            _, image = camera.read()
            image = cv2.flip(image,-1)
            cv2.imshow('Original', image)
    
            if(keyvelue == ord('q')): break
            
            
            if gData.find("1") >= 0:
                gData = ""
                print("ok go")
                carState = "go"
                motor_go(50)
            elif gData.find("2") >= 0:
                gData = ""
                print("ok left")
                carState = "left"
                motor_left(50)
            elif gData.find("3") >= 0:
                gData = ""
                print("ok right")
                carState = "right"
                motor_right(50)
            elif gData.find("4") >= 0:
                gData = ""
                print("ok stop")
                carState = "stop"
                motor_stop()
        
            camera_func(carState,image,i)
            i+= 1
    except:
        pass  

    cv2.destroyAllWindows()


if __name__ == '__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bleSerial.close()
    GPIO.cleanup()