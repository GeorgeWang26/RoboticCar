import RPi.GPIO as GPIO
import time

# 0 <= pwm duty cycle <= 100

# for both left and right side
# positive speed is forward, negative speed is backward


in1 = 23
in2 = 24
ena = 25
in3 = 17
in4 = 22
enb = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)
pwma = GPIO.PWM(ena, 1000)
pwma.start(0)

GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
pwmb = GPIO.PWM(enb, 1000)
pwmb.start(0)

def drive(in_1, in_2, pwm, speed):
    print(in_1, in_2, pwm, speed)
    if speed == 0:
        GPIO.output(in_1, GPIO.LOW)
        GPIO.output(in_2, GPIO.LOW)
    elif speed > 0:
        GPIO.output(in_1, GPIO.HIGH)
        GPIO.output(in_2, GPIO.LOW)
    else:
        GPIO.output(in_1, GPIO.LOW)
        GPIO.output(in_2, GPIO.HIGH)
    pwm.ChangeDutyCycle(abs(speed))
    

def left(speed):
    drive(in1, in2, pwma, speed)
    
def right(speed):
    drive(in3, in4, pwmb, speed)

def close():
    left(0)
    right(0)
    GPIO.cleanup()

#left forward
#left(75)
#time.sleep(5)

#left backward
#left(-75)
#time.sleep(5)

#right forward
#right(75)
#time.sleep(5)

#right backward
#right(-75)
#time.sleep(5)

#close()