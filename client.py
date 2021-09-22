import subprocess
import keyboard
from time import sleep

class Client_ffplay():
    client = subprocess.Popen([
        "ffplay",
         "-nodisp", "-autoexit",
         "rtp://127.0.0.1:1234",
        ],
        stdin=subprocess.PIPE,
        )

    def start(self):
        self.key_listener()
        self.client.wait()
        
    async def key_listener(self):
        while True:
            sleep(0.5)
            if keyboard.is_press_and_release("q"):
                print("asd")
                self.client.communicate(input='q')



    

client = Client_ffplay()
client.start()
