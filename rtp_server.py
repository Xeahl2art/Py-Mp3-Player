import socket as s
from time import sleep

localIp = "localhost"
port    = 1234
buffers = 1024

udps = s.socket(s.AF_INET, s.SOCK_DGRAM)
udps.bind((localIp, port))

recv=None
while recv is None:
    #recv = udps.recvfrom(buffers)

    #message = recv[0]
    #address = recv[1]

    #clientMsg = "Message from Client:{}".format(message)
    #clientIP  = "Client IP Address:{}".format(address)
    
    #print(clientMsg)
    #print(clientIP)

    with open(".test.mp3","rb") as f:
        c_adress = ("localhost",1235)
        with open("rtp_info.sdp","rb")as f2:
            sdp = f2.read()
           
            while 1:
                pkg = f.read(1024)
                if not pkg:
                    break
                udps.sendto( sdp , c_adress)
                udps.sendto( pkg , c_adress)
                #sleep(0.2)

