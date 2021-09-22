import socket as s
from time import sleep
import io
io.DEFAULT_BUFFER_SIZE =131072
localIp = "localhost"
port    = 1234
buffers = 1024

udps = s.socket(s.AF_INET, s.SOCK_DGRAM)
#udps.setsockopt(s.SOL_SOCKET,s.SO_SNDBUF,131072)
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

    with open(".test_rtp","rb") as f:
        c_adress = ("localhost",1235)
        with open("rtp_info2.sdp","rb")as f2:
            sdp = f2.read()
           
            while 1:
                pkg = f.read(1024*8)
                if not pkg:
                    break
                #udps.sendto( sdp , c_adress)
                udps.sendto( pkg , c_adress)
                #sleep(0.15)

