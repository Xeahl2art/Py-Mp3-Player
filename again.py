 
import subprocess
# init command
ffmpeg_command = ["ffmpeg", "-i", ".test.mp3",
         "-ab", "128k", "-acodec", "pcm_s16le", "-ac", "0",  "-map",
         "0:a", "-map_metadata", "-1", "-sn", "-vn", "-y",
         "-f", "wav", "pipe:1"]

 # excute ffmpeg command
pipe = subprocess.run(ffmpeg_command,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       bufsize=10**8)


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
        f.write(out)

out = pipe.stdout
#write_(out)
print(pipe.stderr)
process2.communicate(out)
process2.wait()
