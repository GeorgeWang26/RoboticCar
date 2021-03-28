import socket
import select
import time

server_address = ("0.0.0.0", 5005)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)
count = 0
# time.sleep(5)
print("start")

while True:
    readable, writable, exceptional = select.select([server], [], [], 0)

    if readable:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")
        print("recieved data", data, "from", addr)
        