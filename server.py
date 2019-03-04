import crypto as c, socket, datetime, sys

port = int(sys.argv[1])

# INIT SOCKET
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',port))

# LISTEN
while True:
    # receive
	msg,addr = s.recvfrom(1024)
    # decrypt + append time
    stamp = str(datetime.datetime.now())
	toSend = c.DES(msg,"decrypt") + stamp
    # encrypt + send
    toSend = c.DES(toSend) 
	print(toSend)
    # send back
	s.sendto(toSend,addr)
