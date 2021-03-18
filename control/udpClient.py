import socket

server_address = ("192.168.2.38", 5005)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("0.0.0.0", 6000))
msg = "1"
# data = msg.encode("utf-8")
data = bytes(msg)
client.sendto(data, server_address)