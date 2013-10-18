import matplotlib.pyplot as plt

def plot_function_1(plot_dates,plot_discharge,plot_mean,plot_upper,plot_lower,site_no):


    fig = plt.figure(figsize=(16,8))
    ax = fig.add_axes([0.05,0.1,0.9,0.85])


    plt.plot(plot_dates, plot_mean, 'r', lw= 1.5, label = "Annual Mean Discharge")
    plt.plot(plot_dates, plot_upper,'k:', label = '+/- Std')
    plt.plot(plot_dates, plot_lower,'k:')    
    plt.plot(plot_dates, plot_discharge, 'g', lw = 1.0,label = "Daily Discharge ")
    
 
    plt.fill_between(plot_dates,plot_upper,plot_lower, facecolor='pink',alpha=0.3)


    plt.legend(bbox_to_anchor=(0, 0, 0.25, 1))
    plt.title('Daily Stream Discharge for station no.'+ site_no)
    plt.ylabel('Discharge (m$^{3}$/sec)')
    plt.savefig('plot_graph_discharge_new.pdf')
    
    return plt.show()