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
            stick = joy.rightStick()

            # if abs(stick[0]) < 0.6 and stick[0] != 0:
            #     print("small x", stick[0])
            # if abs(stick[1]) < 0.6 and stick[1] != 0:
            #     print("small y", stick[1])

            x = stick[0]*0.3
            y = stick[1]*0.8
            # could process the speed here instead of on rpi
            data = str(["drive", x, y]).encode("utf-8")
            print(data)
            client.sendto(data, serverAddr)
            prevTime = time.time()

except KeyboardInterrupt as e:
    data = str(["drive", 0, 0]).encode("utf-8")
    client.sendto(data, serverAddr)
    joy.close()
    print("terminate")