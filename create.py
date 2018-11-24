import getpass
import sys
import telnetlib

IP = "10.128.9.4"
user = "SALMAN"
password = "NOKIA778"

tn = telnetlib.Telnet(IP)

tn.read_until("ENTER USERNAME < ")
tn.write(user + "\r\n")
if password:
    tn.read_until("ENTER PASSWORD < ")
    tn.write(password + "\n")

tn.write("\r\n")
ipr = str
with open ('generate.txt', 'r') as f:
    for ipr in f:
        ipr = ipr.strip()
        tn.write(ipr + "\r\n")
        tn.write("\r\n")

tn.write("\r\n")
tn.write("ZUSI:COMP;\r\n")
print tn.read_until("<US_>")