import subprocess
import asyncio
import keyboard
from time import sleep

class Client_ffplay():
    c_ffplay = subprocess.Popen([
        "ffplay", "-f", "wav", # "-loglevel","quiet",
         "-nodisp", "-autoexit","-vn",
         "rtp://127.0.0.1:1235",
        ],
        shell=True,
        stdout=subprocess.PIPE,
        )

    async def start(self):
        print("start")
        self.c_ffplay.wait()
        sleep(0.5)
    async def start2(self):
        print("sd")
        while True:
            sleep(2.2)
            if self.c_ffplay is not None:
                out = self.c_ffplay.stdout
                print(out)
                print(out)
                print("sdasd")
    
    async def main(self):
        
        await asyncio.gather(
                asyncio.create_task(self.start()),
                asyncio.create_task(self.start2())

            )

    

client = Client_ffplay()
asyncio.run(client.main())
