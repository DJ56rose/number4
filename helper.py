def encoder(bits,key):
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

def decoder(bits,key):
    # XOR right
    bits = list(bits)
    if (len(bits)%2 != 0): bits.append(32)
    bits[1] = bits[1]^key
    # swap
    bits[1],bits[0] = bits[0],bits[1]
    # Return
    return bits
