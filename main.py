import multithreading
import subprocess
from tkinter import *
from pydub import AudioSegment
from pydub.playback import play

class Window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master

        # Widget can take all window place
        self.pack(fill=BOTH, expand=1)

        # create exit button
        exit_btn = Button(self, text="Exit", command=self.click_exit_btn) 
        exit_btn.place(x=0, y=0)
        
        # create play button
        play_btn = Button(self, text="Play", command=self.click_play_btn)
        play_btn.place(x=10,y=10)

    def click_play_btn(self):
        song = AudioSegment.from_mp3("test.mp3")
        play(song)

    def click_stop_btn(self):
        

    def click_exit_btn(self):
        exit()


root = Tk()
app = Window(root)
root.wm_title("Mp3 Player ")
root.geometry("320x200")
root.mainloop()
