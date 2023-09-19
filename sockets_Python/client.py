import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
client.send("Sou o Cliente<br>".encode())
from_server = client.recv(4096)
client.close()
print(from_server)