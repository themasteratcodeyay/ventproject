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
# math
# DC = 1./18. * (position) + 2
try:
    while True:
#        for i in range(2, 13):
#            print(i)
#            print("angle: " + str((i-2) / (1./18.)))
#            pwm.ChangeDutyCycle(i)
#            sleep(1)
        pwm.ChangeDutyCycle(AngletoDC(int(input("Enter desired position angle 0-180: "))))
except KeyboardInterrupt:
    print("Program stopped")
    pwm.stop()
    GPIO.cleanup()
    quit()

pwm.stop()
GPIO.cleanup()
