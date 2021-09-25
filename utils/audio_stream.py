from pydub import AudioSegment


class AudioStream:
    FRAME_LENGTH = 8
    AUDIO_LENGTH = 1800
    DEFAULT_FPS = 24

    AUDIO_EOF = b'\xff\xd9'

    # Bitrate datasheet of mp3  
    BR=[64,32 ,40 ,48 ,56 ,64,80 ,96 ,112 ,128 ,160 ,192, 224 ,256, 320,-1] 
    Hz = [44100,48000,32000,-1]
    def __init__(self, file_path=".test.mp3"):
        # for simplicity, mjpeg is assumed to be on working directory
        self._stream = open(".test4.mp3", 'rb')  
        # frame number is zero-indexed
        # after first frame is sent, this is set to zero
        self.current_frame_number = -1
        self.bytes_number =0 
        self.freq   = 0
        self.bitrate = 0
        self.frameSize=0
        self.dur =-1
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
        #while self.get_header(frame) == -1:
        #    frame = self._stream.read(1)
        #frame = self.get_mp3data(frame)
        #print("au " + str(frame[128:140]))
        print("\n")
        #self._stream[frame_length*(self.i-1):frame_length*self.i]
        self.current_frame_number += 1
        print("cur frame"+ str(self.current_frame_number))
        #self.bytes_number = frame_length * self.current_frame_number
        return frame

    def get_header(self,open_file): # -1 broke   
        pattern = self.find_pattern_in_open_file(pattern=[b'\xff',[b'\xfb',b'\xfa']], 
                open_file=open_file)

        print("found pattern: " +str(pattern))
        
        by3 = open_file.read(1)
        print("by3: " str(by3))

        #set offset 
        self.offset = 4 if by3 == b'\x94' else 0
        
        #getting information from third byte 
        by3_in_bit = bin(by[0]) # conv by3 in bits

        # full by3_in_bit to a 8-bit string
        diff= 8 - (len(by3_in_bit)-2)
        by3_in_bit = by3_in_bit if dif==0 else '0b'+'0'*dif+by3_in_bit[2:]                  
        print("by3_in_bit: "+str(by3_in_bit))
 
        
        #bitrate
        bby3_in_bit = by3_in_bit[:6]  # need first 4 bits -> '0bxxxx' because of '0b' first 6 needed
        self.bitrate =self.BR[int(bby3_in_bit,2)]
        print("by3_in_bit: "+str(bby3_in_bit))
        print("bitrate: "+str(self.bitrate))



        #frequenz or sammple rate
        fq = '0b'+by3_in_bit[6:8]
        print("fby3_in_bit: "+str(fq))
        w = int(fby3_in_bit,2)
        print("w: "+ str(w))
        self.fq = self.Hz[w]
        print("fq: "+str(fq))



    def find_pattern_in_open_file(self, pattern, open_file ):
        '''return found_pattern and the open_file heads to the postion after given pattern
         Example
         input: pattern = [ a, [x,y] ] -> first position must be a  and second x or y
        '''
        found_pattern =['']*len(pattern)    
        for i in range(0,len(pattern)):
                bys =['']*len(pattern)    
                length_in_pat =[ len(pattern[k]) for k  in range(0,len(pattern))]
                bys[i] = open_file.read(1)
                
                # could be pattern of previous pattern
                if bys[i-1] == bys[i]:
                    i -=1
                    continue
                   
                # match bytes in pattern
                for pats in pattern[i]:
                    while bys[i] != pats: 
                        bys[i] = open_file.read(1)
                        if bys[i] == '':
                            return "file empty"
                    else:
                        found_pattern[i] = pats
        return found_pattern

#            if frame2 == b'\xfb'or frame2 == b'\xfa' : # 0b1111011 = 251 -> mp3
#                frame3 =self._stream.read(1)
#                frame4 =self._stream.read(1)
#                frame = frame1+frame2+frame3+frame4
#                print( bin( frame[0] ) )
#                print( str( bin(frame[1])))
#                print( str(bin(frame[2])))
#                print( str(bin(frame[3])))
#                print("frame: "+str( [ hex(q) for q in frame[:9] ] ))
#                if frame3 == b'\x94':
#                    self.offset =4
#                # third byte 
#                q = bin(frame[2])
#                print("frame: "+str(frame[2])) 
#                dif= 8 - (len(q)-2)
#                q = q if dif==0 else '0b'+'0'*dif+q[2:]                  
#                print("q: "+str(q))
#
#                #bitrate
#                bq = q[:6]
#                BR=[64,32 ,40 ,48 ,56 ,64,80 ,96 ,112 ,128 ,160 ,192, 224 ,256, 320,-1] 
#                self.bitrate =BR[int(bq,2)]
#                print("bq:"+str(bq))
#                print("bitrate: "+str(self.bitrate))
#
#                #fq
#                fq = '0b'+q[6:8]
#                Hz = [44100,48000,32000,-1]
#                print("fq: "+str(fq))
#                w = int(fq,2)
#                print("w: "+ str(w))
#                self.freq = Hz[w]
#                print("freq: "+str(self.freq))
#               
#                #padding bit
#                qp =q[-1]
#
#                if self.freq < 0 or self.bitrate < 0:
#                    self.i +=1
#                    print("\n")
#                    print("-----------------------------------")
#                    print("frame: "+str( [ hex(q) for q in frame[:4] ] )) 
#                    print("fq: "+str(fq))
#                    print("freq: "+str(self.freq))
#                    print("bq:"+str(bq))
#                    print("bitrate: "+str(self.bitrate))
#                    print("Header skip: "+ str(self.i))
#                    print("------------------------------------")
#                    print("\n")
#                    #input()
#                    return -1
#                self.header = frame
#                 
#                print()
#                print()
#                return 1
#        return -1
    
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

