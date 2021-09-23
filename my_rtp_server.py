import socket
from time import sleep
from threading import Thread
from utils.audio_stream import AudioStream

class UDP_Server:
    
    def __init__(self):
        self.server   = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.AudioS   = AudioStream() 
    
    def handle(self):
        while True:
            frame = self.AudioS.get_next_frame()
            if frame =='':
                break
            frame_number = self.AudioS.current_frame_number
            if (frame_number+1) % 500 ==0:
                print(frame[:5])
                sleep(5)
            self.send_mp3(frame)
    
    def send_mp3(self, send_frame):
        self.server.sendto(send_frame, ("127.0.0.1",1237))
        sleep(0.128/2.)



srv = UDP_Server()
srv.handle()
print("finish")
srv.server.close()
srv.AudioS.close()


