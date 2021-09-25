from pydub import AudioSegment


class AudioStream:
    FRAME_LENGTH = 8
    AUDIO_LENGTH = 1800
    DEFAULT_FPS = 24

    AUDIO_EOF = b'\xff\xd9'


    def __init__(self, file_path=".test.mp3"):
        # for simplicity, mjpeg is assumed to be on working directory
        self._stream = open(".test4.mp3", 'rb')  
        # frame number is zero-indexed
        # after first frame is sent, this is set to zero
        self.current_frame_number = -1
        self.bytes_number =0 
        self.i=0
        self.freq   = 0
        self.bitrate = 0
        self.frameSize=0
        self.dur =-1
        self.pad =0
        self.header=0
        self.offset=0
    def close(self):
        self._stream.close()

    def get_next_frame(self) -> bytes:
        print()
        print()
        print()
        print()
        print()
        print()
        #frame_length= len(self._stream)//3000
        
        frame = self._stream.read(1)
        #print(frame[:60])
        #input()
        while self.get_header(frame) == -1:
            frame = self._stream.read(1)
        frame = self.get_mp3data(frame)
        #print("au " + str(frame[128:140]))
        print("\n")
        #self._stream[frame_length*(self.i-1):frame_length*self.i]
        self.current_frame_number += 1
        print("cur frame"+ str(self.current_frame_number))
        #self.bytes_number = frame_length * self.current_frame_number
        return frame

    def get_header(self): # -1 broke   
        self.find_pattern_in_open_file(pattern=[b'\xff',[b'\xfb',b'\xfa'])

    def find_pattern_in_open_file(self, pattern,open_file )
        for i in range(0,len(pattern)):
            pats =['']*len(pattern)    
            length_in_pats =[ len(pattern[i]) for in range(0,len(pattern))
            pats[i] = file.read(1)
    
            while pats[i] != pattern[i]: 
                pats[i] = open_file.read(1)

            by2 = self._stream.read(1)
        while by2 == b'\xff':
                by1 = by2 
                by2 = self._stream.read(1)
                
            if frame2 == b'\xfb'or frame2 == b'\xfa' : # 0b1111011 = 251 -> mp3
                frame3 =self._stream.read(1)
                frame4 =self._stream.read(1)
                frame = frame1+frame2+frame3+frame4
                print( bin( frame[0] ) )
                print( str( bin(frame[1])))
                print( str(bin(frame[2])))
                print( str(bin(frame[3])))
                print("frame: "+str( [ hex(q) for q in frame[:9] ] ))
                if frame3 == b'\x94':
                    self.offset =4
                # third byte 
                q = bin(frame[2])
                print("frame: "+str(frame[2])) 
                dif= 8 - (len(q)-2)
                q = q if dif==0 else '0b'+'0'*dif+q[2:]                  
                print("q: "+str(q))

                #bitrate
                bq = q[:6]
                BR=[64,32 ,40 ,48 ,56 ,64,80 ,96 ,112 ,128 ,160 ,192, 224 ,256, 320,-1] 
                self.bitrate =BR[int(bq,2)]
                print("bq:"+str(bq))
                print("bitrate: "+str(self.bitrate))

                #fq
                fq = '0b'+q[6:8]
                Hz = [44100,48000,32000,-1]
                print("fq: "+str(fq))
                w = int(fq,2)
                print("w: "+ str(w))
                self.freq = Hz[w]
                print("freq: "+str(self.freq))
               
                #padding bit
                qp =q[-1]

                if self.freq < 0 or self.bitrate < 0:
                    self.i +=1
                    print("\n")
                    print("-----------------------------------")
                    print("frame: "+str( [ hex(q) for q in frame[:4] ] )) 
                    print("fq: "+str(fq))
                    print("freq: "+str(self.freq))
                    print("bq:"+str(bq))
                    print("bitrate: "+str(self.bitrate))
                    print("Header skip: "+ str(self.i))
                    print("------------------------------------")
                    print("\n")
                    #input()
                    return -1
                self.header = frame
                 
                print()
                print()
                return 1
        return -1
    
    def get_mp3data(self,frame):
        self.frameSize = 144 * self.bitrate*1000 // (self.freq+self.pad)
        payload = self._stream.read(self.frameSize - self.offset )
        self.offset = 0
        alles = b''+self.header[:]+payload[:]
        print("####################")
        print("header: "+ str(self.header))
        print()
        print("payload: "+ str(payload))
        print()
        print("alles: "+ str(alles))
        print("####################")
        print("frameSize: "+ str(self.frameSize)) 
        #print(frame)
        self.dur= self.frameSize*8 / self.bitrate
        print("dur: " + str(self.dur))
        return alles

