from pydub import AudioSegment


class AudioStream:
    FRAME_LENGTH = 8
    AUDIO_LENGTH = 1800
    DEFAULT_FPS = 24

    AUDIO_EOF = b'\xff\xd9'


    def __init__(self, file_path=".test.mp3"):
        # for simplicity, mjpeg is assumed to be on working directory
        self._stream = open(".test.mp3", 'rb')  
        # frame number is zero-indexed
        # after first frame is sent, this is set to zero
        #self._stream = AudioSegment.from_mp3(".test.mp3").raw_data
        self.current_frame_number = -1
        self.bytes_number =0 
        self.i=1
    def close(self):
        self._stream.close()

    def get_next_frame(self) -> bytes:
        
        #frame_length= len(self._stream)//3000
        frame = self._stream.read(1024) 
        print("au" + str(frame[:5]))
        #self._stream[frame_length*(self.i-1):frame_length*self.i]
        self.current_frame_number += 1
        self.i+=1
        #self.bytes_number = frame_length * self.current_frame_number
        return frame
