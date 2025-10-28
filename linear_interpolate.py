import matplotlib.pyplot as plt
import numpy as np


WAVELENGTHS_UM = [
    0.1879, 0.1916, 0.1953, 0.1993, 0.2033, 0.2073,
    0.2119, 0.2164, 0.2214, 0.2262, 0.2313, 0.2371
]

N_VALUES = [
    1.28, 1.32, 1.34, 1.33, 1.33, 1.30,
    1.30, 1.30, 1.30, 1.31, 1.30, 1.32
]


def linear_interpolate(x_new, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    if x1 == x2:
        return y1

    proportion = (x_new - x1) / (x2 - x1)
    y_new = y1 + (y2 - y1) * proportion    
    return y_new

def find_bounding_points(x_new):
    wavelengths = WAVELENGTHS_UM
    n_values = N_VALUES
    
    # --- Edge case 1: x_new is smaller than the first known point ---
    if x_new <= wavelengths[0]:
        return (wavelengths[0], n_values[0]), (wavelengths[0], n_values[0])

    # --- Edge case 2: x_new is larger than the last known point ---
    if x_new >= wavelengths[-1]:
        return (wavelengths[-1], n_values[-1]), (wavelengths[-1], n_values[-1])

    for i in range(1, len(wavelengths)):
        if wavelengths[i] >= x_new:
            # The point before it is the left neighbor (p1)
            p1 = (wavelengths[i-1], n_values[i-1])
            # This current point is the right neighbor (p2)
            p2 = (wavelengths[i], n_values[i])
            return p1, p2
        
def find_nearest_neighbor(x_new):
    wavelengths = WAVELENGTHS_UM
    n_values = N_VALUES

    min_distance = float('inf')
    nearest_n_value = None

    for i in range(len(wavelengths)):
        distance = abs(x_new - wavelengths[i])

        if distance < min_distance:
            min_distance = distance
            nearest_n_value = n_values[i] 

    return nearest_n_value

x_dense = np.linspace(min(WAVELENGTHS_UM), max(WAVELENGTHS_UM), 400)
y_interpolated = []
y_nearest = []

for x in x_dense:
    p1, p2 = find_bounding_points(x)
    y_interp = linear_interpolate(x, p1, p2)
    y_interpolated.append(y_interp)
    
    y_near = find_nearest_neighbor(x)
    y_nearest.append(y_near)

plt.figure(figsize=(10, 6))

plt.plot(WAVELENGTHS_UM, N_VALUES, 'o', color='red', label='Oryginalne dane', markersize=8)

plt.plot(x_dense, y_interpolated, '-', color='blue', label='Interpolacja Liniowa')

plt.plot(x_dense, y_nearest, '--', color='green', label='Najbliższy Sąsiad')

plt.xlabel('Długość fali (µm)')
plt.ylabel('Współczynnik załamania (n)')
plt.title('Porównanie interpolacji dla złota')
plt.legend()
plt.grid(True)

plt.show()