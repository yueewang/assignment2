import matplotlib.pyplot as plt

def plot_function(dates,plot_discharge,plot_mean,plot_upper,plot_lower):

    fig = plt.figure()
    plt.plot(dates, plot_mean, 'r', lw= 1.5, label = "Annual Mean Discharge")
    plt.plot(dates, plot_upper,'k:', label = '+ Std')
    plt.plot(dates, plot_lower,'k:', label = '- Std')    
    plt.plot(dates, plot_discharge, 'b', lw = 1.0,label = "Daily Discharge ")
    
 
    #plt.fill_between(plot_dates,plot_upper,plot_lower, facecolor='black',alpha=0.3)

    plt.legend(loc = 'upper right')
    plt.title('Daily Stream Discharge for San Jacinto Rv nr Cleveland, TX')
    plt.ylabel('Discharge (m$^{3}$/sec)')
    #plt.savefig('river_discharge.pdf')