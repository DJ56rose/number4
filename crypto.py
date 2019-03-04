import helper as h

# inData may either be filename or actual data

def DES(inData,action="encrypt"):
    # hardcoded key
    theKey = "a7hd70mj"

    # ***** ENCRYPTION AND DECRYPTION *****
    b = []  # bytes in file

    dataFlag = False   
    try: f = open(inData,"rb")
    except:
        print("Assuming data is given (not a file)")
        dataFlag = True

    # File is given
    if not dataFlag:
        with f as x:
            temp = x.read(2); b.append(temp)
            while temp != b"":
                temp = x.read(2); b.append(temp)
    # Data is given
    else: 
        bTemp = inData
        for i in range(0,len(bTemp),2):
            t = bTemp[i]+bTemp[i+1]
            t = t.encode('utf-8')
            b.append(t)
        b.append(b'\n')

    # *** ENCRYPT ***
    bts = []    # the actual encoded thing
    if (action=="encrypt"):
        print("ENCRYPTING")
        for i in range(0,8):
            cnt = 0
            while len(b[cnt]) == 2: 
                print(b[cnt])
                b[cnt] = h.encoder(b[cnt],ord(theKey[i]))
                if i == 7: bts = bts+b[cnt]
                cnt = cnt+1
        print("done with stuff...")
    # *** DECRYPT ***
    else:
        print("DECRYPTING")
        for i in range(0,8):
            cnt = 0
            while b[cnt] != b"":
                b[cnt] = h.decoder(b[cnt],ord(theKey[7-i]))
                if i == 7: bts = bts+b[cnt]
                cnt = cnt+1
    return bts

DES('hello worlds')
DES('test')
