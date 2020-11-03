import sys
import socket
from datetime import datetime

# Define the target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4 
else:
	print("Invalid number of arguments")
	print("Expected syntax: python3 scanner.py <ip address>")

# Adding a banner
print('-' * 50)
print('Scanning target: ' + target)
print('Time started: ' + str(datetime.now()))
print('-' * 50)

try: 
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) # Returns an error indicator
		if result == 0:
			print(f'Port {port} is open')
		s.close()

except KeyboardInterrupt:
	print("Exiting program...")
	sys.exit()

except socket.gaierror:
	print("Hostname can not be resolved!")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()
