




class InvalidPacketException(Exception):
    pass

class RTPacket:
    # default header info

    HEADER_SIZE = 12    # bytes
    VERSION     = 0b10  # 2 bits .> current version 2
    PADDING     = 0b0   # 1 bit
    EXTENSION   = 0b0   # 1 bit
    CC          = 0x0   # 4 bits
    MARKER      = 0b0   # 1 bit
    SSRC        = 0x00000000 # 32 bits

    class TYPE: 
        MJPEG = 26

    def __init__(self, 
                payload_type: int = None,
                sequence_number: int = None,
                timestamp: int = None,
                payload:bytes =None):

        self.paylaod        = payload
        self.payload_type   = payload_type
        self.sequence_number= sequence_number
        self.timestamp      = timestamp


