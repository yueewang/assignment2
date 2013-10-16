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

discharge = discharge * 0.0283

month = np.array([d.month for d in dates])
day   = np.array([d.day for d in dates])
    
for idx in dates:
    cal_discharge = discharge [(month ==idx.month) & (day ==idx.day)]
    mean.append (np.mean (cal_discharge))
    std.append (np.std (cal_discharge))

mean = np.array(mean)
std  = np.array(std)

upper = mean + std
lower = mean - std

plot_year = np.array([d.year for d in dates])
idx       = np.where ((plot_year >= 2005)&(plot_year <= 2007))
plot_dates    = dates[idx]
plot_discharge = discharge [idx]
plot_mean      = mean[idx]
plot_upper     = plot_mean+ std[idx]
plot_lower   = plot_mean -  std[idx]


fig = plt.figure(figsize=(16,8))
ax = fig.add_axes([0.05,0.1,0.9,0.85])


plt.plot(plot_dates, plot_mean, 'r', lw= 1.5, label = "Annual Mean Discharge")
plt.plot(plot_dates, plot_upper,'k:', label = '+/- Std')
plt.plot(plot_dates, plot_lower,'k:')    
plt.plot(plot_dates, plot_discharge, 'g', lw = 1.0,label = "Daily Discharge ")
    
 
plt.fill_between(plot_dates,plot_upper,plot_lower, facecolor='pink',alpha=0.3)


plt.legend(bbox_to_anchor=(0, 0, 0.25, 1))
plt.title('Daily Stream Discharge for San Jacinto Rv nr Cleveland, TX')
plt.ylabel('Discharge (m$^{3}$/sec)')
plt.savefig('plot_graph_discharge.pdf')


