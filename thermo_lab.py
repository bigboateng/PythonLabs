__author__ = 'Boateng'

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def plot():
    t = np.linspace(300,5000)
    y_c = 1 - 300/t
    y_s = (np.log(4)*(t - 300))/(1.5*(t - 300) + t*np.log(4))
    rat = y_s/y_c
    carnot, = plt.plot(t,y_c, label="Carnot", linewidth=2.0)
    stirling,  = plt.plot(t,y_s, label="Stirling",linewidth=2.0)
    ratio, = plt.plot(t, rat, label="Ratio of Stirling/Carnot",linewidth=2.0)
    fontP = FontProperties()
    plt.xlabel("Temperature (Th) / Kelvin")
    plt.ylabel("Efficiency")
    plt.legend(handles=[carnot, stirling, ratio],prop = fontP,title="Graph of efficiency as function of Th", loc="bottom center")
    fontP.set_size('small')
    plt.savefig('graph.pdf')
    plt.show()

if __name__ == '__main__':
    plot()