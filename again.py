 
import subprocess
# init command
with open('.test.mp3','rb') as f:
         chunk = f.read(7896687) # 4Kib


ffmpeg_command = ["ffmpeg", "-i", "-",
         "-ab", "128k", "-acodec", "pcm_s16le", "-ac", "0",  "-map",
         "0:a", "-map_metadata", "-1", "-sn", "-vn", "-y",
         "-f", "wav", "-"]

 # excute ffmpeg command
pipe = subprocess.Popen(ffmpeg_command,
                        stdin =subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                       )


process2 = subprocess.Popen(
    [   
        'ffplay',
        '-f', 'wav',
        '-i', '-',
    ],  
    stdin=subprocess.PIPE,
)

def write_(file):
    with open(".test2.wav",'wb') as f:
        f.write(file)

print(len(chunk))
out = pipe.communicate(input=chunk)[0]
write_(out)
print(pipe.stderr)
process2.communicate(out)
process2.wait()
