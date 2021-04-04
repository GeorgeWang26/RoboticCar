from adafruit_servokit import ServoKit
# pip3 install adafruit-circuitpython-servokit
import time
# init 16 channels hat
kit = ServoKit(channels=16)

# x at channel 1
# y at  channel 0
x = kit.servo[1]
y = kit.servo[0]

# left side of x >90
# right side of x <90
# up side of y <90
# down side of y >90

# 500 microseconds  = 0 deg
# 1500 microseconds = 90 deg
# 2500 microseconds = 180 deg
x.set_pulse_width_range(500,2500)
y.set_pulse_width_range(500,2500)


def xChange(angle):
    x.angle = angle

def yChange(angle):
    y.angle = angle

def close():
    x.angle = 90
    y.angle = 90

# init at 90 deg(flat)
x.angle = 90
y.angle = 90

if __name__ == '__main__':
    time.sleep(3)
    y.angle = 60
    time.sleep(3)
    y.angle = 90
    time.sleep(3)
    y.angle = 110
    time.sleep(3)
    x.angle = 90
    y.angle = 90
