
import numpy as np
import matplotlib.pyplot as plt
from math import pi



x = np.arange(0,2*pi,0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y, 'r',x,z,'b')
plt.xlabel('x values from 0 to 2Pi')
plt.ylabel('y values from -1 to 1')
plt.title('One Period of Sine and Cosine Plot ')
plt.legend(['sin(x)', 'cos(x)'])
plt.axhline(y=0)
plt.show()


