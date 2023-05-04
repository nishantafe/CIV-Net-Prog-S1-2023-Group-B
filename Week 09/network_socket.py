import socket
import datetime

timestamp = datetime.datetime.now().strftime(f"%d-%b-%Y (%H:%M:%S.%f)")

ip = "10.56.17.7"
port = 135

socket.setdefaulttimeout(0.1)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((ip, port))
if result == 0:
    print(f"{ip}:{port:<3d} Open | Time: {timestamp}")

else:
    print(f"{ip}:{port:<3d} Closed/Filtered or host is offline | Time: {timestamp}")
sock.close()

# TODO Generate a range of IP addresses (using suffix by a user + an octet between 0 and 255)
# TODO Retrieve port number as a list from lines of a txt file ports.txt
# TODO Scan each IP with each port and print the message (open or closed)
# TODO Write only the message of Open or Closed to a file ip_port_log.txt
