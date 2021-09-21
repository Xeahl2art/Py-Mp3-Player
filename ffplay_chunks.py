import subprocess

with open('.test.mp3','rb') as f:
        chunk = f.read(4096) # 4Kib
ffplay_proc = subprocess.Popen('ffplay', shell=True, stdin=subprocess.PIPE)
ffplay_proc.stdin.write(chunk)



