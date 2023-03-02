##__author name__ = "Student's name"
##__email__ = "students.email@studytafensw.edu.au"
##__copyright__ = "Copyright Red Opal Innovations"
##__license__ = "Proprietary"
##__last update date__ = 16/11/2020
##__version__ = "1.0.1"
##__status__ = "Development"

##This apps executes port scan based on network and port input by user.
##Exclude 10 Top IPs as they will be reserved for printers
##Exclude EVEN IPs from SCAN

##Import packages
import socket
import subprocess
import sys
import os
from os import strerror
import time
from datetime import datetime
import win32evtlogutil
import win32evtlog

##validate network address
def ipinput(network): 
    networkaddress=network+"."+"1"
    try:
      socket.inet_aton(networkaddress)              ##Valid IP address - print("Valid IP")
      return True
    except socket.error:
      print("You entered Invalid network address")  ##Invalid IP address
      return False
      
##define function to write to the syslog
def writelog(mylist, eventtype):
    IP_EVT_APP_NAME = " CheckIPPort - IP Scan Application"
    IP_EVT_ID = 7040                                ##According to ???
    IP_EVT_CATEG = 9876                             ##According to ???
    IP_EVT_TYPE=win32evtlog.EVENTLOG_WARNING_TYPE #WARNING=2
    IP_EVT_ERR=win32evtlog.EVENTLOG_ERROR_TYPE #ERROR=1
    IP_EVT_STRS = [status for status in mylist]
    IP_EVT_DATA = b"Scan IP Address Event Data"
    win32evtlogutil.ReportEvent(IP_EVT_APP_NAME,\
                                IP_EVT_ID,\
                                eventCategory=IP_EVT_CATEG,\
                                eventType=eventtype,\
                                strings=IP_EVT_STRS,\
                                data=IP_EVT_DATA)

##Ask user to input network to scan    
network=input("Please enter the first three octects seperate by . \"dot\": ")
validip = ipinput(network)
while not validip:
                
    network=input("Please enter the first three octects seperate by . \"dot\": ")
    validip = ipinput(network)
    
iplist= [network+"."+str(ip) for ip in range (11, 50, 2)]

##define scanport function
def portscan(ip, port):
    dateTimeObj = datetime.now()
    timestamp = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    try:
        fo = open("ip_port_log.txt", "a+t")
        socket.setdefaulttimeout(0.1)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result= sock.connect_ex((ip, port))
        if result == 0:
            print("IP: ", ip,":", port, "Open", "Time Stamp", timestamp)
            #fline="IP: " +ip+":"+str( port)+ " Open" + "\n"
            data1="IP: " +ip+" : "+str( port)+ " Open " +"Time "+timestamp
            fo.write(data1+"\n")
            listipport.append(data1)
        else:
            print("IP: ", ip,":", port, " Closed/Filtered or host is offline")
            data1="IP: "+ ip+" : "+  str(port)+ " Closed/Filtered or host is offline"
            listipport.append(data1)
        sock.close()
        fo.close()      
    except KeyboardInterrupt:
        print ("You press Ctrl+c")
        sys.exit()
    except socket.error:
        print("Cant connecto to IP: ", ip)
        sys.exit()
    except IOError as e:
        print("I/O error occurred:", strerr(e.errno))
    subprocess.call('clear', shell=True)

##Read port from the ports.txt file
portlist=[]
if os.path.isfile("ports.txt"):
    f=open("ports.txt", "r")
    for port in f:
        if port in portlist:
            print("This port is already in the list")
        else:
            portlist.append(int(port))
    
    f.close()    
else:
    print("ports.txt does not exist")
    exit(1)
    
##start to scan ports

listipport=[]
for ip in iplist:
    for port in portlist:
        portscan(ip,port)
print(listipport)
##write the system log
writelog(listipport, 2)
writelog(listipport, 1)
