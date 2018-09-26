import pandas as pd
import numpy as np
import datetime
import warnings
import itertools
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Warning = 70, Critical = 90
data = pd.read_csv('Final Model/10.193.123.5/Uptime/Uptime.csv')
data.head()
df = data[['Time','Avg. Value']]

#Check for NA values
df['Avg. Value'].isnull().sum()   #0
df.rename(columns={'Avg. Value': 'Current_value'}, inplace=True)

df['Time'] = pd.to_datetime(df['Time'], format = '%d/%m/%y %H:%M') #Converting 'str' to 'timestamp'

dts=df.sort_values(by='Time') #sort data frame in chronological order
dts.rename(columns={'Avg. Value': 'Current_value'}, inplace=True)

dts.set_index('Time',inplace = True) #Set 'Time' column as index

dts.plot(figsize=(15, 6))
plt.show()
#dts.index
#converted = dts.asfreq('5Min', method = 'pad')

#Seasonal and Trend Decomposition---------------------

dailyfreq =int((24*60)/5*1)
weeklyfreq=int((24*60)/5*7)

from pylab import rcParams
rcParams['figure.figsize'] = 11, 9

decomposition_d = sm.tsa.seasonal_decompose(dts, model='additive', freq=dailyfreq)
fig = decomposition_d.plot()
plt.show()

decomposition_w = sm.tsa.seasonal_decompose(dts, model='additive', freq=weeklyfreq)
fig = decomposition_w.plot()
plt.show()

'''
dts.index.head()
<class 'pandas.tseries.index.DatetimeIndex'>
dts.index.freq: None

dts.resample('T').ffill().reindex(pd.date_range(dts.index[0],dts.index[-1],freq='5T'))
dts.index.freq: <5 * Minutes>
'''

#ARIMA model-------------------------------------------

#statsmodels
from statsmodels.tsa.arima_model import ARIMA
p,d,q = 4,1,1  #p:AR, q:MA d(integ): No. of times to difference the data
dts.rename(columns={'Current Value': 'Current_value'}, inplace=True)
dts.Current_value = dts.Current_value.astype(float)
model = ARIMA(dts.Current_value, order=(p,d,q))
model_fit = model.fit(disp=0)
print(model_fit.summary())
# plot residual errors
from pandas import DataFrame
residuals = DataFrame(model_fit.resid)
residuals.plot()
plt.show()
residuals.plot(kind='kde')
plt.show()
print(residuals.describe())
'''
                 0
count  6911.000000
mean     -0.004567  #very little bias in the prediction (centred on 0)
std       1.345207
min     -43.546404
25%      -0.221028
50%      -0.055496
75%       0.148704
max      21.130473
'''
'''
model_fit.plot_predict(dts.index[len(dts)-10],dts.index[len(dts)-1]) #plot forecasts
plt.show()
preds = model_fit.predict(len(dts)-10,len(dts)+10) #Dataframe format
'''
#pyflux
import pyflux as pf
p,d,q = 4,0,1
model = pf.ARIMA(data=dts, ar=p, integ=d, ma=q)
x = model.fit()
model.plot_fit(figsize=(15,4))
'''
mu, Y = model._model(model.latent_variables.get_z_values())
fitted_values = pd.Series(model.link(mu),index=dts.ix[-len(mu):].index)
dts.subtract(fitted_values).plot()
'''

#MLE: Maximum Likelihood Estimation
model = pf.ARIMA(data=dts,ar=2,ma=2,integ=0,target='Current_value') #family is pf.Normal()[By default]
x = model.fit("MLE")
x.summary()
model.plot_z(figsize=(15, 7))    # Latency Variable plot
model.plot_z(indices=range(1,9)) # Latency Variable plot
model.plot_fit(figsize=(15,5)) #ARIMA model fit

model.plot_predict(h=30,figsize=(15,5)) # plots predictions for next 30 time steps, 95% confidence interval
model.plot_predict_is(h=30) # plots rolling in-sample prediction for past 5 time steps :Idea of performance #model.plot_predict(h=20,past_values=20,figsize=(15,5))
predictions = model.predict(h=5, intervals=True) # outputs dataframe of predictions

'''
samples = model.sample(nsims=10) # returns 10 samples from the data
ppc_pvalue = model.ppc(T=np.mean) # p-value for mean posterior predictive test
model.plot_sample(nsims=10) # draws samples from the model
model.plot_ppc(T=np.mean) # plots histogram of posterior predictive check for mean
'''







