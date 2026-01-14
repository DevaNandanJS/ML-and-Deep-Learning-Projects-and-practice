import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0, 10, 100)
y= np.sin(x)
z= np.cos(x)

#plotting the data
#sin()
"""
plt.plot(x,y)
plt.show()
"""
#cos()
plt.plot(x,z)
plt.xlabel("angle")
plt.ylabel("cos(x)")
plt.title("cos wave")
plt.show()



