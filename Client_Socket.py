import socket

HOST='localhost'
PORT=80
BUFSIZ=256

client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_addr=(HOST,PORT)
client_sock.connect(sock_addr)
payload='GET TIME'
try:
    while True:
        client_sock.send(payload.encode('utf-8'))
        data =client_sock.recv(BUFSIZ)
        print(repr(data))
        more = input("Want to send more data to server[y/n]   :")
        if more.lower() == 'y':
            payload = input("Enter payload: ")
        else:
            break
except KeyboardInterrupt:
    print('interupted')
client_sock.close()
