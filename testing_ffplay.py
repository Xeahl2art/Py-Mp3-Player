from time import sleep

import subprocess 


client = subprocess.Popen([
        "ffplay",
         "-nodisp", "-autoexit","-sample_rate ", "1026",
         "-",
        ],
        stdin=subprocess.PIPE,
        )

with open(".test.mp3","rb") as f:
    data = f.read(1026)
    while data is not None:
        client.communicate(input=data)
        client.wait()
        sleep(1)
