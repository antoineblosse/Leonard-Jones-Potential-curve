import matplotlib.pyplot as plt                                                 
import numpy as np

x = np.arange(3.0, 8.0, 0.01)          ## [3.0-8.0] is range for x-axis; [0.0-2.99] not part of range, since vertical asymptote at point 0.0
                                       ## 0.01 is the interval between each succesive point drawn on the curve
y = 4*0.997*((3.4/x)**12-(3.4/x)**6)   ##Leonard-Jones potential formula

plt.plot(x, y)                         ## Plot function

## Label the graph
plt.title('Modeling interactions between two Argon atoms')
plt.xlabel('r')
plt.ylabel('E')

plt.show()                             ## Show the graph
