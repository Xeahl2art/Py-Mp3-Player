import socket
from time import sleep
from  threading import Thread

from utils.rtp_packet import RTPPacket


from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3(".test.mp3")

def wait_con():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = "localhost", 1234

    s.bind(address)
    s.listen(1)
    print(f"Listening for con.. ")
    conc, client_addr = s.accept()
    print(f"conc {conc} client_addr {client_addr}")
    
wait_con()

