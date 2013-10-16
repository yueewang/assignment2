import numpy as np
import urllib
from datetime import datetime 
import read_data_function as read_data
import plot_function as plot

start_date = '1999-10-23'
end_date   = '2009-10-23'
site_no    = '08070000'

data_1     = read_data.read_data_function(start_date,end_date,site_no)

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

#plot.plot_function(plot_year,plot_dates,plot_discharge,plot_mean,plot_upper,plot_lower)

 