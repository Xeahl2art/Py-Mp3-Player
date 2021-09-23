import subprocess
import asyncio
import keyboard
from time import sleep

class Client_ffplay():
    c_ffplay = subprocess.Popen([
        "ffplay", "-f", "wav",
         "-nodisp", "-autoexit","-vn",
         "rtp://127.0.0.1:1235",
        ],
        stdout=subprocess.PIPE,
        )

    async def start(self):
        self.c_ffplay.wait()
    async def start2(self):
        while True:
            if self.c_ffplay is not None:
                out = self.c_ffplay.stdout
                print(out)
                print("sdasd")
    
    async def main(self):
        
        await asyncio.gather(
                asyncio.create_task(self.start()),
                asyncio.create_task(self.start2())

            )

    

client = Client_ffplay()
asyncio.run(client.main())
