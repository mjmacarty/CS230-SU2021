import pandas_datareader as pdr
import matplotlib.pyplot as plt


data = pdr.get_data_morningstar('GOOG')['price']

print(len(data))
print(type(data))

print(data)
