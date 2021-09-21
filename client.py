import socket
import json
import pickle

ip = "127.0.0.1" # input("IP-Adresse: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((ip, 1234))

data = {'x':[1,2,3,5,6,7]}
s.close()
#try: 
#    while True: 
#        data = pickle.dumps(data)
#        s.send(data) 
#        antwort = s.recv(1024) 
#        print("[{}] {}".format(ip, antwort.decode())) 
#finally: 
#    s.close()
