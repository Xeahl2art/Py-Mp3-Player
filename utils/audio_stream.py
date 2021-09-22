from pydub import AudioSegment


class AudioStream:
    FRAME_LENGTH = 8
    AUDIO_LENGTH = 1800
    DEFAULT_FPS = 24

    AUDIO_EOF = b'\xff\xd9'


    def __init__(self, file_path=".test.mp3"):
        # for simplicity, mjpeg is assumed to be on working directory
        #self._stream = open(file_path, 'rb')  
        # frame number is zero-indexed
        # after first frame is sent, this is set to zero
        self._stream = AudioSegment.from_mp3(".test.mp3")
        self.current_frame_number = -1
        self.bytes_number =0 
        self.i=1
    def close(self):
        self._stream.close()

    def get_next_frame(self) -> bytes:
        
        frame_length= len(self._stream)//3000
        if self.i > 3000:
            return bytes(self.AUDIO_EOF)
        frame = self._stream[frame_length*(self.i-1):frame_length*self.i]
        self.current_frame_number += 1
        self.bytes_number = frame_length * self.current_frame_number
        return bytes(frame)
