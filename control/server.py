import socket
import select
import ast
import l298nControl

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
            print(type(msg.decode("utf-8")), msg.decode("utf-8"))
            data = ast.literal_eval(msg.decode("utf-8"))
            # data = list()
            header = data[0]
            
            if header == "drive":
                # robot movement control
                x = data[1]
                y = data[2]
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
                
                print("movement", leftSpeed, rightSpeed)
                # drive DC motor here
                l298nControl.left(leftSpeed)
                l298nControl.right(rightSpeed)
                
                
            elif header == "cam":
                # camera control
                print("camera")
                # drive servo motor here

except KeyboardInterrupt as e:
    l298nControl.close()