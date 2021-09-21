import subprocess



class Server_ffmpeg():

    def __init__(self,mp3_file_path):
        self.mp3_file_path = mp3_file_path



    def start(self):
        self.server = subprocess.Popen([
            "ffmpeg","-re", "-i", self.mp3_file_path,
            "-acodec", "libmp3lame", "-ab", "128k",
            "-ac","2", "-ar", "44100", "-hide_banner","-vn",
            "-f","rtp" , "rtp://127.0.0.1:1234",
            ])

        self.server.wait()

server = Server_ffmpeg(".test.mp3")
server.start()
