import server as s, client as c

def lab4(port,IP=None,filename=None):
	if IP == None and filename == None:
		print("going to create server")
	else:
		print("going to create client")
		### error checking ###
		# file exists?
		try: fn = open(filename,"rb")
		except:
			print("Error: " + filename + " does not exist")
		# 3 periods in IP?
		IPnums= IP.split('.')
		if len(IPnums) != 4:
			print("Error: Incorrect IP format")
			return None

		# set up client
		
port = 2
IP = "192.12.13.127"
fn = "file.txt"
print("GOING INTO LAB4 FILE")
lab4(port,IP,fn)

