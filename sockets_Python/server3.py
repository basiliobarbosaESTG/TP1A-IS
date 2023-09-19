from multiprocessing import connection
import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('A iniciar na %s porta %s' % server_address, file = sys.stderr)
sock.bind(server_address)

sock.listen(1)
while True:
    print('A esperar pela conexão', file = sys.stderr)
    connection, client_address = sock.accept()
    try:
        print("Conexão de", client_address, file = sys.stderr)
        while True:
            data = connection.recv(26)
            print('Recebido "%s"' % data, file = sys.stderr)
            if data:
                print('A enviar dados para o cliente', file = sys.stderr)
                connection.sendall(data)
            else:
                print('Não foram recebidos dados de', client_address, file = sys.stderr)
                break
    finally:
        connection.close()