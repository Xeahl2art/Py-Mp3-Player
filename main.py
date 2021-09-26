from threading import Thread
import curses
from time import sleep
import socket
from utils.audio_stream import AudioStream
#from server import UDP_Server

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
            while g_pause:
                sleep(0.4)

            self.send_mp3(frame)

    def send_mp3(self, send_frame):
        self.server.sendto(send_frame, ("127.0.0.1",1237))
        dur = self.AudioS.duration
        dur = (dur )/1000.
        dur = dur
        print("dur2: "+str(dur))
        sleep(dur)       

class Controller:
    
    def __init__(self):

        srv = UDP_Server()
        self.thread_server = Thread(target=srv.handle)
        self.thread_server.start()
        sleep(0.2)

    def main(self):
        
        global g_stop 
        global g_pause

        s=''
        while 1:
            print("sdhj")
            s = self.my_input("Play-Console:")
            
            if s == "q":
                g_stop = True 
                print("asdaskdlaksdlaksdlk")
            if s == "s":
                g_pause = not g_pause
            s =''

    def my_input(self,message):
        try:
            win = curses.initscr()
            win.addstr(0, 0, message)
            while True: 
                ch = win.getch()
                if ch in range(32, 127): 
                    break
                sleep(0.1)
        finally:
            curses.endwin()
        return chr(ch)


if __name__== '__main__':

    g_stop      = False    
    g_pause     = False

    control = Controller()
    control.main()
    print("finish")

#srv.server.close()
#srv.AudioS.close()
