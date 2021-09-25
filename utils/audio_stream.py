class AudioStream:

    # Bitrate and Frequenz or Sample rate  datasheet of mp3  
    BR = [64,32 ,40 ,48 ,56 ,64,80 ,96 ,112 ,128 ,160 ,192, 224 ,256, 320,-1] 
    Hz = [44100,48000,32000,-1]
    DEBUG = 1
    

    def __init__(self, file_path=".test.mp3"):
        # for simplicity, mp3 is assumed to be on working directory
        self._stream = open(file_path, 'rb')  
        
        # frame number start at zero
        self.current_frame_number   = -1
        self.bytes_number           = -1  
        self.freq                   = 0
        self.bitrate                = 0
        self.frameSize              = 0
        self.duration               = -1
        self.header                 = 0
        self.offset                 = 0

    def close(self):
        self._stream.close()

    def get_next_frame(self) -> bytes:

        while not self.get_header(self._stream): # if header is uncorrect
           self.get_header(self._stream)

        self.current_frame_number += 1
        #frame = header and payload
        frame = self.get_mp3data(self._stream)

        #get mp3 data: framesize, duration
        if self.DEBUG:
            print('\n'*4)
            print("cur frame"+ str(self.current_frame_number))
        return frame

    def get_header(self, open_file):    
        ''' 
        return 1 if header is correct and 0 if dont
        '''
        
        pattern = self.find_pattern_in_open_file(pattern=[b'\xff',[b'\xfb',b'\xfa']], 
                open_file=open_file)
        
        by3 = open_file.read(1)
        by4 = open_file.read(1)
        self.bytes_number += 2

        #set offset 
        self.offset = 4 if by3 == b'\x94' else 0
        
        #getting information from third byte 
        by3_in_bit = bin(by3[0]) # conv by3 in bits

        # full by3_in_bit to a 8-bit string
        diff= 8 - (len(by3_in_bit)-2)
        by3_in_bit = by3_in_bit if diff==0 else '0b'+'0'*diff+by3_in_bit[2:]                  
 
        
        #bitrate
        bits_bitrate = by3_in_bit[:6]  # need first 4 bits -> '0bxxxx' because of '0b' first 6 needed
        self.bitrate =self.BR[int(bits_bitrate,2)]


        #frequenz or sammple rate
        bits_freq = '0b'+by3_in_bit[6:8]
        w = int(bits_freq,2)
        self.freq = self.Hz[w]

        
        if self.freq < 0 or self.bitrate < 0:
            if self.DEBUG:
                print("\n")
                print("-----------------------------------")
                print("freq: "+str(self.freq))
                print("bitrate: "+str(self.bitrate))
                print("Header skip "+ str(self.bytes_number))
                print("------------------------------------")
                print("\n")
                #input()
            return 0
    
        self.header = pattern[0] + pattern[1] + by3 + by4
        
        if self.DEBUG:
            print("by3_in_bit: "+str(bits_bitrate))
            print("by3_in_bit: "+str(by3_in_bit))
            print("by3: "+ str(by3))
            print("found pattern: " +str(pattern))
            print("bitrate: "+str(self.bitrate))
            print("bits_freq: "+str(bits_freq))
            print("w: "+ str(w))
            print("fby3_in_bit: "+str(bits_freq))
        
        return 1


    def find_pattern_in_open_file(self, pattern, open_file ):
        '''return found_pattern and the open_file heads to the postion after given pattern
         Example
         input: pattern = [ a, [x,y] ] -> first position must be a  and second x or y
        '''
        found_pattern = b''    
        for i in range(0,len(pattern)):
                bys =['']*len(pattern)    
                length_in_pat =[ len(pattern[k]) for k  in range(0,len(pattern))]
                bys[i] = open_file.read(1)
                self.bytes_number += 1
               
                # could be pattern of previous pattern
                if bys[i-1] == bys[i]:
                    i -=1
                    self.bytes_number -= 1
                    continue
                   
                # match bytes in pattern
                for pats in pattern[i]:
                    while bys[i] != pats: 
                        bys[i] = open_file.read(1)
                        self.bytes_number += 1
                        if bys[i] == '':
                            return "file empty"
                    else:
                        found_pattern += pats.to_bytes(1,"little")
        return found_pattern
    
    def get_mp3data(self, open_file):
        self.frameSize = 144 * self.bitrate*1000 // self.freq
        payload = open_file.read(self.frameSize - self.offset)
        self.offset = 0
        header_and_payload = self.header+payload
        self.duration= self.frameSize*8 / self.bitrate
        
        if self.DEBUG ==1:
            print("####################")
            print("header: "+ str(self.header))
            print()
            print("payload: "+ str(payload))
            print()
            print("alles: "+ str(header_and_payload))
            print("####################")
            print("frameSize: "+ str(self.frameSize)) 
            print("dur: " + str(self.duration))
        
        return header_and_payload 

