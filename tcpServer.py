import socket
#TCP protocol Server
#tcp protocol establishes connection and also have packet valiadtiob
#packet validation trough congestion window


def Main():
    # declare the host and port of socket
    host = 'localhost'
    port = 12345
    #create and bind socket to the port/host
    s = socket.socket()
    s.bind((host,port))

    #listen to incoming connections
    s.listen(1)
    #accept connection
    c,addr = s.accept()
    print("we got connected from : "+  str(addr))
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("we got from user :" + str(data))
        data=str(data).upper()
        print("sending:" +str(data))
        c.send(data.encode('utf-8'))
    c.close()

if __name__=='__main__':
    Main()

