import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Epitrochoid parameters
R = 100   # Radius of the fixed circle
r = 30    # Radius of the rolling circle
d = 60    # Distance from the center of the rolling circle to the drawing point

# Generate theta values
theta = np.linspace(0, 20 * np.pi, 5000)

#Epitrochoid equations
x = (R + r) * np.cos(theta) + d * np.cos(((R + r) / r) * theta)
y = (R + r) * np.sin(theta) - d * np.sin(((R + r) / r) * theta)

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')  # Black background
line, = ax.plot([], [], color='red', linewidth=2)  # Red line
ax.set_xlim(np.min(x) - 10, np.max(x) + 10)
ax.set_ylim(np.min(y) - 10, np.max(y) + 10)
ax.axis('off')  # Hide axes

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation function
def animate(i):
    line.set_data(x[:i * 5], y[:i * 5])  # Faster drawing by skipping points
    return line,

# Create animation (fewer frames, faster intervals)
ani = FuncAnimation(fig, animate, frames=len(x) // 5, init_func=init, interval=0.5, blit=True)

plt.show()
