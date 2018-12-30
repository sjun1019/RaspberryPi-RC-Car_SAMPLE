### BY LSJ with SAMPLE
### 2018.10.28 //ui edit, seperate for lcd
### 2018.11.11 //integrate
### 2018.11.15 //SoftPWM for Servo
### raspberry pi car project
### part of car controller

import RPi.GPIO as GPIO
from tkinter import*
from tkinter import ttk
from time import sleep
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 550)
cap.set(cv2.CAP_PROP_FPS, 60)

MOTOR_A_PWM = 12       # PWM(1,24,26,23)
MOTOR_A_DIR = 6   # IN1
MOTOR_B_PWM = 19       # PWM(1,24,26,23)
MOTOR_B_DIR = 16  # IN1

SERVO_A_PWM = 13
SERVO_B_PWM = 18

SPEED = 70
SPEED_GO = 100

tilt = 90.0
pan = 90.0

tilt_H = 180.0
tilt_L = 0.0
pan_H = 180.0
pan_L = 0.0

val = 10.0

delay = 0.5
delay_servo = 0.2

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(MOTOR_A_PWM, GPIO.OUT)
GPIO.setup(MOTOR_A_DIR, GPIO.OUT)
GPIO.setup(MOTOR_B_PWM, GPIO.OUT)
GPIO.setup(MOTOR_B_DIR, GPIO.OUT)

GPIO.setup(SERVO_A_PWM, GPIO.OUT)
GPIO.setup(SERVO_B_PWM, GPIO.OUT)

MOTOR_A = GPIO.PWM(MOTOR_A_PWM, 100)
MOTOR_B = GPIO.PWM(MOTOR_B_PWM, 100)
#SERVO_A = GPIO.PWM(SERVO_A_PWM, 50)
#SERVO_B = GPIO.PWM(SERVO_B_PWM, 50)

#SERVO_A.start(15) # 0
#SERVO_B.start(15)

def servo(degree, pin):
    usec = round(map(degree, 0.0, 180.0, 0.001, 0.002), 6)
    for i in range(0,20):
        GPIO.output(pin, GPIO.HIGH)
        sleep(usec)
        GPIO.output(pin, GPIO.LOW)
        sleep(0.02-usec)

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def home():
    global tilt, pan
    tilt = 90
    pan = 90
    servo(tilt, SERVO_A_PWM)
    servo(pan, SERVO_B_PWM)
    #sleep(delay_servo)

home()

root = Tk()

def forward():
    MOTOR_A.start(0)
    MOTOR_B.start(0)
    GPIO.output(MOTOR_A_DIR, GPIO.HIGH)
    MOTOR_A.ChangeDutyCycle(SPEED_GO)
    GPIO.output(MOTOR_B_DIR, GPIO.LOW)
    MOTOR_B.ChangeDutyCycle(SPEED_GO)
    #sleep(delay)
    print('forward')

def backward():
    MOTOR_A.start(0)
    MOTOR_B.start(0)
    GPIO.output(MOTOR_A_DIR, GPIO.LOW)
    MOTOR_A.ChangeDutyCycle(SPEED_GO)
    GPIO.output(MOTOR_B_DIR, GPIO.HIGH)
    MOTOR_B.ChangeDutyCycle(SPEED_GO)
    #sleep(delay)
    print('backward')

def left():
    MOTOR_A.start(0)
    MOTOR_B.start(0)
    GPIO.output(MOTOR_A_DIR, GPIO.LOW)
    MOTOR_A.ChangeDutyCycle(SPEED)
    GPIO.output(MOTOR_B_DIR, GPIO.LOW)
    MOTOR_B.ChangeDutyCycle(SPEED)
    #sleep(delay)
    print('left')

def right():
    MOTOR_A.start(0)
    MOTOR_B.start(0)
    GPIO.output(MOTOR_A_DIR, GPIO.HIGH)
    MOTOR_A.ChangeDutyCycle(SPEED)
    GPIO.output(MOTOR_B_DIR, GPIO.HIGH)
    MOTOR_B.ChangeDutyCycle(SPEED)
    #sleep(delay)
    print('right')


def u():
    global tilt, pan
    #servo(tilt, SERVO_A_PWM)

    if tilt > tilt_L:
        tilt = tilt - val
    
    servo(tilt, SERVO_A_PWM)
    #sleep(delay_servo)

    print('up', tilt)

def d():
    global tilt, pan
    #servo(tilt, SERVO_A_PWM)

    if tilt<tilt_H:
        tilt = tilt + val

    servo(tilt, SERVO_A_PWM)
    #sleep(delay_servo)

    print('down', tilt)

def l():
    global tilt, pan
    #servo(pan, SERVO_B_PWM)

    if pan<pan_H:
        pan = pan + val
    
    servo(pan, SERVO_B_PWM)
    #sleep(delay_servo)

    print('left', pan)

def r():
    global tilt, pan
    #servo(pan, SERVO_B_PWM)

    if pan>pan_L:
        pan = pan - val

    servo(pan, SERVO_B_PWM)
    #sleep(delay_servo)

    print('right', pan)


def exit():
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
    root.destroy()


