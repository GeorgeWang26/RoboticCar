import xbox
import time
import socket

serverAddr = ("192.168.2.29", 6000)
clinetAddr = ("0.0.0.0", 6001)
joy = xbox.Joystick()

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(clinetAddr)
prevTime = time.time()

try:
    while True:
        if (time.time() - prevTime) > 0.2:
            # could restrict small change in joystick axis
            # not needed for this xbox because it is not sensitive
            stick = joy.rightStick()
            x = stick[0]*0.5
            y = stick[1]*0.8
            leftSpeed = 100*(y+x)
            rightSpeed = 100*(y-x)
            
            if leftSpeed > 100:
                leftSpeed = 100
            elif leftSpeed < -100:
                leftSpeed = -100
            
            if rightSpeed > 100:
                rightSpeed = 100
            elif rightSpeed < -100:
                rightSpeed = -100

            data = str(["drive", leftSpeed, rightSpeed]).encode("utf-8")
            print(data)
            client.sendto(data, serverAddr)
            prevTime = time.time()

except KeyboardInterrupt as e:
    data = str(["drive", 0, 0]).encode("utf-8")
    client.sendto(data, serverAddr)
    joy.close()
    print("terminate")