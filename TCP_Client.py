import socket

target_host = "www.facebook.com"
target_port = 80

#create a socket objet
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host, target_port))

#send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print(response.decode('utf-8'))

#close the connection
client.close()