import matplotlib.pyplot as plt
import numpy as np


# Define x values from 0 to pi
x = np.arange(0, np.pi, 0.1)

# Calculate sin(x) and cos(x)
y=np.sin(x)
z=np.cos(x)


# Plotting
plt.plot(x,y, color='blue', linestyle='solid',linewidth=2, marker='o', markersize=5 )
plt.plot(x,z, color='orange', linestyle='solid',linewidth=2, marker='o', markersize=5 )

plt.xlabel('x values from zero to pie')
plt.ylabel("sin(x) and cos(x)")
plt.title("plot of sin(x) and cos(x) from zero to pie")
plt.legend(["sin(x)","cos(x)"])
plt.show()
