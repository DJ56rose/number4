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
    msgByte = bytearray(msg)
    tempFile = open("temp","wb")
    tempFile.write(msgByte)
    print(msg)
	msg = c.DES("temp")
	stamp = datetime.datetime.now()
	s.sendto(stamp+msg,addr)
