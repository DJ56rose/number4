import crypto as c
import datetime, sys, socket, os.path

IP = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]

# ERROR CHECKING
if not os.path.isfile(filename):
    print("Error: the file " + filename + " DNE")
    exit()
IPnums = IP.split('.')
if len(IPnums) != 4:
	print("Error: Incorrect IP format")
	exit()

# ENCRYPT
coded = bytes(c.DES(filename))

# "SOCKET PROGRAMMING"
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = (IP,port)
print("addr"); print(addr)
s.sendto(coded, addr)

print("receiving shit...")
msg = s.recvfrom(1024)
print("creating stamp")
stamp = datetime.datetime.now()
print(msg)
s.close()
