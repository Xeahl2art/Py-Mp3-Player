import ffmpeg
import subprocess

in_filename = '.test.mp3'

with open('.test.mp3','rb') as f:
         chunk = f.read(7896687) # 4Kib
process1 = (
    ffmpeg
    .input('pipe:', format='mp3')
    # (filters/etc. go here)
    .output('pipe:', format='mp3')
    .run_async(pipe_stdout=True)
)

myproc = subprocess.Popen([

    'ffmpeg',
    '-f mp3',
    '-i pipe:',
    '-o pipe:',
    '-f mp3',
    ],
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)


process2 = subprocess.Popen(
    [
        'ffplay',
        '-f', 'mp3',
        '-i', 'pipe:',
    ],
    stdin=subprocess.PIPE,
)

myproc.wait()
#myproc.stdin.write(chunk)
out = myproc.communicate(chunk)[0]
print(out)
#process1.wait()

#process2.communicate(out)[0]
#process2.wait()


