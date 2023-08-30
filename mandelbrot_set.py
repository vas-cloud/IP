import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(width, height, xmin, xmax, ymin, ymax, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.zeros((height, width))

    for i in range(width):
        for j in range(height):
            img[j, i] = mandelbrot(x[i] + 1j * y[j], max_iter)

    return img

width, height = 800, 800
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
max_iter = 100

mandelbrot_image = mandelbrot_set(width, height, xmin, xmax, ymin, ymax, max_iter)

plt.imshow(mandelbrot_image, extent=(xmin, xmax, ymin, ymax))
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.show()
