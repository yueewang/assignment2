import numpy as np
import urllib
from datetime import datetime 
import matplotlib.pyplot as plt

url = 'http://waterdata.usgs.gov/nwis/dv?referred_module=sw&cb_00060=on&format=rdb&begin_date=1999-10-23&end_date=2009-10-23&site_no=08070000'

data = urllib.urlopen(url)

dates = []
discharge = []
mean= []
std  = []
 

for line in data.readlines()[27:]: 
    data_split    = line.split()
    date    = data_split[2]
    year    = int(date.split('-')[0])
    month   = int(date.split('-')[1])
    day     = int(date.split('-')[2])
#    date    = datetime.strptime(date_split, "%Y-%m-%d")
    discharge.append(float(data_split[3]))
    dates.append(datetime(year,month, day))
    
discharge = np.array(discharge) 
dates = np.array(dates)

month = np.array([d.month for d in dates])
day   = np.array([d.day for d in dates])
    
for idx in dates:
    cal_discharge = discharge [(month ==idx.month) & (day ==idx.day)]
    mean.append (np.mean (cal_discharge))
    std.append (np.std (cal_discharge))

mean = np.array(mean)
std  = np.array(mean)

upper = mean + std
lower = mean - std

fig = plt.figure()
plt.plot(dates, discharge, 'b', lw = 1.0,label = "Daily Time Series ")
plt.plot(dates, mean, 'k', lw= 2.0, label = "Annual Mean")
plt.plot(dates, upper,'k:', label = 'Std Upper Bound')
plt.plot(dates, lower,'k:', label = 'Std Lower Bound')
plt.fill_between(dates,upper,lower, facecolor='black',alpha=0.3)
plt.legend(loc = 'upper right')
plt.title('River Discharge for San Jacinto Rv nr Cleveland, TX')
plt.xlabel('Date')
plt.ylabel('Discharge (m$^{3}$/sec)')
plt.show()
plt.savefig('river_discharge.pdf')