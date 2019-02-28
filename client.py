import crypto as c, socket, time

def client(IP, port, filename, keyfile=None):
    # ERROR CHECKING
	kf = "keyfile.txt"
	try: kf = open("keyfile.txt","rb")
	except:
		print("Error: create keyfile.txt")
		return None
	try: fn = open(filename,"wb")
	except:
		print("Error: " + filename + " does not exist")
		return None
	IPnums = IP.split('.')
	if len(IPnums) != 4:
		print("Error: Incorrect IP format")
		return None

	# ENCRYPT
	coded = c.DES(filename,"wb")

	# "SOCKET PROGRAMMING"
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	addr = (IP,port)
	s.sendto(coded, addr)

	print s.recv(1024)
	s.close()	
	
