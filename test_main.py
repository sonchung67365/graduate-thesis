# Imports ---------------------------
import RPi.GPIO as GPIO
#import RPiSim as GPIO
import time
import test_l298 as L298

# Constants ----------------
IN_1 = 17
IN_2 = 27
IN_3 = 22
IN_4 = 23
BUTTON_PIN = 24
LED_PIN = 25

# Setups -----------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

#motor1 = L298.Motor(IN_1, IN_2)
#motor2 = L298.Motor(IN_3, IN_4)
motor = L298.MotorRobot(IN_1, IN_2, IN_3, IN_4)

GPIO.output(LED_PIN, GPIO.LOW)

try:
    while(1):
        time.sleep(1/50)
        if GPIO.input(BUTTON_PIN) == False:
            print("Led On")
            GPIO.output(LED_PIN, GPIO.HIGH)
            #motor1.moveF(100, 5)
            motor.move(0, 40, 5)
        else:
            print("Led Off")
            GPIO.output(LED_PIN, GPIO.LOW)
            #motor1.stop()
            motor.stop()
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    print("Exit")