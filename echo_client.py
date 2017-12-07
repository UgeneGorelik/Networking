import socket
import struct

HOST='localhost'
PORT=12345
BUFSIZE=4096
MSG_LEN=4

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.connect((HOST,PORT))




while True:
    tosend = input(">>")
    sock.send(tosend.encode('utf-8'))
    data=sock.recv(BUFSIZE)
    print(data.decode('utf-8'))