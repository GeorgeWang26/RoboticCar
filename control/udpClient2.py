import socket

server_address = ("192.168.2.38", 5005)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("0.0.0.0", 6001))
msg = "2"
data = bytes(msg, 'utf-8')
client.sendto(data, server_address)