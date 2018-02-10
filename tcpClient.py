import socket

#TCP protocol Client
#tcp protocol establishes connection and also have packet valiadtiob
#packet validation trough congestion window


def Main():
    #declare the host and port of socket
    host='localhost'
    port=12345

    #create socket
    s=socket.socket()
    #connect to existing socket
    s.connect((host,port))

    #message shoudl be encoded
    message=input(">>").encode('utf-8')
    while message!='q'.encode('utf-8'):
        s.send(message)
        data=s.recv(1024)
        print('Recieved from server :' + str(data))
        message=input(">>").encode('utf-8')

if __name__=='__main__':
    Main()