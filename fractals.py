import numpy as np
import matplotlib.pyplot as plt

# Define image size and Mandelbrot parameters
img_size = 1000
max_iter = 100

# Define complex plane boundaries
x = np.linspace(-2.0, 1.0, img_size)
y = np.linspace(-1.5, 1.5, img_size)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y  # Complex grid

Z = np.zeros_like(C)
divergence_time = np.zeros(C.shape, dtype=int)

# Mandelbrot iteration
for i in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask] ** 2 + C[mask]
    divergence_time[mask & (np.abs(Z) > 2)] = i

# Plot using matplotlib
plt.figure(figsize=(10, 10))
plt.imshow(divergence_time, cmap='magma', extent=(-2, 1, -1.5, 1.5))
plt.colorbar(label='Iteration Count')
plt.title('Mandelbrot Set (Vectorized)')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.show()
