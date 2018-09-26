# #Time Series Analysis using ARIMA model

## Objective

- To collect network data for around 120 days and forecast an predict health of link for next 2 weeks by taking all network parameter in consideration.  
- To classify link health i.e. low risk, high risk etc. based on predicted values of packet drop.  
- To do the profiling of each KPI and forecast KPI values for next two weeks.  
- To put results on a platform/dashboard which can help in visualizing results by means of intuitive graphs.  

## Data
Tata Communications Limited has central Network Moniotring System (NMS) named WIRELESS ONE which is connected to all network devices & links and captures data by means of Simple Network Management Protocol trap (SNMP trap). There are two devices for which the data has been collectedat the granularity of 5 minutes.  
Network Parameters:  
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
1. [main.py](https://github.com/asmitapoddar/nowplaying-RS-Music-Recommendation-FM/blob/master/main.py): The main file from which the other scripts are called.

