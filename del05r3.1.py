""" Matthew Bono I. De las Alas
DATALOG Lab05
Feb. 19, 2020
I have neither received nor provided any help on this (lab) activity,
nor have I concealed any violation of the Honor Code.
"""

import matplotlib.pyplot as plt
import numpy as np
n = np.arange(1,10**9,10000)
plt.xlabel('log x')
plt.ylabel('log y')
plt.title("Plot of R-3.1\nDATALgo Feb. 19, 2020\ni5@2.40GHz,Win10")
plt.xscale('log')
plt.yscale('log')
y1 = 8*n
y2 =  4*n*np.log(n)
y3 =2*n**2
y4 = n**3
y5 = 2**n
plt.plot(n,y1,label = '8n')
plt.plot(n,y2,label ='4n log n')
plt.plot(n,y3,label ='2n^2')
plt.plot(n,y4,label ='n^3')
plt.plot(n,y5,label = ' 2^n')
plt.legend()
plt.show()

