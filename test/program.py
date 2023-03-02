import ipaddress
import socket


def basic_ip4_sample():
    ip_addr1 = ipaddress.IPv4Address('192.168.1.1')
    print(ip_addr1)
    print(type(ip_addr1))

    ip_addr2 = ipaddress.IPv4Address('200.200.200.1')

    # Print details about the ip address
    print('Is 192.168.1.1 private?', ip_addr1.is_private)
    print('Is 192.168.1.1 global?', ip_addr1.is_global)

    print('Is 200.200.200.1 private?', ip_addr2.is_private)
    print('Is 200.200.200.1 global?', ip_addr2.is_global)

    # Can extract each octect using the packed attribute and accessing
    # by index position
    print('The first octet in', ip_addr1, 'is', ip_addr1.packed[0])
    print('The second octet in', ip_addr1, 'is', ip_addr1.packed[1])
    print('The third octet in', ip_addr1, 'is', ip_addr1.packed[2])
    print('The fourth octet in', ip_addr1, 'is', ip_addr1.packed[3])

    loopback = ipaddress.IPv4Address('127.0.0.1')
    print('Is', loopback, 'a loopback address?', loopback.is_loopback)


def ip_network_sample():
    nwk_addr1 = ipaddress.IPv4Network('192.0.2.0/24')
    print('The number of address in', nwk_addr1, 'is', nwk_addr1.num_addresses)

    nwk_addr2 = ipaddress.IPv4Network('192.168.0.0/255.255.255.0')
    print('The number of address in', nwk_addr2, 'is', nwk_addr2.num_addresses)

    print('The netmask for', nwk_addr1, 'is', nwk_addr1.netmask)
    print('The hostmask for', nwk_addr1, 'is', nwk_addr1.hostmask)

    # Can also print out all the host address in a network
    # for ip in nwk_addr1.hosts():
    #     print(ip)

    # Can put all host addresses in a list
    ip_net_lists = list(nwk_addr1.hosts())

    # Can divide a network into more subnets
    for subnet in nwk_addr1.subnets(new_prefix=27):
        print(subnet)
        print('The number of addresses in', subnet, 'is', subnet.num_addresses)


def basic_ip6_sample():
    ip6_addr = ipaddress.IPv6Address('2001:acad:a:1::1')

    print(ip6_addr.is_global)
    print(ip6_addr.is_link_local)

    ip6_net = ipaddress.IPv6Network('2001:acad:a:1::/64')
    print(ip6_net.hostmask)
    print(ip6_net.prefixlen)
    print(ip6_net.num_addresses)


def sock_sample():
    # Create a socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Can control timeout duration (in this case 5 seconds)
    sock.settimeout(5)

    ip_and_port = ('192.168.0.1', 80)
    result = sock.connect_ex(ip_and_port)

    print(result)
    # Close connection to socket once done
    sock.close()

    # Should create a new socket for every new ip/port combo
    # Can automatically close the socket by using with
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex(('172.217.24.35', 443))

        print(result)


def other_socket_samples():
    lookup = socket.getfqdn("8.8.8.8")
    lookup2 = socket.gethostbyname('dns.google.com')

    print(lookup)
    print(lookup2)

    lookup = socket.getfqdn("172.217.24.35")
    print('The fully qualified domain name for 172.217.24.35 is:', lookup)

    lookup = socket.getfqdn("172.27.59.160")
    print(lookup)


def basic_scanner():
    # Create a new network address
    nwk_addr1 = ipaddress.IPv4Network('192.168.0.0/30')

    # Loop over each host address
    for ip in nwk_addr1.hosts():
        # Try to connect to a specific port on that ip
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Set a timeout for the socket
            sock.settimeout(4)

            ip_as_str = str(ip)
            print(ip_as_str)
            # Need to give the IP address as a str to connect_ex
            result = sock.connect_ex((ip_as_str, 80))
            print('The code returned for', ip, 'on port 80 is:', result)


basic_ip4_sample()
ip_network_sample()
basic_ip6_sample()
sock_sample()
other_socket_samples()
basic_scanner()
