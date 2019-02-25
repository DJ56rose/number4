import helper as h

def DES(filename=None,key_file=None,action="encrypt"):
    # ***** ERROR CHECKING *****
    # check that required arguments are given
    if key_file == None and filename == None:
        print("Error: need to input filename and key")
        return None
    # check that key is given
    if (not isinstance(key_file,str)):
        print("Error: need to input key file")
        return None
    # check that key file (kf) exists
    try: kf = open(key_file,"rb")
    except:
        print("Error: " + key_file + " does not exist")
        return None
    # check for invalid file
    if (not isinstance(filename,str)):
        print("Error: First input must be filename (string)")
        return None
    # check that file exists
    try: f = open(filename,"rb")
    except:
        print("Error: " + filename + " does not exist")
        return None

    key = []
    with kf as x:
        temp = x.read(); key.append(temp);
        while temp != b"":
            temp = x.read(); key.append(temp)
    # do weird binary stuff - dunno how it even got working
    theKey = key[0]
    if theKey[-1] == '\n': theKey = theKey[:-1]
    # check correct key length
    if (len(theKey) != 8):
        print(theKey)
        print("Error: must give exactly 8 keys")
        return None

    # ***** ENCRYPTION AND DECRYPTION *****
    b = []  # bytes in file
    with f as x:
        temp = x.read(2); b.append(temp)
        while temp != b"":
            temp = x.read(2); b.append(temp)
    # *** ENCRYPT ***
    if (action=="encrypt"):
        print("ENCRYPTING")
        for i in range(0,8):
            cnt = 0
            while b[cnt] != b"":
                b[cnt] = h.encode(b[cnt],theKey[i])
                cnt = cnt+1
    # *** DECRYPT ***
    else:
        print("DECRYPTING")
        for i in range(0,8):
            cnt = 0
            while b[cnt] != b"":
                b[cnt] = h.decode(b[cnt],theKey[7-i])
                cnt = cnt+1
    # ** SAVE TO FILE ENCRYPTED **
    f1 = open("encrypted",'wb')
    b = ''.join(b)  #convert to string
    f1.write(b)
    f1.close()

##############################################

#DES("test1.dms","key1.dms","encrypt")
#DES("encrypted","key1.dms","decrypt")
