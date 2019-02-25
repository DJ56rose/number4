def encode(bits,key):
    # swap
    bits = list(bits)   #convert to list
    #print("PRINTING BITS"); print(bits)
    # pad
    if (len(bits)%2 != 0):
        bits.append(32)   #append space
    bits[0],bits[1] = bits[1],bits[0]
    # XOR with key
    bits[1] = bits[1]^key
    # Return
    return bits

def encodeHeader(bits,key):
    print(bits); print(key)
    e = bits #init
    for i in range(0,len(key)):
        print(e)
        if i == 8: return e
        for j in range(0,8,2):
            e[j:j+2] = encode(e[j:j+2],key[i])
    # convert to byte
    #for i in range(0,len(e)):
    #    e[i] = (e[i]).to_bytes(1,byteorder='big')

def decode(bits,key):
    # XOR right
    bits = list(bits)
    if (len(bits)%2 != 0): bits.append(32)
    bits[1] = bits[1]^key
    # swap
    bits[1],bits[0] = bits[0],bits[1]
    # Return
    return bits

#d - data, p - pseudo header, h - header
def checksum(d,p,h):
    # preprocess
    sum = 1
    pseudo = p[0]; header = h[0]
    for i in range(1,len(p)): pseudo += p[i]
    for j in range(1,len(h)): header += h[j]
    p1 = [pseudo[i:i+2] for i in range(0,len(pseudo),2)]
    h1 = [header[i:i+2] for i in range(0,len(header),2)]
    # perform sum
    for i in range(0,len(p1)-2,2):
        temp = int.from_bytes(p1[i],byteorder='little')
        temp2 = int.from_bytes(p1[i+2],byteorder='little')
    # Return complement
    sum = (sum).to_bytes(2,byteorder='big')
    return sum
