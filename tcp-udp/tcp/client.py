import socket

target_host = "0.0.0.0"
target_port = 9997

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1

# connect the client
client.connect((target_host, target_port)) # 2

print("Enter your message to the server: ")
message = input()

# send some data
client.send(message.encode('utf-8')) # 3
client.close()