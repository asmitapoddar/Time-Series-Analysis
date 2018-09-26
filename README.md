# Time Series Analysis of Wireless Network Parameters using ARIMA model

## Objective

- To collect network data for around 120 days and forecast an predict health of link for next 2 weeks by taking all network parameter in consideration.  
- To classify link health i.e. low risk, high risk etc. based on predicted values of packet drop.  
- To do the profiling of each KPI and forecast KPI values for next two weeks.  
- To put results on a platform/dashboard which can help in visualizing results by means of intuitive graphs.  

## Data
Tata Communications Limited has central Network Moniotring System (NMS) named WIRELESS ONE which is connected to all network devices & links and captures data by means of Simple Network Management Protocol trap (SNMP trap). There are two devices for which the data has been collectedat the granularity of 5 minutes.  
#### Network Parameters:  
- Packet Drop
- Latency
- Uplink Utilization %
- Downlink Utilization %
- Uplink Utilization
- Downlink Utilization
- Availability
- IDU UL Issue
- Frequency
- Uptime

## Environment
Python 3.0

## Dependencies 
- numpy
- pandas
- matplotlib
- tatsmodels
- warnings
- itertools
- datetime

## Code
The following scripts, stored in this repository, have been developed for implementing Time Series Analysis using ARIMA model to  fforecast an predict health of link:  
1. [Latency.py](https://github.com/asmitapoddar/Time-Series-Analysis/blob/master/Latency.py): Perform Time Series Analysis on the parameter 'Latency' to predict its value in the next 14 days using ARIMA model.
2. [Service_Uptime.py](https://github.com/asmitapoddar/Time-Series-Analysis/blob/master/Service_Uptime.py): Perform Time Series Analysis on the parameter 'Service Uptime' to predict its value in the next 14 days using ARIMA model.
3. [Stationary_testing.py](https://github.com/asmitapoddar/Time-Series-Analysis/blob/master/Stationary_testing.py): Check if the time series is stationary through Summary statistics, Augmented Dickey-Fuller Test, ACF and PACF (Autocorrelation and Partial Auto Correlation) and Visualization of results.
4. [concat.py](https://github.com/asmitapoddar/Time-Series-Analysis/blob/master/concat.py): Concatenate mulitple files into a single file.
5. [convert to csv linux.sh](https://github.com/asmitapoddar/Time-Series-Analysis/blob/master/convert%20to%20csv%20linux.sh): bash command to convert a .xlsx file to .csv format.
6. [loop_convert.sh](https://github.com/asmitapoddar/Time-Series-Analysis/blob/master/loop_convert.sh): Convert all .xlsx files in the directory to .csv format.

