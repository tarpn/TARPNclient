import getpass
import sys
import telnetlib
import time
from time import gmtime, strftime

HOST = "localhost"  
PORT = "8010"
#user = raw_input("Enter your remote account: ")   #use if you want to prompt for a password
#password = getpass.getpass()
username = "kn4orb"
password = "p"

tn = telnetlib.Telnet(HOST,PORT)

print tn.read_until(":")
tn.write(username + "\r\n")

print tn.read_until(":")
tn.write(password + "\r\n")
print("***** Waiting 3 Seconds for the node *****\n")
time.sleep(3)
print tn.read_very_eager()

#Get Commands via "I"
tn.write("I\r\n")
print("Wrote 'I'")
time.sleep(1) #we must wait after every command for the node to send back the output before reading it
print tn.read_very_eager()

#Disconnect
tn.write("Bye\r\n")
tn.write("^]")
tn.write("exit\r\n")

print tn.read_all()
