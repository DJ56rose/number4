import helper as h

def DES(filename,action="encrypt"):
    # hardcoded key
    theKey = "a7hd70mj"

    # ***** ENCRYPTION AND DECRYPTION *****
    b = []  # bytes in file
    f = open(filename,"rb")
    with f as x:
        temp = x.read(2); b.append(temp)
        while temp != b"":
            temp = x.read(2); b.append(temp)
    # *** ENCRYPT ***
    bts = []    # the actual encoded thing
    if (action=="encrypt"):
        print("ENCRYPTING")
        for i in range(0,8):
            cnt = 0
            while b[cnt] != b"":
                b[cnt] = h.encoder(b[cnt],ord(theKey[i]))
                if i == 7: bts = bts+b[cnt]
                cnt = cnt+1
    # *** DECRYPT ***
    else:
        print("DECRYPTING")
        for i in range(0,8):
            cnt = 0
            while b[cnt] != b"":
                b[cnt] = h.decoder(b[cnt],theKey[7-i])
                if i == 7: bts = bts+b[cnt]
                cnt = cnt+1
    return bts
