import json
import socket

# UDP IP address and port
UDP_IP = "127.0.0.1"
UDP_PORT = 5005


class RPCClient:
    def __init__(self, func):
        # wrap the function
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tempFunc = func

    def __call__(self, *args, **kwargs):
        # Format JSON message
        json_message = {"name": self.tempFunc.__name__, "args": args}
        json_message = json.dumps(json_message)

        # Send JSON message
        self.sock.sendto(json_message.encode(), (UDP_IP, UDP_PORT))

        # Wait to receive Data
        returned_data, addr = self.sock.recvfrom(1024)

        # Decode Data
        decoded_return = returned_data.decode()
        return decoded_return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Import functions
    from funcoes import abc, double_int, say_hello, rpc_test, doggo_test, favorite_number, half_float, bye_basilio

    # Wrap all functions
    wrapped_abc = RPCClient(abc)
    wrapped_double = RPCClient(double_int)
    wrapped_hello = RPCClient(say_hello)
    wrapped_rpc_test = RPCClient(rpc_test)
    wrapped_doggo_test = RPCClient(doggo_test)
    wrapped_favorite_number = RPCClient(favorite_number)
    wrapped_half_float = RPCClient(half_float)
    wrapped_bye_basilio = RPCClient(bye_basilio)

    # Run functions that have been wrapped
    print(wrapped_abc(5, 'AAA'))
    print(wrapped_double(5.0))
    print(wrapped_hello())
    print(wrapped_doggo_test('WOOF!'))
    print(wrapped_favorite_number(11))
    print(wrapped_favorite_number(713))
    print(wrapped_rpc_test())
    print(wrapped_half_float(13.0))
    print(wrapped_bye_basilio())
