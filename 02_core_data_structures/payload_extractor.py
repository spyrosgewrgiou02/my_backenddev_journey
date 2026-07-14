raw_log = "ERROR|2026-07-14|192.168.1.50|Failed login attempt"

date = None
ip = None

for item in raw_log.split("|"):
    if item.count(".") == 3 and all(p.isdigit() for p in item.split(".")):
        ip = item
        print(ip)  # print IP when found
    elif item.count("-") == 2 and all(x.isdigit() for x in item.split("-")):
        date = item

if date and ip:
    print(f"{ip} - {date}")