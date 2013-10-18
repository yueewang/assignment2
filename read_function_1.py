import numpy as np
import urllib
from datetime import datetime


def read_function_1(start_date,end_date,site_no):
    
    url = []
    
    url = 'http://waterdata.usgs.gov/nwis/dv?referred_module=sw&cb_00060=on&format=rdb&begin_date='+start_date+'&end_date='+end_date+'&site_no='+site_no
    
    data = urllib.urlopen(url)

    dates = []
    discharge = []

    for line in data.readlines()[27:]: 
        data_split    = line.split()
        date         = data_split[2]
        year    = int(date.split('-')[0])
        month   = int(date.split('-')[1])
        day     = int(date.split('-')[2])
#    date    = datetime.strptime(date_split, "%Y-%m-%d")
        discharge.append(float(data_split[3]))
        
        dates.append(datetime(year,month, day))
       
   
    discharge = np.array(discharge)
    dates = np.array(dates)

    discharge = discharge * 0.0283
    
    return dates, discharge
    

    
