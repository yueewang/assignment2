import numpy as np
import urllib
from datetime import datetime 

start_date = '1999-10-23'
end_date   = '2009-10-23'
site_no    = '08070000'
    

def read_data_function(start_date,end_date,site_no):
    
    url = 'http://waterdata.usgs.gov/nwis/dv?referred_module=sw&cb_00060=on&\
    format=rdb&begin_date='+start_date+'&end_date='+end_date+'&site_no='+site_no+''
    
    
    data = urllib.urlopen(url)

    dates = []
    discharge = []

    for line in data.readlines()[27:]: 
        data_split    = line.split()
        dates    = data_split[2]
        year    = int(dates.split('-')[0])
        month   = int(dates.split('-')[1])
        day     = int(dates.split('-')[2])
#    date    = datetime.strptime(date_split, "%Y-%m-%d")
        discharge.append(float(data_split[3]))
        dates.append(datetime(year,month, day))
   
    discharge = np.array(discharge)
    dates = np.array(dates)

    discharge = discharge * 0.0283
    
data_1 = read_data_function(start_date,end_date,site_no)

mean  = []
std   = [] 
dates = data_1[1]
discharge = data_1[0]

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
idx       = np.where (plot_year >= 2005 & plot_year >= 2007)
plot_dates    = dates[idx]
plot_discharge = discharge [idx]
plot_mean      = mean[idx]
plot_upper     = plot_mean+ std[idx]
plot_lower   = plot_mean+ std[idx]

plot_function(plot_year,plot_dates,plot_discharge,plot_mean,plot_upper,plot_lower)