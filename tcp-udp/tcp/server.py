import socket
import threading

IP = '0.0.0.0' # \ 
#                 -- 1
PORT = 9998 #   /

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5) # 2
    print(f'[*] Listening on {IP}:{PORT}')

    while True: # 3
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,)) # 4
        client_handler.start()
    
def handle_client(client_socket): # 5
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()