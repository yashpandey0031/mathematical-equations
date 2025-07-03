#import numpy and matplotlib library
import numpy as np
import matplotlib.pyplot as plt
 
plt.axes(projection='polar')
 
a = 1
n = 200
 
rad = np.arange(0, 2 * np.pi, 0.001)
 
# plotting the rose
for i in rad:
    r = a * np.cos(n*i)
    plt.polar(i, r, 'g.')
 
# display the polar plot
plt.show()