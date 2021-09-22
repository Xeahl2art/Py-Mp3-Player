import socket
from time import sleep
from threading import Thread
from utils.audio_stream import AudioStream
from utils.rtp_packet import RTPPacket

class RTP_Server:
    
    def __init__(self):
        self.server   = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.BUF_SIZE = 1024
        self.AudioS   = AudioStream() 
    def handle(self):
        sleep(1)
        while True:
            frame = self.AudioS.get_next_frame()
            if frame is None:
                break
            frame_number = self.AudioS.current_frame_number
            rtp_pkg = RTPPacket(
                    payload_type    = RTPPacket.TYPE.MPA,
                    sequence_number = frame_number,
                    timestamp       = frame_number*48000,
                    payload         = frame,
                    )
            
            pkg =rtp_pkg.get_packet()
            if frame_number % 1000 ==0:
                print( self.AudioS.bytes_number/7896687)
            self.send_mp3(pkg)
    
    def send_mp3(self, rtp_pkg_frame):
        self.server.sendto(rtp_pkg_frame, ("127.0.0.1",1235))
        sleep(0.0003)


srv = RTP_Server()
srv.handle()
srv.server.close()
srv.AudioS.close()


