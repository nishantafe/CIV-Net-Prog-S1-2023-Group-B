players_1 = ["David", "George", "Steve"]
players_2 = ["Sara", "Rita", "Cathy"]

for player_1 in players_1:
    for player_2 in players_2:
        # print(player_1, "VS", player_2)
        pass

# All IPs against all ports
ips = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]  # You can use range() to generate this
ports = ["80", "445", "110"]
for ip in ips:
    print("Start of a new iteration of the FIRST loop")
    for port in ports:
        print("\tStart of a new iteration of the SECOND loop")

        # scan(ip, port)
        print("\t" + ip, ":", port + "\n")
