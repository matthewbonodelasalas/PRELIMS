""" Matthew Bono I. De las Alas
DATALOG Lab05
Feb. 24, 2020
I have neither received nor provided any help on this (lab) activity,
nor have I concealed any violation of the Honor Code.
"""

import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(10,10**9,100) #sets the range of the  values of n to be substituted to the function
plt.xlabel('log x') #label of x-axis
plt.ylabel('log y') #label of y-axis
plt.title("Plot of R-3.1\nDATALgo Feb. 19, 2020\ni5@2.40GHz,Win10") #Title of the Graph with Info of the hardware and operating system
plt.xscale('log') #sets the type of scale in the graph in the x-axis
plt.yscale('log')#sets the type of scale in the graph in the y-axis
y1 = 8*n #exponential function
y2 = 4*n*np.log(n) #logarithmic function
y3 =2*(n**2) #exponential function
y4 = n**3 #exponential function
plt.plot(n,y1,label = '8n') #plot of  the exponential function
plt.plot(n,y2,label ='4nlogn') #plot of  the logarithmic function
plt.plot(n,y3,label ='2n^2') #plot of  the exponential function
plt.plot(n,y4,label ='n^3') #plot of  the exponential function
plt.legend() # shows the label in every function that uses the plt.plot
plt.show()#Shows the graph

