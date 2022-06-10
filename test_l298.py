import RPiSim.GPIO as GPIO
import time

class Motor():
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        self.in1_pwm = GPIO.PWM(self.in1, 100)
        self.in2_pwm = GPIO.PWM(self.in2, 100)
        self.in1_pwm.start(0)
        self.in2_pwm.start(0)
    def moveF(self, speed=50, t=0):
        self.in1_pwm.ChangeDutyCycle(0)
        self.in2_pwm.ChangeDutyCycle(speed)
        time.sleep(t)
    def moveB(self, speed=50, t=0):
        self.in1_pwm.ChangeDutyCycle(speed)
        self.in2_pwm.ChangeDutyCycle(0)
        time.sleep(t)
    def stop(self, t=0):
        self.in1_pwm.ChangeDutyCycle(0)
        self.in2_pwm.ChangeDutyCycle(0)
        time.sleep(t)

class MotorRobot():
    def __init__(self, in1, in2, in3, in4):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4

        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)

        self.in1 = GPIO.PWM(self.in1, 100)
        self.in2 = GPIO.PWM(self.in2, 100)
        self.in3 = GPIO.PWM(self.in3, 100)
        self.in4 = GPIO.PWM(self.in4, 100)

        self.in1.start(0)
        self.in2.start(0)
        self.in3.start(0)
        self.in4.start(0)
    
    def move(self, speed=50, turn=0, t=0):
        leftSpeed = speed - turn
        rightSpeed = speed + turn

        if leftSpeed > 100 : leftSpeed = 100
        elif leftSpeed < -100 : leftSpeed = -100
        if rightSpeed > 100 : rightSpeed = 100
        elif rightSpeed < -100 : rightSpeed = -100

        if rightSpeed > 0 :
            self.in1.ChangeDutyCycle(0)
            self.in2.ChangeDutyCycle(rightSpeed)
        else:
            self.in1.ChangeDutyCycle(abs(rightSpeed))
            self.in2.ChangeDutyCycle(0)
        if leftSpeed > 0 :
            self.in3.ChangeDutyCycle(0)
            self.in4.ChangeDutyCycle(leftSpeed)
        else:
            self.in3.ChangeDutyCycle(abs(leftSpeed))
            self.in4.ChangeDutyCycle(0)

        time.sleep(t)
    
    def stop(self, t=0):
        self.in1.ChangeDutyCycle(0)
        self.in2.ChangeDutyCycle(0)
        self.in3.ChangeDutyCycle(0)
        self.in4.ChangeDutyCycle(0)
        time.sleep(t)