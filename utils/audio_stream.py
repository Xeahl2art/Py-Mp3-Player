class AudioStream:
    FRAME_LENGTH = 8
    AUDIO_LENGTH = 1800
    DEFAULT_FPS = 24

    AUDIO_EOF = b'\xff\xd9'


    def __init__(self, file_path=".test__rtp_mpegts"):
        # for simplicity, mjpeg is assumed to be on working directory
        self._stream = open(file_path, 'rb')
        # frame number is zero-indexed
        # after first frame is sent, this is set to zero
        self.current_frame_number = -1
        self.bytes_number =0 
    def close(self):
        self._stream.close()

    def get_next_frame(self) -> bytes:
        
        frame_length= 8
        frame = self._stream.read(frame_length)
        self.current_frame_number += 1
        self.bytes_number = frame_length * self.current_frame_number
        return bytes(frame)
