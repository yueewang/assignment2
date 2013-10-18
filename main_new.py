import numpy as np
import read_function_1 as read_data
import plot_function_new as plot

start_date  = raw_input('Enter start data (XXXX-XX-XX): ')
end_date    = raw_input('Enter end data (XXXX-XX-XX): ')
site_no     = raw_input('Enter site number: ')

data_1     = read_data.read_function_1(start_date,end_date,site_no)

date = data_1[0]
discharge = data_1[1]


mean  = []
std   = [] 


month = np.array([date[d].month for d in range(date.size)])
day   = np.array([date[d].day for d in range(date.size)])
    
for idx in date:
    cal_discharge = discharge [(month ==idx.month) & (day ==idx.day)]
    mean.append (np.mean (cal_discharge))
    std.append (np.std (cal_discharge))

mean = np.array(mean)
std  = np.array(std)

upper = mean + std
lower = mean - std

plot_year = np.array([d.year for d in date])
idx       = np.where ((plot_year >= 2005) & (plot_year <= 2007))
plot_dates    = date[idx]
plot_discharge = discharge [idx]
plot_mean      = mean[idx]
plot_upper     = plot_mean+ std[idx]
plot_lower   = plot_mean  - std[idx]

plot.plot_function_1(plot_dates,plot_discharge,plot_mean,plot_upper,plot_lower,site_no)
