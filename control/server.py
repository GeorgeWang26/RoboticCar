import socket
import select
import ast

serverAddr = ("0.0.0.0", 6000)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(serverAddr)

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
            print("movement", data[1], data[2])
            # drive DC motor here

        if header == "cam":
            # camera control
            print("camera")
            # drive servo motor here
