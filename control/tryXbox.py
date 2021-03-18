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
            stick = joy.rightStick()
            x = stick[0] * 0.3
            y = stick[1] * 0.8
            # here will be sending msg
            # print(x, y)
            print(count)
            count+=1
            # get newest time again for pressision
            prevTime = time.time()
        
except KeyboardInterrupt as e:
    print('terminate')
    joy.close()