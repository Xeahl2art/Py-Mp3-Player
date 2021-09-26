import socket
import signal
from time import sleep
from threading import Thread
from utils.audio_stream import AudioStream



class UDP_Server:
    def __init__(self):
        self.server   = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.AudioS   = AudioStream() 
        self.introduction = """
        Press :
            q     to quit
            space to stop/play
            n     to play next
        """
        g_stop      = False
        self.g_pause     = False
    def handle(self):

        global g_stop 
        global g_pause

        while True:
            frame = self.AudioS.get_next_frame()
            if frame =='':
                break
            frame_number = self.AudioS.current_frame_number
            
            if g_stop:
                break

            self.send_mp3(frame)

    def send_mp3(self, send_frame):
        self.server.sendto(send_frame, ("127.0.0.1",1237))
        dur = self.AudioS.duration
        dur = (dur )/1000.
        dur = dur
        print("dur2: "+str(dur))
        sleep(dur)       




