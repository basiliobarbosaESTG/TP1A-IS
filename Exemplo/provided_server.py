import socket
from funcoes import abc, double_int, say_hello, rpc_test, doggo_test, favorite_number, half_float, bye_basilio
import json

# UDP IP address and port
UDP_IP = "127.0.0.1"
UDP_PORT = 5005


# Class for the registry
class RPCRegistry(set):

    # Create a blank set on init
    def __init__(self):
        self.registryMapping = {}

    # Register the function to the set
    def register(self, func):
        self.registryMapping[func.__name__] = func


# Class for the Server
class RPCServer:

    # Set up the registry
    def __init__(self):
        self.registry = RPCRegistry()

    # Call the function
    def __call__(self, *args, **kwargs):
        loaded_data = json.loads(args[0])
        function_name = self.registry.registryMapping[loaded_data["name"]]
        func_args = tuple(loaded_data["args"])
        return function_name(*func_args)

    # Register the function wrapper
    def register(self, wrapper):
        self.registry.register(wrapper)
        return wrapper


def serve(passed_server):
    # Set up UDP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    # Run 5-ever
    while True:
        # Receive Data
        data, address = sock.recvfrom(1024)

        # Decode and Dump JSON
        decoded_data = data.decode()
        return_data = passed_server.__call__(decoded_data)

        # Encode and Send Back Data
        json_return_data = json.dumps(return_data)
        sock.sendto(json_return_data.encode(), address)


if __name__ == '__main__':
    # Set up server
    server = RPCServer()

    # Register wrapped functions
    wrapped_abc = server.register(abc)
    wrapped_double = server.register(double_int)
    wrapped_sayhello = server.register(say_hello)
    wrapped_rpc_test = server.register(rpc_test)
    wrapped_doggo_test = server.register(doggo_test)
    wrapped_favorite_number = server.register(favorite_number)
    wrapped_half_float = server.register(half_float)
    wrapped_bye_basilio = server.register(bye_basilio)

    # Run server
    serve(server)
