import numpy as np
import matplotlib.pyplot as plt

def x2(x):
    return x**2


x = np.linspace(-2,2,101)
y = x2(x)

plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()