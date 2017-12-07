import socket
import struct

HOST='localhost'
PORT=12345
BUFSIZE=4096
MSG_LEN=4

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((HOST,PORT))
sock.listen(1)

sc,addr=sock.accept()
tot_len=0


while True:
    data=bytearray()
    data=sc.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
    tosend = input(">>")
    sc.send(tosend.encode('utf-8'))




