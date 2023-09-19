import socket
import sys
# Create a TCP/IP socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print ('A conectar a %s porta %s' % server_address, file = sys.stderr)
sock.connect(server_address)
try:
    # Send data
    mensagem = 'Esta é a mensagem. Será repetido.'
    print ('Enviando "%s"' % mensagem, file = sys.stderr)
    sock.sendall(mensagem.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(mensagem)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print ('Recebido "%s"' % data, file = sys.stderr)
finally:
    print('A fechar o socket', file = sys.stderr)
    sock.close()