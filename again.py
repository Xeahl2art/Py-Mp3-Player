 
import subprocess
# init command
with open('.test.mp3','rb') as f:
         chunk = f.read(7896687) # 4Kib

parts = int( len(chunk)/4)
ffmpeg_command = ["ffmpeg", "-i", ".test.mp3",
         "-re", "-ar 8000", "-f mulaw", "-f", "rtp",
         "rtp://127.0.0.1:1234",
         ]

 # excute ffmpeg command
pipe = subprocess.Popen(ffmpeg_command,
                        stdin =subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                       )


process2 = subprocess.Popen(
    [   
        'ffplay',
        '-f', 'mp3',
        'rtp://127.0.0.1:1234',
    ],  
    
)

def write_(file):
    with open(".test2.wav",'wb') as f:
        f.write(file)

pipe.wait()
pipe.communicate(input=chunk)
process2.wait()
