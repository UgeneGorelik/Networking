import socket

#UDP server doest establishes connection
#can 

def Main():
    host='localhost'
    port=12345

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    print("server started")
    while True:
        data,addr = s.recvfrom(1024)
        print("message from : "+ str(addr))
        print("from user we got" + str(data))
        data=str(data).upper()
        print("sending data")
        s.sendto(data.encode('utf-8'),addr)
    s.close()

if __name__=='__main__':
    Main()