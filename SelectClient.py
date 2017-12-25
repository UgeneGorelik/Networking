#-----------------------------------------------------------------------------
#this example shows how to use Python Feature called SELECT
#thats "Knows" what socket is available to send which to recieve and which is errored
#-----------------------------------------------------------------------------



import socket
import sys



messages = [ 'MESSAGE',
             ]
server_address = ('localhost', 12345)

# create socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          ]

#create 2 sockets one input one output
for s in socks:
    s.connect(server_address)

#send message
for message in messages:
    for s in socks:
        print ( '%s: sending "%s"' % (s.getsockname(), message))
        s.send(message.encode('utf-8'))

#recieveing messgae
    for s in socks:
        data = s.recv(1024)
#close if data is null
        if not data:
            print >>sys.stderr, 'closing socket', s.getsockname()
            s.close()