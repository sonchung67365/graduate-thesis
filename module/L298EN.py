from hamcrest import none
from sqlalchemy import null
import RPiSim.GPIO as GPIO
from time import sleep


HZ = 5000


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)







class Motor():
    in1 = null
    in2 = null
    en = null

    def __init__(self, in1:int, in2:int, en:int):
        self.in1 = in1
        self.in2 = in2
        self.en = en

        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.en, GPIO.OUT)
        self.pwm = GPIO.PWM(self.en, HZ)

        GPIO.OUT(self.in1, GPIO.LOW)
        GPIO.OUT(self.in2, GPIO.LOW)
        self.pwm.start(0)

    def moveF(self, speed=50, t=0):
        GPIO.OUT(self.in1, GPIO.HIGH)
        GPIO.OUT(self.in2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)
        sleep(t)

    def moveB(self, speed=50, t=0):
        GPIO.OUT(self.in1, GPIO.LOW)
        GPIO.OUT(self.in2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)
        sleep(t)
        
    def stop(self, t=0):
        GPIO.OUT(self.in1, GPIO.LOW)
        GPIO.OUT(self.in2, GPIO.LOW)
        sleep(t)
        










class MotorRobot():
    in1 = null
    in2 = null
    en1 = null

    in3 = null
    in4 = null
    en2 = null

    motorLeft = Motor(in1, in2, en1) 
    motorRight = Motor(in3, in4, en2) 


    def __init__(self, in1:int, in2:int, en1:int, in3:int, in4:int, en2:int):
        # Declare motor left and motor right
        self.motorLeft = Motor(in1, in2, en1)
        self.motorRight = Motor(in3, in4, en2)

    
    def move(self, speed=50, turn=0, t=0):
        # If turn > 0 robot turn right
        leftSpeed = speed + turn
        # If turn < 0 robot turn left
        rightSpeed = speed - turn

        # Bounding speed
        if leftSpeed > 100 : leftSpeed = 100
        elif leftSpeed < -100 : leftSpeed = -100
        if rightSpeed > 100 : rightSpeed = 100
        elif rightSpeed < -100 : rightSpeed = -100

        # Setup speed motor right
        if rightSpeed > 0 : self.motorRight.moveF(rightSpeed)
        elif rightSpeed < 0 : self.motorRight.moveB(abs(rightSpeed))
        else : self.motorRight.stop()

        # Setup speed motor left
        if leftSpeed > 0 : self.motorLeft.moveF(leftSpeed)
        elif leftSpeed < 0 : self.motorLeft.moveB(abs(leftSpeed))
        else : self.motorLeft.stop()

        sleep(t)
    

    
    def stop(self, t=0):
        self.motorLeft.stop()
        self.motorRight.stop()
        sleep(t)