# for item in range(6, 20, 2):
#     print(item)
""" Generate a list of 50 ip addresses that are formed of the
    subnet prefix and subsequent numbers skipping the first 10 and the even numbers.
    For example  10.56.17.11, 10.56.17.12, 10.56.17.13...
"""
# for number in range(11, 50, 2):  # range(Start, End, Step)
    # print(number)

# subnet_prefix = "10.56.17"
subnet_prefix = input("Enter the subnet prefix: ")
ips_list = [subnet_prefix + "." + str(number) for number in range(11, 50, 2)]
print(ips_list)
