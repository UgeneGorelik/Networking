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
while tot_len<MSG_LEN:
    msg_len=sc.recv(MSG_LEN)
    tot_len=len(msg_len)
    data=""
    msg_len = struct.unpack('>I', msg_len)[0]
    tot_data_len=0
while len(data)<msg_len:
       chunk=sc.recv(BUFSIZE)
       if not chunk:
                break
       else:
            data=data+chunk.decode('utf-8')
print(data)

# while True:
#     data=bytearray()
#     data=sc.recv(BUFSIZE)
#     if not data:
#         break
#     print(data.decode('utf-8'))
#     tosend = input(">>")
#     sc.send(tosend.encode('utf-8'))

print(data)



