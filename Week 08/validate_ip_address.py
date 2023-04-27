import socket

my_ip = "10.56.17.22"


def validate_ip(my_ip_address):
    try:
        socket.inet_aton(my_ip)
        return True
    except socket.error:
        print("You entered and invalid ip address")
        return False


print(validate_ip(my_ip))