def switch():
    if(len(ttk.Widget.state(F))>3):
        if(ttk.Widget.state(F)[2]=='pressed'):
            forward()

    elif(len(ttk.Widget.state(B))>3):
        if(ttk.Widget.state(B)[2]=='pressed'):
            backward()

    elif(len(ttk.Widget.state(L))>3):
        if(ttk.Widget.state(L)[2]=='pressed'):
            left()

    elif(len(ttk.Widget.state(R))>3):
        if(ttk.Widget.state(R)[2]=='pressed'):
            right()
    else:
        MOTOR_A.stop()
        MOTOR_B.stop()


    if(len(ttk.Widget.state(UP))>3): 
        if(ttk.Widget.state(UP)[2]=='pressed'):
            #GPIO.setup(SERVO_A_PWM, GPIO.OUT)
            #GPIO.setup(SERVO_B_PWM, GPIO.OUT)
            u() 
        #else:
            #SERVO_A.stop()
            #SERVO_B.stop()

    elif(len(ttk.Widget.state(DOWN))>3):
        if(ttk.Widget.state(DOWN)[2]=='pressed'):
            #GPIO.setup(SERVO_A_PWM, GPIO.OUT)
            #GPIO.setup(SERVO_B_PWM, GPIO.OUT)
            d()
        #else:
            #SERVO_A.stop()
            #SERVO_B.stop()

    elif(len(ttk.Widget.state(LEFT))>3):
        if(ttk.Widget.state(LEFT)[2]=='pressed'):
            #GPIO.setup(SERVO_A_PWM, GPIO.OUT)
            #GPIO.setup(SERVO_B_PWM, GPIO.OUT)
            l()
        #else:
            #SERVO_A.stop()
            #SERVO_B.stop()

    elif(len(ttk.Widget.state(RIGHT))>3):
        if(ttk.Widget.state(RIGHT)[2]=='pressed'):
            #GPIO.setup(SERVO_A_PWM, GPIO.OUT)
            #GPIO.setup(SERVO_B_PWM, GPIO.OUT)
            r()
        #else:
            #SERVO_A.stop()
            #SERVO_B.stop()

    elif(len(ttk.Widget.state(HOME))>3):
        if(ttk.Widget.state(HOME)[2]=='pressed'):
            #GPIO.setup(SERVO_A_PWM, GPIO.OUT)
            #GPIO.setup(SERVO_B_PWM, GPIO.OUT)
            home()
        #else:
            #SERVO_A.stop()
            #SERVO_B.stop()
    
    elif(len(ttk.Widget.state(EXIT))>3):
        if(ttk.Widget.state(EXIT)[2]=='pressed'):
            exit()

root.title('샘플전자 - 라즈베리 RC 카')
root.geometry('475x145+420+620')

F = ttk.Button(root)

Forward = PhotoImage(file = '/home/pi/RaspberryPi-RC-Car_SAMPLE/Images/Forward.gif')
F.img = Forward.subsample(4,4)
F.config(image = F.img, compound = CENTER)
F.grid(row=1, column=0)
#F.pack()

B = ttk.Button(root)

Backward = PhotoImage(file = '/home/pi/RaspberryPi-RC-Car_SAMPLE/Images/Backward.gif')
B.img = Backward.subsample(4,4)
B.config(image = B.img, compound = CENTER)
B.grid(row=1, column=1)
#B.pack()

L = ttk.Button(root)

Left = PhotoImage(file = '/home/pi/RaspberryPi-RC-Car_SAMPLE/Images/Left.gif')
L.img = Left.subsample(4,4)
L.config(image = L.img, compound = CENTER)
L.grid(row=1, column=3)
#L.pack()

R = ttk.Button(root)

Right = PhotoImage(file = '/home/pi/RaspberryPi-RC-Car_SAMPLE/Images/Right.gif')
R.img = Right.subsample(4,4)
R.config(image = R.img, compound = CENTER)
R.grid(row=1, column=4)
#R.pack()


UP = ttk.Button(root)

Up = PhotoImage(file = '/home/pi/RaspberryPi-RC-Car_SAMPLE/Images/Forward.gif')
UP.img = Up.subsample(14,14)
UP.config(image = UP.img, compound = CENTER)
UP.grid(row=0, column=0)
#UP.pack()

DOWN = ttk.Button(root)
Down = PhotoImage(file = '/home/pi/RaspberryPi-RC-Car_SAMPLE/Images/Backward.gif')
DOWN.img = Down.subsample(14,14)
DOWN.config(image = DOWN.img, compound = CENTER)
DOWN.grid(row=0, column=1)
#DOWN.pack()

LEFT = ttk.Button(root)

Left = PhotoImage(file = '/home/pi/RaspberryPi-RC-Car_SAMPLE/Images/Left.gif')
LEFT.img = Left.subsample(14,14)
LEFT.config(image = LEFT.img, compound = CENTER)
LEFT.grid(row=0, column=3)
#LEFT.pack()

RIGHT = ttk.Button(root)

Right = PhotoImage(file = '/home/pi/RaspberryPi-RC-Car_SAMPLE/Images/Right.gif')
RIGHT.img = Right.subsample(14,14)
RIGHT.config(image = RIGHT.img, compound = CENTER)
RIGHT.grid(row=0, column=4)
#RIGHT.pack()

HOME = ttk.Button(root)
Home = PhotoImage(file = '/home/pi/RaspberryPi-RC-Car_SAMPLE/Images/Home.gif')
HOME.img = Home.subsample(35,35)
HOME.config(image = HOME.img, compound = CENTER)
HOME.grid(row=0, column=2)

EXIT = ttk.Button(root)
Exit = PhotoImage(file = '/home/pi/RaspberryPi-RC-Car_SAMPLE/Images/Exit.gif')
EXIT.img = Exit.subsample(35,35)
EXIT.config(image = EXIT.img, compound = CENTER)
EXIT.grid(row=1, column=2)
#root.mainloop()

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    root.update_idletasks()
    root.update()
    switch()
    #GPIO.setup(SERVO_A_PWM, GPIO.IN)
    #GPIO.setup(SERVO_B_PWM, GPIO.IN)