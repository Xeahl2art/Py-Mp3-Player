from tkinter import *

class Window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master

        # Widget can take all window place
        self.pack(fill=BOTH, expand=1)

        # create exit button
        exit_button = Button(self, text="Exit", command=self.click_exit_button) 

        # place button at (0,0)
        exit_button.place(x=0, y=0)

    def click_exit_button(self):
        exit()


root = Tk()
app = Window(root)
root.wm_title("Mp3 Player ")
root.geometry("320x200")
root.mainloop()
