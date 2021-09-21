import ffmpeg
import subprocess

in_filename = '.test.mp3'

with open('.test.mp3','rb') as f:
         chunk = f.read(7896687) # 4Kib
process1 = (
    ffmpeg
    .input('pipe: -f mp3')
    # (filters/etc. go here)
    .output('pipe: ')
    .run_async(pipe_stdout=True)
)

myproc = subprocess.run([

    'ffmpeg',
    '-f mp3',
    '-i pipe:',
    'pipe:1',
       ],
    
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    bufsize=10**8,
)


process2 = subprocess.Popen(
    [
        'ffplay',
        '-f', 'mp3',
        '-i', 'pipe:',
    ],
    stdin=subprocess.PIPE,
)

#process1.wait()
#myproc.stdin.write(chunk)
#out = myproc.communicate(chunk)[0]
myproc.stdout
#print(out)
#process1.wait()

#process2.communicate(out)[0]
#process2.wait()


