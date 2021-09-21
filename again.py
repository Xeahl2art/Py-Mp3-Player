 
import subprocess
# init command
with open('.test.mp3','rb') as f:
         chunk = f.read(7896687) # 4Kib


ffmpeg_command = ["ffmpeg", "-i", "pipe:2",
         "-ab", "128k", "-acodec", "pcm_s16le", "-ac", "0",  "-map",
         "0:a", "-map_metadata", "-1", "-sn", "-vn", "-y",
         "-f", "wav", "pipe:1"]

 # excute ffmpeg command
pipe = subprocess.Popen(ffmpeg_command,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       )


process2 = subprocess.Popen(
    [   
        'ffplay',
        '-f', 'wav',
        '-i', 'pipe:',
    ],  
    stdin=subprocess.PIPE,
)

def write_(file):
    with open(".test2.wav",'wb') as f:
        f.write(file)
#pipe.stdin = chunk
out = pipe.communicate(input=chunk.hex())[0]
#write_(out)
print(pipe.stderr)
process2.communicate(out)
#process2.wait()
