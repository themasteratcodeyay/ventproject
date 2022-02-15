import requests
import json
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
servoPin=11
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)

def AngletoDC(cdc):
    return 1./18. * (cdc) + 2

def DCtoAngle(angle):
    return (angle-2) / (1./18.)

def get_degrees():
  r = requests.get("https://williamventproject-default-rtdb.firebaseio.com/ventproject.json").json()
  return r['degrees']
# math
# DC = 1./18. * (position) + 2
t=get_degrees() 

# initialize t = current value of degrees

pwm.ChangeDutyCycle(AngletoDC(t))

try:
    while True:
        # create a variable to keep track of the previous degree value (previous relative to each while loop iteration)
        # use that variable in an if statement to control the flow of the program so that
        #     it only runs the code that changes the servo when there is a change in the database
        #     if there is no change, print out current degrees and continue in the loop
        v = get_degrees()
        if t!=v:
            t=v
            pwm.ChangeDutyCycle(AngletoDC(v))            
        
        sleep(1)
except KeyboardInterrupt:
    print("Program stopped")
    pwm.stop()
    GPIO.cleanup()
    quit()

pwm.stop()
GPIO.cleanup()