from socket import socket, AF_INET, SOCK_DGRAM

DEFAULT_SERVER = ('127.0.0.1', 11113) 


class Client():
    '''
    Simple client written in Python3. Polls a server and waits for its response.
    '''
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(('127.0.0.1', 0)) # OS chooses port
        self.socket_name = self.socket.getsockname()
    
    def poll_server(self, data,  server=DEFAULT_SERVER):
        self.socket.sendto(bytes(data, "utf-8"), server)
        response = self.socket.recvfrom(2048)
        self.socket.close()
        return response


if __name__ == '__main__':
    test_client = Client()
    data = {'username': 'pippo', 'password': None}
    print(test_client.poll_server(data['username']))