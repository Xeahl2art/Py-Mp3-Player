
with open('.test.mp3','r') as f:
    for i,e in enumerate( f.readlines() ):
        print(e)
        if i ==50:
            break


