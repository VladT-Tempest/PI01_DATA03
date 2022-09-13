import pandas as pd
FILE = 'C:/Users/aagui/Github/PI01_DATA03/Datasets/drivers.json'

df = pd.read_json(FILE)

data_dict = df.to_dict()

print(data_dict)