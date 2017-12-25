
#-----------------------------------------------------------------------------
#this example shows how to use Python Feature called SELECT
#thats "Knows" what socket is available to send which to recieve and which is errored
#-----------------------------------------------------------------------------


import select
import socket
import sys
import queue

#create Socket
server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)
server_address= ('localhost', 12345)
print ( 'starting up on %s port %s' % server_address)
server.bind(server_address)
server.listen(5)




inputs =[ server ]

outputs = []

#define Queue for sockets  which will be sent when socket is ready
message_queues ={}

while input:

#HERE we define the select and three lists each one accordingly will be sockets
#accordingly one  gets data ,one sends and one Errored

    readable,writable,exceptional =select.select(inputs,outputs,inputs)

    for s in readable:
        if s is server:
            connection,client_address=s.accept()
            print ( 'new connection from', client_address)
            connection.setblocking(0)
        # append to queue as  listening
            inputs.append(connection)
            message_queues[connection]=queue.Queue()
        else:
            data =s.recv(1024)
            if data:
            #send data to socket
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:

                 if s in outputs:
                     outputs.remove(s)
                 inputs.remove(s)
                 s.close()

                 del message_queues[s]
    for s in writable:
        try:
            next_msg=message_queues[s].get_nowait()
        except queue.Empty:

            outputs.remove(s)
        else:

            s.send(bytes(next_msg))
            # Handle "exceptional conditions"

    for s in exceptional:

        # if exception stops
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Remove  queue
        del message_queues[s]




