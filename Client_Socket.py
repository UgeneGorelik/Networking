
#example of simple Client Socket

import socket

#defining socket details

HOST='localhost'
PORT=80
BUFSIZ=256


#creatint TCP socket
client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_addr=(HOST,PORT)

#connecting socket
client_sock.connect(sock_addr)
payload='GET TIME'
#sending user defined data encoded in utf-8 to server
#and recieving data from server
try:
    while True:
        client_sock.send(payload.encode('utf-8'))
        data =client_sock.recv(BUFSIZ)
        print(repr(data))
        more = input("send data to server?   :")
        if more.lower() == 'y':
            payload = input(">>>: ")
        else:
            break
except KeyboardInterrupt:
    print('stopped')
client_sock.close()
