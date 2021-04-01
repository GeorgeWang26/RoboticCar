import socket
import select
import ast
import l298nControl
import hatControl

serverAddr = ("0.0.0.0", 6000)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(serverAddr)

l298nControl.left(0)
l298nControl.right(0)

try:
    while True:
        redable, writable, execptional = select.select([server], [], [])
        
        if redable:
            msg, adr = server.recvfrom(1024)
            data = ast.literal_eval(msg.decode("utf-8"))
            print(data)
            header = data[0]
            
            if header == "drive":
                leftSpeed = data[1]
                rightSpeed = data[2]
                print("movement", leftSpeed, rightSpeed)
                l298nControl.left(leftSpeed)
                l298nControl.right(rightSpeed)
            elif header == "cam":
                xAngle = data[1]
                yAngle = data[2]
                print("camera", xAngle, yAngle)
                hatControl.xChange(xAngle)
                hatControl.yChange(yAngle)

except KeyboardInterrupt as e:
    l298nControl.close()
    hatControl.close()
    server.close()