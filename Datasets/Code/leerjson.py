import json

drivers = {}

with open('C:/Users/aagui/Github/PI01_DATA03/Datasets/drivers.json', encoding ='utf-8') as f:
    for linea in f:
        data = json.loads(linea)     
        drivers[data['driverId']] = data

print(drivers)
