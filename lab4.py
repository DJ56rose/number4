import server as s, client as c

def lab4(port,IP=None,filename=None):
	if isinstance(IP,None) and isinstance(filename,None):
		print("going to create server")
	else:
		print("going to create client")
		# error checking
		try: fn = open(filename,"rb")
		except:
			print("Error: " + filename + " does not exist")
		# see if there are three periods in IP

