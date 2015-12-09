
from pyneuroml import pynml


import matplotlib.pyplot as plt


data, indices = pynml.reload_standard_dat_file('KAHP.states.dat')
x = []
y = []
for i in indices:
    x.append(data['t'])
    y.append(data[i])
    
totals = []
for j in range(len(data['t'])):
    tot = 0
    for i in indices:
        tot+=data[i][j]
    totals.append(tot)
    
labels = indices
x.append(data['t'])
y.append(totals)
labels.append('total')

pynml.generate_plot(x,
                    y, 
                    "States", 
                    xaxis = "Time (ms)", 
                    yaxis = "State occupancy",
                    labels = labels,
                    show_plot_already=False,
                    save_figure_to = None)
                    

plt.show()