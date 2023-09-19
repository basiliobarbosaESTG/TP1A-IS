import socket
HOST = '127.0.0.1'
PORT = 8190

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello Basilio Barbosa')
    data = s.recv(1024)
    
print('Received', repr(data))