import crypto as c, socket, datetime, sys

port = int(sys.argv[1])

# INIT SOCKET
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',port))

# for updating disp
k = 0; disp = []

# LISTEN
while True:
    # receive
    msg,addr = s.recvfrom(1024)
    IP_client = addr[0]
    # decrypt + append time
    stamp = str(datetime.datetime.now())
    toSend = c.DES(msg,"decrypt")    #+ stamp
    # get IP addresses
    hostName = socket.gethostname()
    hostIP = str(socket.gethostbyname(hostName))
    # print
    for i in range(0,len(toSend)): toSend[i] = chr(toSend[i])
    printer = ''.join(toSend)
    toPrint = stamp+': '+printer+"\n    Client IP: "+IP_client+", Server IP: "+hostIP
    disp.append(toPrint)
    goto = len(disp)
    if goto > 5: k = goto - 5
    for i in range(k,goto):
        print(disp[i])
    # encrypt + send
    stamp = list(stamp)+[':',' ']
    toSend = c.DES(stamp+toSend)
    # send back
    s.sendto(bytes(toSend),addr)
    print("===      ===     ===")
