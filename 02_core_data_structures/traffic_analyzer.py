traffic = ['10.1.1.1', '10.1.1.2', '10.1.1.1', '10.1.1.3']

lst = list(dict.fromkeys(traffic))
print(len(lst))

coords = (40.7128, -74.0060)  
coords[0] = 41.856