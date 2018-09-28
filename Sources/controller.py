### BY LSJ with SAMPLE
### sjun1019@naver.com
### 2018.09.28
### raspberry pi car project For release
### part of car controller

import RPi.GPIO as GPIO
from tkinter import*
from tkinter import ttk
from time import sleep

MOTOR_A_PWM = 12       # PWM(1,24,26,23)
MOTOR_A_DIR = 6   # IN1
MOTOR_B_PWM = 19       # PWM(1,24,26,23)
MOTOR_B_DIR = 16  # IN1

SERVO_A_PWM = 13
SERVO_B_PWM = 18

SPEED = 70
SPEED_GO = 100

tilt = 8
pan = 8

tilt_H = 10
tilt_L = 3.7
pan_H = 12
pan_L = 3

val = 0.3

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
SERVO_A = GPIO.PWM(SERVO_A_PWM, 50)
SERVO_B = GPIO.PWM(SERVO_B_PWM, 50)

SERVO_A.start(15) # 0
SERVO_B.start(15)

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
    SERVO_A.start(tilt)

    if tilt > tilt_L:
        tilt = tilt - val
    
    SERVO_A.ChangeDutyCycle(tilt)
    sleep(delay_servo)

    print('up', tilt)

def d():
    global tilt, pan
    SERVO_A.start(tilt)

    if tilt<tilt_H:
        tilt = tilt + val

    SERVO_A.ChangeDutyCycle(tilt)
    sleep(delay_servo)

    print('down', tilt)

def l():
    global tilt, pan
    SERVO_B.start(pan)

    if pan<pan_H:
        pan = pan + val
    
    SERVO_B.ChangeDutyCycle(pan)
    sleep(delay_servo)

    print('left', pan)

def r():
    global tilt, pan
    SERVO_B.start(pan)

    if pan>pan_L:
        pan = pan - val

    SERVO_B.ChangeDutyCycle(pan)
    sleep(delay_servo)

    print('right', pan)


def home():
    global tilt, pan
    tilt = 8
    pan = 8
    SERVO_A.start(tilt)
    SERVO_B.start(pan)
    SERVO_A.ChangeDutyCycle(tilt)
    SERVO_B.ChangeDutyCycle(pan)
    sleep(delay_servo)


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
            GPIO.setup(SERVO_A_PWM, GPIO.OUT)
            GPIO.setup(SERVO_B_PWM, GPIO.OUT)
            u() 
        else:
            SERVO_A.stop()
            SERVO_B.stop()

    elif(len(ttk.Widget.state(DOWN))>3):
        if(ttk.Widget.state(DOWN)[2]=='pressed'):
            GPIO.setup(SERVO_A_PWM, GPIO.OUT)
            GPIO.setup(SERVO_B_PWM, GPIO.OUT)
            d()
        else:
            SERVO_A.stop()
            SERVO_B.stop()

    elif(len(ttk.Widget.state(LEFT))>3):
        if(ttk.Widget.state(LEFT)[2]=='pressed'):
            GPIO.setup(SERVO_A_PWM, GPIO.OUT)
            GPIO.setup(SERVO_B_PWM, GPIO.OUT)
            l()
        else:
            SERVO_A.stop()
            SERVO_B.stop()

    elif(len(ttk.Widget.state(RIGHT))>3):
        if(ttk.Widget.state(RIGHT)[2]=='pressed'):
            GPIO.setup(SERVO_A_PWM, GPIO.OUT)
            GPIO.setup(SERVO_B_PWM, GPIO.OUT)
            r()
        else:
            SERVO_A.stop()
            SERVO_B.stop()

    elif(len(ttk.Widget.state(HOME))>3):
        if(ttk.Widget.state(HOME)[2]=='pressed'):
            GPIO.setup(SERVO_A_PWM, GPIO.OUT)
            GPIO.setup(SERVO_B_PWM, GPIO.OUT)
            home()
        else:
            SERVO_A.stop()
            SERVO_B.stop()

root.title('샘플전자 - 라즈베리 RC 카')
root.geometry('800x230+120+300')

F = ttk.Button(root)

Forward = PhotoImage(file = '~/RaspberryPi-RC-Car_SAMPLE/Buttons/Forward.gif')
F.img = Forward.subsample(2,2)
F.config(image = F.img, compound = CENTER)
F.grid(row=1, column=0)
#F.pack()

B = ttk.Button(root)

Backward = PhotoImage(file = '~/RaspberryPi-RC-Car_SAMPLE/Buttons/Backward.gif')
B.img = Backward.subsample(2,2)
B.config(image = B.img, compound = CENTER)
B.grid(row=1, column=1)
#B.pack()

L = ttk.Button(root)

Left = PhotoImage(file = '~/RaspberryPi-RC-Car_SAMPLE/Buttons/Left.gif')
L.img = Left.subsample(2,2)
L.config(image = L.img, compound = CENTER)
L.grid(row=1, column=2)
#L.pack()

R = ttk.Button(root)

Right = PhotoImage(file = '~/RaspberryPi-RC-Car_SAMPLE/Buttons/Right.gif')
R.img = Right.subsample(2,2)
R.config(image = R.img, compound = CENTER)
R.grid(row=1, column=3)
#R.pack()


UP = ttk.Button(root)

Up = PhotoImage(file = '~/RaspberryPi-RC-Car_SAMPLE/Buttons/Forward.gif')
UP.img = Up.subsample(10,10)
UP.config(image = UP.img, compound = CENTER)
UP.grid(row=0, column=0)
#UP.pack()

DOWN = ttk.Button(root)
Down = PhotoImage(file = '~/RaspberryPi-RC-Car_SAMPLE/Buttons/Backward.gif')
DOWN.img = Down.subsample(10,10)
DOWN.config(image = DOWN.img, compound = CENTER)
DOWN.grid(row=0, column=1)
#DOWN.pack()

LEFT = ttk.Button(root)

Left = PhotoImage(file = '~/RaspberryPi-RC-Car_SAMPLE/Buttons/Left.gif')
LEFT.img = Left.subsample(10,10)
LEFT.config(image = LEFT.img, compound = CENTER)
LEFT.grid(row=0, column=2)
#LEFT.pack()

RIGHT = ttk.Button(root)

Right = PhotoImage(file = '~/RaspberryPi-RC-Car_SAMPLE/Buttons/Right.gif')
RIGHT.img = Right.subsample(10,10)
RIGHT.config(image = RIGHT.img, compound = CENTER)
RIGHT.grid(row=0, column=3)
#RIGHT.pack()

HOME = ttk.Button(root)
Home = PhotoImage(file = '~/RaspberryPi-RC-Car_SAMPLE/Buttons/Home.gif')
HOME.img = Home.subsample(16,16)
HOME.config(image = HOME.img, compound = CENTER)
HOME.grid(row=0, column=4)

#root.mainloop()

while True:
    root.update_idletasks()
    root.update()
    switch()
    GPIO.setup(SERVO_A_PWM, GPIO.IN)
    GPIO.setup(SERVO_B_PWM, GPIO.IN)

GPIO.clean()