import xbox
import time
import socket

joy = xbox.Joystick()
print(joy.connected)

prevTime = time.time()
count = 0
try:
    while True:
        if (time.time() - prevTime) > 0.2:
            print(joy.rightThumbstick())
            prevTime = time.time()
        
except KeyboardInterrupt as e:
    print('terminate')
    joy.close()