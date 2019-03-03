import crypto as c, socket, datetime, sys

port = sys(argv[1])

# INIT SOCKET
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',port))

# LISTEN
while True:
	msg,addr = s.recvfrom(1024)
	msg = c.decrypt(msg)
	stamp = datetime.datetime.now()
	s.sento(stamp+msg,addr)

