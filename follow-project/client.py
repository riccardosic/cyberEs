from socket import *

client = socket(AF_INET, SOCK_STREAM)

client.connect(('127.0.0.1', 1234))
response = client.recv(2048)
# Input UserName
name = input(response.decode())	
client.send(str.encode(name))
response = client.recv(2048)
# Input Password
# password = input(response.decode())	
# client.send(str.encode(password))
''' Response : Status of Connection :
	1 : Registeration successful 
	2 : Connection Successful
	3 : Login Failed
'''
response = client.recv(2048)
response = response.decode()

print(response)
password = client.recv(2048).decode()
print(password)
client.close()

