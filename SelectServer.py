import select
import socket
import sys
import queue
server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)
server_address= ('localhost', 12345)
print ( 'starting up on %s port %s' % server_address)
server.bind(server_address)
server.listen(5)

inputs =[ server ]

outputs = []

message_queues ={}

while input:
    print ( '\nwaiting for the next event')
    readable,writable,exceptional =select.select(inputs,outputs,inputs)

    for s in readable:
        if s is server:
            connection,client_address=s.accept()
            print ( 'new connection from', client_address)
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection]=queue.Queue()
        else:
            data =s.recv(1024)
            if data:
                print ( 'received "%s" from %s' % (data, s.getpeername()))
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                 print ( 'closing', client_address, 'after reading no data')
                 if s in outputs:
                     outputs.remove(s)
                 inputs.remove(s)
                 s.close()

                 del message_queues[s]
    for s in writable:
        try:
            next_msg=message_queues[s].get_nowait()
        except queue.Empty:
            print ( 'output queue for', s.getpeername(), 'is empty')
            outputs.remove(s)
        else:
            print(  'sending "%s" to %s' % (next_msg, s.getpeername()))
            s.send(bytes(next_msg))
            # Handle "exceptional conditions"

    for s in exceptional:
        print ( 'handling exceptional condition for', s.getpeername())
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Remove message queue
        del message_queues[s]




