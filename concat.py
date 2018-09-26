import pandas as pd

data1 = pd.read_csv('Wirelessone27/10.193.123.5/Network_Performance_Latency.csv')
data2 = pd.read_csv('WirelessOne27-23/10.193.123.5/Network_Performance_Latency.csv')
data3 = pd.read_csv('Equipment_DATA_POC/10.193.123.5/Latency.csv')
frames = [data1, data2, data3]
data = pd.concat(frames)
