import ipaddress

my_ip = "10.56.17.33"


# print(type(ipaddress.ip_address(my_ip)))
def validate_ip(my_ip_address):
    try:
        # ipaddress.ip_address creates a new IP address object if the string provided is a valid IP address
        ipaddress.ip_address(my_ip_address)
        return True
    except ValueError:
        print("You entered and invalid ip address")
        return False


print(validate_ip(my_ip))
