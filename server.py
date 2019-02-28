import crypto as c, socket

def server(port,keyfile=None):
	# INIT SOCKET
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind(('',port)

	# LISTEN
	while True:
		msg,addr = s.recvfrom(1024)
		msg = msg.upper()
		# concat in msg timestamp!
		s.sento(msg,addr)
		s.close()	# is this necessary?
