import xbox
import time
import socket

serverAddr = ('192.168.2.29', 6000)
clinetAddr = ('0.0.0.0', 6001)

joy = xbox.Joystick()
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(clinetAddr)

xAng = 0
yAng = 0
diff = 10
prevTime = time.time()

try:
    while True:
        if (time.time() - prevTime) > 0.2:
            # could restrict small change in joystick axis
            # not needed for this xbox because it is not sensitive
            stick = joy.leftStick()
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

            driveData = str(['drive', leftSpeed, rightSpeed]).encode('utf-8')
            print(driveData)
            client.sendto(driveData, serverAddr)

            if joy.rightBumper():
                xAng = 90
                yAng = 90
                print('reset')
            elif joy.Y():
                yAng += diff
                print('up', joy.Y())
            elif joy.A():
                yAng -= diff
                print('down')
            elif joy.X():
                xAng -= diff
                print('left')
            elif joy.B():
                xAng += diff
                print('right')

            if xAng > 60:
                xAng = 60
            elif xAng < -60:
                xAng = -60
            
            if yAng > 60:
                yAng = 60
            elif yAng < -60:
                yAng = -60

            camData = str(['cam', 90+xAng, 90+yAng]).encode('utf-8')
            print(camData)
            client.sendto(camData, serverAddr)

            prevTime = time.time()

except KeyboardInterrupt as e:
    driveData = str(['drive', 0, 0]).encode('utf-8')
    client.sendto(driveData, serverAddr)
    camData = str(['cam', 90, 90]).encode('utf-8')
    client.sendto(camData, serverAddr)
    joy.close()
    client.close()
    print('terminate')