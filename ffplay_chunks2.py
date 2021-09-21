import ffmpeg
import subprocess

in_filename = '.test.mp3'
width, height = 1920, 1080  # (or use ffprobe or whatever)

process1 = (
    ffmpeg
    .input(in_filename)
    # (filters/etc. go here)
    .output('pipe:', format='mp3')
    .run_async(pipe_stdout=True)
)
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
