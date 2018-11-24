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

tn.write("ZEFO:1&&3000:;\r\n")
tn.write("ZQRI:ETPA,::VLAN621:IPV4:;\r\n")
tn.write("ZQKB:ETPA;\r\n")

print tn.read_until("<QK_>")