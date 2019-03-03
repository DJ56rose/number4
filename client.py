import crypto as c, socket, datetime, sys

IP = sys(argv[1])
port = sys(argv[2])
filename = sys(argv[3])

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

msg = s.recvfrom(1024)
stamp = datetime.datetime.now()
print(msg+stamp)
s.close()	
	
