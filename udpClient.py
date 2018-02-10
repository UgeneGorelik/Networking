import socket

def Main():
    host = 'localhost'
    port=  54321

    server =('localhost',12345)

    s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))

    message=input(">>")
    while message!='q':
        s.sendto(message.encode('utf-8'),server)
        data ,addr =s.recvfrom(1024)
        print("recieved from server : " +str(data) )
        message=input(">>")
    s.close()

if __name__=="__main__":
    Main()