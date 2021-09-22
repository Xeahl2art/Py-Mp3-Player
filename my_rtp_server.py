import socket
from time import sleep
from threading import Thread

class RTP_Server:
    
    def init(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        BUF_SIZE = 1024

    def 

    def send_mp3(self, rtp_pkg_frame):
        
        self.server.sendto(rtp_pkg_frame[:BUF_SIZ])


