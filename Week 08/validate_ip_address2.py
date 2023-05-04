import ipaddress

my_ip = "10.56.17.33"


# print(type(ipaddress.ip_address(my_ip)))
def validate_ip(my_ip_address):
    try:
        ipaddress.IPv4Address(my_ip_address)  # validates IPv4 only
        return True
    except ipaddress.AddressValueError:
        print("You entered and invalid ip address")
        return False


print(validate_ip(my_ip))

