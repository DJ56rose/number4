import crypto as c, socket, datetime, sys

port = int(sys.argv[1])
print(port)
print(type(port))

# INIT SOCKET
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',port))

# LISTEN
while True:
	msg,addr = s.recvfrom(1024)
    print("type of msg is " + str(type(msg)))
	toSend = bytearray(c.DES(msg))
	stamp = datetime.datetime.now()
	s.sendto(toSend,addr)
