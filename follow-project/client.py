from socket import *

client = socket(AF_INET, SOCK_STREAM)

client.connect(('127.0.0.1', 1234))
response = client.recv(2048)
# Input phone
phone = input(response.decode())	
#client.send(str.encode(str(phone)))
client.send(str.encode(phone))
#response = client.recv(2048)
# Input Password
password = input('ENTER PASSWORD: ')	
# client.send(str.encode(password))
''' Response : Status of Connection :
	1 : Registeration successful 
	2 : Connection Successful
	3 : Login Failed
'''
#response = client.recv(2048)
client.send(str.encode(password))

connOk = client.recv(2048).decode()
print(connOk)
if str(connOk) != 'connessione sicura':
	client.close()

