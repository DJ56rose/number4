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
s.sendto(coded, addr)
# receive
msg, addr = s.recvfrom(1024)
msg = c.DES(msg,"decrypt")
stamp = str(datetime.datetime.now())
# get IP addr
hostName = socket.gethostname()
hostIP = str(socket.gethostbyname(hostName))
IP_Server = addr[0]
# output
cutoff = -1
for i in range(0,len(msg)):
    if msg[i] == 58 and msg[i+1] == 32:
        cutoff = i+1
    msg[i] = chr(msg[i])
msg = msg[cutoff-1:]
msg = ''.join(msg)
print(stamp+msg+"\n Client IP: "+hostIP+", Server IP: "+IP_Server)
# close
s.close()
