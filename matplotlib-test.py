import numpy as np
import matplotlib.pyplot as plt

def f(x, y, z = 0):
    numerator = np.sin(x) + np.cos(y) + np.exp(z)
    denominator = x + y + z + 1
    return numerator / denominator

# Generate x and y values
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
z = np.linspace(-5, 5, 10)

# Generate a grid of points
X, Y = np.meshgrid(x, y)

# Compute the function values
F = f(X, Y)

# Create the plot
plt.subplot(2,1,1)
plt.plot(X, Y, F)
plt.title('f(x, y, z=0)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 3D plot
F1 = f(X, Y, z)
plt.subplot(212, projection='3d')
plt.plot_surface(X, Y, Z, F)
plt.title('f(x, y, z)')
plt.xlabel('x')
plt.ylabel('y')
plt.zlabel('z')
plt.show()
