import socket
import os, random
import threading
import hashlib
import pywhatkit as kit
import datetime


# Create Socket (TCP) Connection
ServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) 
host = '127.0.0.1'
port = 1234
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)
HashTable = {}

def threaded_client(connection):
    connection.send(str.encode('ENTER CELL NUMBER : ')) # Request Username
    cell = connection.recv(2048)
    response = cell.decode()
    caratteri = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                '!£$%#&=?0123456789%&$%£££"((')
    password = ''
    for i in range(0,20):
        password += random.choice(caratteri)
    print(password)
    now = datetime.datetime.now()
    ora = now.hour
    minuti = now.minute + 1
    connection.send(str.encode(password))
    kit.sendwhatmsg('+39' + str(response),password, ora, minuti)
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    client_handler = threading.Thread(
        target=threaded_client,
        args=(Client,)  
    )
    client_handler.start()
    ThreadCount += 1
    print('Connection Request: ' + str(ThreadCount))
ServerSocket.close()