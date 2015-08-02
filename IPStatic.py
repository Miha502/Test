import platform
import socket
import getpass
hostname = socket.gethostname()
print("Domain and Hostname",socket.getfqdn())
print("User Connected",getpass.getuser())
print("OS Release: ",platform.system(),platform.release())
print("Host IP is:",socket.gethostbyname(socket.gethostname))
