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