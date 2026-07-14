ips = ["192.168.1.1", "10.0.0.5", "192.168.1.100", "HALT", "172.16.0.1"]

for i in ips:
    if i == "10.0.0.5":
        continue
    if i == "HALT":
        print("Found HALT")
        break
    print(F"Scanning Target: [{i}]")  
