import ffmpeg
import subprocess

in_filename = '.test.mp3'

with open('.test.mp3','rb') as f:
         chunk = f.read(4096) # 4Kib
process1 = (
    ffmpeg
    .input("pipe:")
    # (filters/etc. go here)
    .output('pipe:', format='mp3')
    .run_async(pipe_stdout=True)
)
process1.stdin(chunk)
process2 = subprocess.Popen(
    [
        'ffplay',
        '-f', 'mp3',
        '-i', 'pipe:',
    ],
    stdin=process1.stdout,
)
process1.wait()
process2.wait()
