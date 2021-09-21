 
import subprocess
# init command
ffmpeg_command = ["ffmpeg", "-i", ".test.mp3",
         "-ab", "128k", "-acodec", "pcm_s16le", "-ac", "0", "-ar", "-map",
         "0:a", "-map_metadata", "-1", "-sn", "-vn", "-y",
         "-f", "wav", "pipe:1"]

 # excute ffmpeg command
pipe = subprocess.run(ffmpeg_command,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       bufsize=10**8)

 # debug
