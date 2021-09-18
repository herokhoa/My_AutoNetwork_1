import time
#from telnetlib import Telnet
import telnetlib

# Get Username and Password
#user = input("Enter your username: ")
#password = getpass.getpass()
user = "epnm"
password = "epnm@890!"

#  Open file with list of switches
f = open ("csg_list")

#  Telnet to each switch and cofigure it
for line in f:
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        print("Saving config csg: " + line)
        print("Saving ........")
        tn.write(b"copy running-config startup-config\n")
        tn.write(b"\n")
        time.sleep(10)
        tn.write(b"\n")
        tn.write(b"exit\n")
        readoutput = tn.read_all()
        print(tn.read_all().decode('ascii'))
        tn.close()
