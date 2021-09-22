

def show_32bit(by):
    for i,b in enumerate(by):
        print(f"{b:08b} ", end='\n' if (i+1) % 4 ==0 else ' ' )


f = open(".test.mp3", "rb")
q = f.read()
