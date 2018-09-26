import pandas as pd
import numpy as np
import statsmodels
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

data = pd.read_csv('Network_Performance_Latency.csv')
data.head()
df = data[['Time','Current Value']]

dts=df.iloc[::-1] #reversing the data frame (now chronological)

dts['Time'] = pd.to_datetime(dts['Time'], format = '%d/%m/%y %H:%M') #Converting 'str' to 'timestamp'

dts.set_index('Time',inplace = True)

#Visualization
dts.plot(figsize=(15, 6))
plt.show()

#Summary statistics
dts.hist()
plt.show()

#Augmented Dickey-Fuller Test
dts.rename(columns={'Current Value': 'Current_value'}, inplace=True)
dts.Current_value = dts.Current_value.astype(float)
res = adfuller(dts.Current_value)  #df.a is a pandas Series
res

#ACF and PACF (Autocorrelation and Partial Auto Correlation)
statsmodels.graphics.tsaplots.plot_acf(dts.Current_value)
plt.show()

statsmodels.graphics.tsaplots.plot_pacf(dts.Current_value, lags=50)
plt.show()


'''
Latency

(-2.7819942122797645, 0.020892153239807803, 28, 6882, {'10%': -2.5669935989779469, '1%': -3.4313005580926594, '5%': -2.8619600691766256}, 23325.923239234042)
ADF Statistic: -2.7819942122797645
p-value: 0.020892153239807803 (<5% - reject NULL(non-stationary) hypothesis : stationary, here alpha(significance level) is 5%)
No. of lags used: 28
No. of observations used to calculate critical values: 6882
Critical Values:
	5%: -2.8619600691766256
	1%: -3.4313005580926594
	10%: -2.5669935989779469
'''

